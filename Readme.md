# Honey Shop

## Project Milestone Four - Code Institute

The [Honey Shop](https://honeyshopstef.herokuapp.com/) app was developed and deployed by : 
<h2 style="color: #e34525;"> Stefan Sarbu</h2>as the last project for the : <h2 style="color: #e34525;">Code Institute</h2> <h2 style="color: blue;">Full Stack Software Development Diploma</h2>

This website/app is to emulate an e-commerce store where visitors can buy different honey products.

### Live App here: https://honeyshopstef.herokuapp.com/

## Table of contents

1. [UX](#UX)
    1. [User goals](#User-goals)
    2. [Design choices](#Design-choices)
    3. [Colors](#Colors)
    4. [Wireframes](#Wireframes)
2. [Features](#Features)
    1. [Accounts](#Accounts)
        1. [Register page](#Register-page)
        2. [Login page](#Login-page)
        3. [Reset password](#Reset-password)
    2. [Honey Shop](#HoneyShop)
        1. [Navigation and pages](#Navigationandpages)
        2. [Products](#Products)
        3. [Product details](#Product-details)
    3. [Cart](#Cart)
    4. [Checkout](#Checkout)
    5. [Search](#Search)
    6. [Admin page](#Admin-page)
    7. [Features left to implement](#Features-left-to-implement)
3. [Technologies](#Technologies)
    1. [Tools](#Tools)
    2. [Libraries and frameworks](#Libraries-and-frameworks)
    3. [Languages](#Languages)
4. [Testing](#Testing)
      
5. [Deployment](#Deployment)
    1. [Instructions](#Instructions)
    2. [Deployment to Heroku](#Deployment-to-Heroku)
    3. [Add static files to AWS s3](#Add-static-files-to-AWS-s3)
6. [Credits](#Credits)
    1. [Media](#Media)
    2. [Code](#Code)
    3. [Acknowledgment](#Acknowledgment)
 

# UX

## User goals
The target audience of Honey Shop are:
- People who want to eat healthy and to use honey products for different purposes in their diet or meals.
- People who are looking for the best products on the market.
- Bee lovers who acknowledge the quality and benefits of using honey.

User goals:
- Search for honey typing different keywords and receive a feedback by the website if it isn't available.
- Find information about the team's passion to produce, import and sell high quality honey products.
- Finding the product, product details and description will be displayed together with the price and the rating of it.
- User can scroll on products page and through different product categories.
- User can register/signup and that way a personal profile will be created.
- After registration user can easily login. 
- For each step the user will receive an error, alert, warning or success message.
- If the user is not logged in they will be redirected to the login page before go to the cart page.
- Edit the shopping cart if required.
- Checkout using card payment.
- Once the payment is done a success message is sent below the navbar.

## Design choices
The Honey Shop website is a e-commerce store application that was designed for customers, people who want to buy unique, high quality honey products.
Therefore, the website design was designed to bring these characteristics to its users. In which all of its design details is aligned to its purpose.

### Fonts
- The font used in this project is [Sriracha](href="https://fonts.googleapis.com/css2?family=Sriracha&display=swap") which is an user friendly mainly used by its creator Google to give a proper reading in different screen sizes.

### Colors
   - Chocolate: ![#D2691E](https://via.placeholder.com/15/D2691E/000000?text=+) `#D2691E`
   - Light-grey: ![#AAB7C4](https://via.placeholder.com/15/AAB7C4/000000?text=+) `#AAB7C4`
   - White: ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+) `#FFFFFF`
   - Black: ![#000000](https://via.placeholder.com/15/000000/000000?text=+) `#000000`
   
  #### These set of colors were chosen to bring a smooth experience to the users as same as to match with the purpose of the application.


### Wireframes
The wireframes developed for this project was only taken two types of devices, desktop and mobile.
In addition, the tool used to develop this wireframes was [Balsamiq](https://balsamiq.com/) giving the ability to a rapid design. There are several mockups below :
<p align="center">
<h4>Main page<h4>
<img src="/static/images/readme_images/Shop.png" width="75%">
</p>
<p align="center">
<h4>About page<h4>
<img src="/static/images/readme_images/Shop-about.png" width="75%">
</p>
<p align="center">
<h4>All products<h4>
<img src="/static/images/readme_images/Shop-All.png" width="75%">
</p>
<p align="center">
<h4>Product Details<h4>
<img src="/static/images/readme_images/Shop-productDetails.png" width="75%">
</p>
<p align="center">
<h4>Register<h4>
<img src="/static/images/readme_images/Shop-Reg.png" width="75%">
</p>
<p align="center">
<h4>Login<h4>
<img src="/static/images/readme_images/Shop-S.png" width="75%">
</p>
<p align="center">
<h4>Main page mobile and About Page Mobile<h4>
<img src="/static/images/readme_images/Shop Android.png" width="35%">
<img src="/static/images/readme_images/Shop-About Android.png" width="36%">
</p>

<p align="center">
<h4>All Products and Product Details Mobile<h4>
<img src="/static/images/readme_images/Shop-all Android.png" width="35%">
<img src="/static/images/readme_images/Shop-productDetails Android.png" width="35%">
</p>

<p align="center">
<h4>Register and Login Mobile<h4>
<img src="/static/images/readme_images/Shop-Reg Android.png" width="35%">
<img src="/static/images/readme_images/Shop-S Android.png" width="35%">
</p>

# Features

Honey Shop website is composed by seven different applications: `home`, `bag`, `checkout`, `honeyshopstef`,  `products`, `profiles` and `about`. Using MVC architecture from the Django framework, each application holds its own model, view and controller that interacts all together.

## Accounts
 The accounts app holds the functionality of register, login, logout and the reset password.

### Register page
<p align="center">
<img src="/static/images/readme_images/register.png" width="40%">
</p>

  - An username, email and password is required to create an account.
  - Username must be unique.
  - Password should not be short, must contain at least 8 characters and should not be common.
  - As soon as the user creates its username they are redirected to home page.

### Login page
<p align="center">

<img src="/static/images/readme_images/login.png" width="40%">
</p>
  - The login page is a normal page that will ask for the name or email and the user password who already registered their account.

### Reset password
  - Step 1: at the login page, above of the button you can find the `forgot password` link in which will lead to a form to add your account email.
  - Step 2: Add the email from the account you need to reset the password.
  - Step 3: You will receive an email with a link that will allow you to add a different password sending you to a reset password form.
  - Step 4: Add a new password and confirm it.
  - Step 5: Once the password is set you can login with the new password.
  
  <p align="center">
  <img src="/static/images/readme_images/passwordreset.png">
  </p>

## Honey Shop

Honey Shop app holds all the main pages in which the user will navigate. Such as:

#### Navigation and pages
  <p align="center">
  <img src="/static/images/readme_images/home.png">
  </p>

  - On the home page the navbar is displayed with the menu bar and the user can select from the Honey page dropdown menu the option that is preffered. Here, the honey products are filtered by "`Price`" , "`Rating`" and/or "`Category`" or if the user wishes to check all products then the `All Honey` button is available. 
  - Clicking on Home/HoneyShop logo (brand name) will send the user back to the main app's page.
  - On the `About` page, the user will find some interesting facts about the company and the team. 
    
    <p align="center">
    <img src="/static/images/readme_images/about.png">
    </p>

  - Further down the page there's a simple and intuitive footer.

    <p align="center">
    <img src="/static/images/readme_images/footer.png">
    </p>

  ### Products

  <p align="center">
  <img src="/static/images/readme_images/products.png" width="40%">
  </p>

  - Clicking on Honey from the navbar then All Honey, or on Shop Honey button from the main page or on the HoneyShop option from the footer section the user will be able to see all the honey products from the store. 
  - Here, the honey products can be filtered by: 
  - `Category` and `Name` (`A-Z, Z-A`)
  - `Price` and `Rating` (`Low to High, High to Low`).

### Product details  

  <p align="center">
  <img src="/static/images/readme_images/product-detail.png" width="40%">
  </p>
  
  - The page that gives the full detail about the product as well as the possibility to add it to cart.
  - In addition, the user can increment or decrement the quantity of the product.
  - If the user wants to add extra honey products to the cart the `More Honey`  button it's available.

## Cart
<p align="center">
<img src="/static/images/readme_images/cart.png">
</p>

 The cart app gives the user the ability to `view`, `add` and `adjust` the cart. Including the option to increase `+` and/or decrease `-` the quantity of the product and updating the quantity with `Update` or removing the product from the cart with `Remove`.
  
  

## Checkout

<p align="center">
<img src="/static/images/readme_images/checkout_image.png" width="40%">
</p>

  - The checkout application holds and manipulates the `Stripe` API. In which empowers the overall application with the e-commerce functionality.
  - In this application is developed and performed the forms users who are willing to buy products, to add their details into the checkout application forms and finalise the purchase.


## Search
<p align="center">
<img src="/static/images/readme_images/search.png" width="40%">
</p>

  - Under the search application, a simple search functionality is used to find different products from the store using the keywords.
  - If a keyword is typed on the search bar but doesn't find anything in the data base, a message will be displayed instead.


## Admin page


  - The admin page has several sections:
     - Authentication and Authorization, where the admin can see and manage the users on the website.
     - Checkout, where the admin can see the orders done by the customers.
     - Add or remove products to the e-commerce store.



## Features Left To Implement
  1. Comments from the user for the products.
  2. Add login option via social (e.g facebook, google).
  3. Add paypal payment option.
  4. Add EN/ES language button.

# Technologies

## Tools

  - [Gitpod](https://gitpod.io/) as an IDE to develop this project.
  - [Stripe](https://stripe.com/ie) to receive payments.
  - [Heroku](https://www.heroku.com/) for hosting the application and deploy.
  - [AWS S3](https://aws.amazon.com/s3/) was used as a cloud service to host static files.
  - [Github](https://github.com/) to share and store code remotely.
  - [Diffchecker](https://www.diffchecker.com/) to check code differences and edits made.
  - [PostgreSQL](https://www.postgresql.org/), a robust database provided by Heroku for production development.
  - [Balsamiq](https://balsamiq.com/) for the wireframes design.

## Libraries and frameworks

  - [Django](https://www.djangoproject.com/) a high level python web-framework used to design this project.
  - [Bootstrap 4](https://getbootstrap.com/) a CSS library grid used for the development of this site.
  - [FontAwesome](https://fontawesome.com/) for the creation and implementation of icons.
  - [Google fonts](https://fonts.google.com/) to bring custom font styling.
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) a template language for python used to bring logic into templates.
  - [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/#description) used as the Python PostgreSQL adapter.
  - [Jquery](https://jquery.com/) a Javascript library to simplify the code.
  - [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) a library that enables python code to modify AWS service.
  - [AOS](https://michalsnik.github.io/aos/) used to bring animation on scroll.

## Languages

  - This project uses HTML, CSS, Javascript and Python programming languages.


# Testing

The testing was made on different browsers, for mobile, tablet and desktop displays.


# Deployment

For the deployment you will need tool as:

  - An IDE such as [Gitpod](https://gitpod.io/) 
- To continue on the process of deployment you should have accounts on the following services:

  - [Stripe](https://stripe.com/ie)
  - [AWS](https://aws.amazon.com/s3/)
  - [Gmail](https://gmail.com)

### Instructions
  1. Download a copy of this repository from the link https://github.com/iiostefanos/honeyshopstef as a download zip file. Or at your terminal do the following git command:

      ```
      $ git clone https://github.com/iiostefanos/honeyshopstef
      ```
  2. If you downloaded the project as a zip file, unzip it and add it in your directory.
  3. To not run in some unexpected behaviours during development, a virtual environment is advised to be used before the project be installed in your machine. So create a virtual environment with the command:

      ```
     $ python -m venv venv
      ```
  4. After you already created the virtual environment folder you need to activate it:

      ```
      $ source venv/bin/activate
      ```
  5. Install requirements.txt file.

      ```
      $ pip install -r requirements.txt
      ```
  6. Create an `env.py` file to store environment variable keys.

     ```
     import os

     os.environ.setdefault('SECRET_KEY', '<secrete key>')
     os.environ.setdefault('DATABASE_URL', '<postgres key>')

     """ STRIPE API Keys """
     os.environ.setdefault('STRIPE_PUBLISHABLE', '<stripe publishable key>')
     os.environ.setdefault('STRIPE_SECRET', '<stripe secret key>')

     """ AWS API Keys """
     os.environ.setdefault('AWS_ACCESS_KEY_ID', '<aws access key id>')
     os.environ.setdefault('AWS_SECRET_ACCESS_KEY', '<aws secret access key>')

     """ Email Keys """
     os.environ.setdefault('EMAIL_ADDRESS', '<your email here>')
     os.environ.setdefault('EMAIL_PASSWORD', '<your email password here>')
     ```
  7. Add a git ignore file to not submit sensitive data to Github repository.

     ```
     $ touch .gitignore
     ```
     - Then add the `env.py` to the `.gitignore` file.

     ```
     $ git update-index --assume-unchanged env.py
     ```
     - Depending where the the `env.py` is locate the path will change.

  8. Migrate the models to crete a database template.

      ```
      $ python manage.py migrate
      ```
  9. In this step you will need to create a super user to have access to the admin page.

      ```
      $ python manage.py createsuperuser
      ```
  10. So, after you do all the steps to create a super user you can now run the server.

      ```
      $ python manage.py runserver
      ```
  11. After the server is running locally add the `/admin` path at the end of the url link. It might look like this if you are not running another application.

      ```
      http://127.0.0.1:8000/admin
      ```

### Deployment to Heroku

To make the deployment of this application to `Heroku` you will need to do the following steps.

  1. Signup for [Heroku](https://signup.heroku.com/)
  2. Install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli)
  3. After installing `Heroku toolbelt` add the following code into your termial and login into your account you already create.
     ```
     $ heroku login
      Enter your Heroku credentials.
      Email: your@email.com
      Password (typing will be hidden):
      Authentication successful.
     ```
  4. Save all the requirements into the `requirements.txt` as mentioned before with the command:
     ```
     $ pip freeze > requirements.txt
     ```
  5. Create a file named `Procfile` and add the following config.
     ```
     web: gunicorn main_tour_folder.wsgi
     ```
 6. After all the setup is done `git add .`, `git commit` and `git push` your application to a repository you created on Github.
 7. In your `Heroku` account click new and create new app.
 9. Select your region and create a name for your project.
10. In your `Heroku` settings click `reveal config vars`.
11. Add the following config variables:

| KEY            | VALUE         |
|----------------|---------------|
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |
| AWS_SECRET_ACCESS_KEY | `<your aws secret access key>`  |
| DATABASE_URL| `<your postgres database url>`  |
| EMAIL_ADDRESS| `<your email address>`  |
| EMAIL_PASSWORD | `<your email password>` |
| SECRET_KEY | `<your secret key>`  |
| STRIPE_PUBLISHABLE| `<your stripe publishable key>`  |
| STRIPE_SECRET| `<your stripe secret key>`  |
| AWS_ACCESS_KEY_ID | `<your aws access key>`  |

12. Add a development (postgres) database:
  ```
  $ heroku addons:add heroku-postgresql:dev
    heroku addons:add heroku-postgresql:dev
    Adding heroku-postgresql on deploy_django... done, v13 (free)
    Attached as HEROKU_POSTGRESQL_COPPER_URL
    Database has been created and is available
    ! This database is empty. If upgrading, you can transfer
    ! data from another database with pgbackups:restore.
    Use `heroku addons:docs heroku-postgresql` to view documentation.

  $ heroku pg:promote HEROKU_POSTGRESQL_COPPER_URL
    Promoting HEROKU_POSTGRESQL_COPPER_URL to DATABASE_URL... done
   ```
13. After adding the config into your dashboard add the following commands.
  - `$ heroku login`
  - `heroku git:remote -a test-app-to-deploy`
  - `$ git push heroku master`

14. On your `Heroku` dashboard click on `open app` button and check if the application is running correctly.

### Add static files to AWS s3

1. If there is a need to add your static files to AWS S3 you can follow [this tutorial](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html). 

# Credits

## Media
The photos and video used in the project were downloaded from:

- https://www.freepik.com

- https://www.pngwing.com/en/free-png-ykeop/download


- https://wallpaperaccess.com/honey


## Fonts 

Font-family: [`Sriracha, cursive`](https://fonts.googleapis.com/css2?family=Sriracha&display=swap) 

#### Platforms that provides no-copyright media and free downloads.

## Code
  
  - The `accounts`, `cart` and `checkout` apps were recycled from the [Code Institute](https://github.com/Code-Institute-Org) lessons but modified to fit with the project purpose.

## Acknowledgment
  - Special thanks to the Code Institute's 24/7 tutor team (Chris, Miklos, Kevin, Samantha, Michael, Stephen, Anna,  and Scott) and all the good willing and helpful programmers from Slack.
  - Many thanks also to Rahul Lakhanpal who is my Code Institute mentor for this project, for offering 
 ideas and solutions to various issues throughout the project, as well as endless patience and understanding!