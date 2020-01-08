from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order


class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = "home-page.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "product-page.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item is in the order.
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated to your Cart.")
            return redirect("shop:item_detail", slug=slug)

        else:
            messages.info(request, "This item was added to your Cart.")
            order.items.add(order_item)
            return redirect("shop:item_detail", slug=slug)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your Cart.")
        return redirect("shop:item_detail", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        # check if the order item is in the order.
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your Cart.")
            return redirect("shop:item_detail", slug=slug)
        else:
            # add a message saying the order doesnot contain the item
            messages.info(request, "This item was not in your Cart.")
            return redirect("shop:item_detail", slug=slug)

    else:
        # add a message saying the user doesnot have the order
        messages.info(request, "You donot have an active order.")
        return redirect("shop:item_detail", slug=slug)


