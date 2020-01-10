# ExpressShop

This is an online E-commerce web application built using django back-end framework and PostgreSQL for the database with added features like viewing products on sale, add-to-cart , checkout and payment option integrated with stripe payment gateway.

## Project Setup
1. First of all create a virtual environment inside your project's directory and make sure that its activated(*refer to: **virtual environment in python** for details*).
2. Then install the required packages mentioned in the **"requirements.txt"** file(*included in the project's directory*) using command: `pip intall -r requirements.txt`.
3. Then setup the database as mentioned below in **Database Configuration** step.
4. Then migrate to update your database using command: `python manage.py migrate`.
5. Finally, you can run the project using command: `python manage.py runserver`.



## virtual environment in python
*(Note: Strictly for Windows users, for others commands may vary slightly.)*

Browse to the directory where you want to setup your virtual environment then enter the command below:

`virtualenv <virtualenvironment_name>`

To activate the virtual environment:

`<virtualenvironment_name>\Scripts\activate`



## Database Configuration

Browse to the **"settings.py"** file in the directory: **_ExpressShop>ExpressShop>settings.py_** where you will find the following lines of code which is a setup for database.

Then enter your *'database name'*, *'password'* that you must have created in your PostgreSQL.

You can use the default *'USER': 'postgres'* and *'HOST': 'localhost'* for the PostgreSQL.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<db_name>',
        'USER': 'postgres',
        'PASSWORD': '<db_password>',
        'HOST': 'localhost'
    }
}
```



## Stripe Configuration

*(Note:Make sure that you have a stripe account for testing purpose.)*

Browse to the **"settings.py"** file in the directory: **_ExpressShop>ExpressShop>settings.py_** where you will find the following lines of code which is a setup for stripe.

Then add your stripe's test API keys.


```python
if DEBUG:
 #test keys
    STRIPE_PUBLISHABLE_KEY = ''
    STRIPE_SECRET_KEY = ''
```
