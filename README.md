# WELCOME TO ZAWADI E-COMMERCE STORE. YOUR ONE-STOP ONLINE SHOP FOR PURCHASING BEAUTIFUL AFRICAN ART PIECES
<br>
<br>

<img src="docs/navigation/homepage.png">

<br>

# 1. Motivation:

This project aims to create an online e-commerce store that celebrates and showcases African art pieces. Our motivation is to provide art enthusiasts, collectors, and anyone interested in African culture with a platform to explore, appreciate, and purchase unique and authentic African artworks.

# 2. User Experience:

The focus is to provide users with a seamless and enjoyable experience. The aim is to create an intuitive and visually appealing interface that allows users to easily browse, view, and purchase African art pieces. By offering a user-friendly website accessible on multiple devices, I want to ensure that users have a delightful experience regardless of whether they're using a desktop, tablet, or mobile device.

# 3. User Stories:

- As a user, I want to explore a diverse collection of African art pieces.
- As a user, I want to view detailed information, images, and prices for each art piece.
- As a user, I want to be able to search dynamically for relevant art by origin, type, artist and price.
- As a user, I want to be able to add art pieces to my shopping cart for future purchase.
- As a user, I want the option to create an account to track my orders and manage my profile.
- As a user, I want to be able to add, update and delete items from my shopping cart.
- As a user, I want a secure and convenient payment option using Stripe for a smooth checkout process.

# 4. Website Goals:

- Showcase a wide variety of African art pieces to captivate users.
- Provide comprehensive product details and clear pricing information.
- Offer in-depth search/filtering functionality for users to find relevant products.
- Implement a user-friendly shopping cart system for easy product selection.
- Offer user account functionality to enhance the customer experience.
- Ensure a secure and smooth payment process through Stripe integration.
- Create a responsive design that works seamlessly across different devices.
- Utilize Bootstrap for structured and visually appealing templates.

# 5. Requirements:

- Django web framework for backend development.
- Flask for handling certain functionalities.
- HTML, CSS, and Bootstrap for frontend templates.
- Stripe API for payment processing.
- JSON file for storing product data.
- Responsive design to support mobile, tablet, and desktop views.
- User and Password authentication system for account creation and management.

# 6. Expectations:

I expect that the project will result in a fully functional e-commerce store for African art pieces. Users will be able to browse, select, and purchase products with ease. The integration of Stripe will enable secure and efficient payments. The website will be responsive, ensuring a consistent experience across devices. Our goal is to create a visually appealing and intuitive platform that encourages users to explore and embrace African art.

# 7. Design:

The website's design will be structured using Bootstrap, a popular frontend framework that offers responsive and aesthetically pleasing templates. I'll focus on a clean, modern design that highlights the beauty of African art. The use of images, fonts, and colors will be carefully chosen to create an engaging visual experience. I will prioritize user-friendly navigation and clear product presentation, ensuring that users can easily find what they're looking for and enjoy the art pieces showcased on the platform.

### Color schema:

- Dark grey
- Dark Gold
- Dark Green

Using backgrounds of African Savannah with gold hue color scheme

### Font Choices 

Segoe UI , Roboto, Helvetica Neue, Noto Sans, Liberation Sans

## Wireframes

- Navbar.

    <details><summary>Picture</summary>
    <img src="docs/wireframes/navbar.png" alt="navbar wireframe">
    </details>
    <br>

- Home Page.

    <details><summary>Picture</summary>
    <img src="docs/wireframes/home_page.png" alt="home wireframe">
    </details>
    <br>

- Search Box

    <details><summary>Picture</summary>
    <img src="docs/wireframes/searchbox.png" alt="search wireframe">
    </details>
    <br>

- Products (ALL & Various Categories)

    <details><summary>Picture</summary>
    <img src="docs/wireframes/products_template.png" alt="products wireframe">
    </details>
    <br>

- Product Card

    <details><summary>Picture</summary>
    <img src="docs/wireframes/product_card.png" alt="productcard wireframe">
    </details>
    <br>

- Refined Search

    <details><summary>Picture</summary>
    <img src="docs/wireframes/custom_search.png" alt="custom wireframe">
    </details>
    <br>

- Cart

    <details><summary>Picture</summary>
    <img src="docs/wireframes/cart.png" alt="cart wireframe">
    </details>
    <br>

# Data Structure

## Database

Product:

| Object | Field |
|---|---|
| ID | is automatically generated |
| PK | DecimalField |
| Name | CharField |
| Description | CharField |
| Image | CloudinaryField |
| Origin | CharField |
| Origin_Image | CloudinaryField |
| Origin_Code | CharField |
| Style | CharField |
| Price | DecimalField |
| Category | CharField |
| Status | CharField |

<hr>

Cart:

| Object | Field |
|---|---|
| Session | OneToOneField - Session|
| Products | ManyToOneField - Product|

<hr>

CartItems:

| Object | Field |
|---|---|
| Cart | ForeignKey - Cart |
| Products | ForeignKey - Product |

<hr>

Order:

| Object | Field |
|---|---|
| User | ForeignKey - User |
| Created_At | DateToTimeField |
| Updated_At | DateToTimeField |
| Total_Amount | DecimalField |

<hr>

ShippingAddress:

| Object | Field |
|---|---|
| Order | OneToOneField - Order |
| Full_Name | CharField |
| Address_Line_1 | CharField |
| Address_Line_2 | CharField |
| City | CharField |
| Province | CharField |
| Postal_code | CharField |
| Country | CharField |

<hr>

## Logic

<img src="docs/flowchart.png" alt="website logic" width="1000">

# Website Structure

- Most of website structure comes from Bootstrap itself, and rest is just overrides to make it look nicer.

|  Screen size |  Breakpoint |
|---|---|
| extra small | >= 320px |
| small | >= 576px |
| medium | >= 768px |
| Custom | 768 >= 900 |
| Custom | >= 990 | 

# Technology, Frameworks and Libraries used.

## Languages

- [HTML](https://en.wikipedia.org/wiki/HTML5) 

- [CSS](https://en.wikipedia.org/wiki/CSS)

- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

<br>

## Frameworks and Libraries used.

- [Django](https://www.djangoproject.com/) Python-based web framework that follows the model–template–views architectural pattern.

- [Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) HTTP server interface.

- [Psycopg](https://wiki.postgresql.org/wiki/Psycopg) Postgres database adaptor.

- [Stripe](https://stripe.com/) Payments.

- [Bootstrap](https://getbootstrap.com/) Bootstrap 5 was used in this project.

- [FontAwesome](https://fontawesome.com/) Icons used in this project.

- [Jquery](https://en.wikipedia.org/wiki/JQuery)

- [Crispy forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html) for forms.

<br>

## Tools

- [Heroku](https://www.heroku.com) Deployment of website.

- [Cloudinary](https://cloudinary.com/) Storing static files and images.

- [Balsamiq](https://balsamiq.com/) Wireframes.

- [Draw.io](draw.io) for flowcharts

- [Flaticon](https://www.flaticon.com/) For flag and navbar icons

<br>

# Features

- Responsive on all devices.
- Profile accounts.
- Custom search bar and filtering
- Saving details at checkout to user account.
- Checkout with Stripe payments.
- Products and Categories.
- Newsletter
- Emails on newsletter signup, checkout confirmation
- Sale.

<br>

# Navigation

## HOME PAGE

<details>
  <summary>Home Page</summary>

  HOME PAGE | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  'Home Page' template will be the first thing the user sees when opening the page | ![](docs/navigation/homepage.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Home Page with Search Box</summary>

  HOME PAGE SEARCH| PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Dynamic Searhc/Filtering box to navigate to specific products. Opens up when user clicks the search bar | ![](docs/navigation/homepage-with-searchmodal.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Search box</summary>

  SEARCH BOX | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Visuals of the dynamic search box | ![](docs/navigation/searchbox.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Navigation Bar</summary>

 NAVBAR | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Visuals of the Navbar when user lands on the page for the first time | ![](docs/navigation/navbar.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Navigation Bar - Post-Login</summary>

 NAVBAR-POST-LOGIN | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Visuals of the Navbar when user has registered/logged in | ![](docs/navigation/navbar-post-login.png) | ![](#)| ![](#)

</details>

<br>

## PRODUCTS

<details>
  <summary>Custom Search Page</summary>

 ALL PRODUCTS | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Custom Search' page | ![](docs/navigation/custom-search-page.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>All Products Page</summary>

 ALL PRODUCTS | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'All Products' page | ![](docs/navigation/all-products.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Sculptures</summary>

 SCULPTURES | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Sculptures' page | ![](docs/navigation/sculptures.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Frames</summary>

 FRAMES | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Frames' page | ![](docs/navigation/frames.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Crafts</summary>

 CRAFTS| PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Crafts' page | ![](docs/navigation/crafts.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Sale</summary>

 SALE| PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Sale' page | ![](docs/navigation/sale.png) | ![](#)| ![](#)

</details>

<br>

## CART

<details>
  <summary>Cart Page</summary>

 CART | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Cart' page | ![](docs/navigation/cart.png) | ![](#)| ![](#)

</details>

<br>

## CHECKOUT

<details>
  <summary>Checkout Page</summary>

 CHECKOUT | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Checkout' page | ![](docs/navigation/checkout.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Payment Confirmation</summary>

 PAYMENT CONFIRMATION | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Payments' page | ![](docs/navigation/checkout.png) | ![](#)| ![](#)

</details>

<br>

## USER AUTHENTICATION

<details>
  <summary>Register</summary>

 REGISTER | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Register' page | ![](docs/navigation/register.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Login</summary>

 LOGIN | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Login' page | ![](docs/navigation/login.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>Logout</summary>

 REGISTER | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Register' page | ![](docs/navigation/register.png) | ![](#)| ![](#)

</details>

<br>

<details>
  <summary>User Profile</summary>

 PROFILE | PC | TABLET | PHONE
  :---:|:---:|:--:|:--:
  Template view of 'Profile' page | ![](docs/navigation/profile.png) | ![](#)| ![](#)

</details>

<br>

# TESTING

## Manual Testing:

<details>
  <summary>Home Page Search Features</summary>

 DESCRIPTION | HOME PAGE | HOME PAGE SEARCH BOX
  :---:|:---:|:--:
Search bar in the center of the homepage is clicked and provides a dropdown menu for various categories to be filtered by the user| ![](docs/navigation/homepage.png)| ![](docs/navigation/homepage-with-searchmodal.png)

</details>

<br>

<details>
  <summary>Search Filtering & Results</summary>

 DESCRIPTION | SEARCH BOX | SEARCH RESULTS
  :---:|:---:|:--:
Search bar in the center of the homepage can be filled with user's exact search/filtering specifications, and the 'Custom Search' page will render the relevant products accordingly, including a filter-summary for the user| ![](docs/navigation/searchbox.png)| ![](docs/navigation/custom-search-page.png)

</details>

<br>

<details>
  <summary>Products Dropdown</summary>

 DESCRIPTION | DROPDOWN | CATEGORY
  :---:|:---:|:--:
Products navlink should display a dropdown menu to provide options to select art from various categories, which will take you to the relevant praduct category page| ![](docs/navigation/products-dropdown.png)| ![](docs/navigation/sculptures.png)

</details>

<br>

<details>
  <summary>Adding Product</summary>

 DESCRIPTION | ADD PRODUCT | PROMPT
  :---:|:---:|:--:
User clicks on 'Add to cart' button inside the product-card. Modal appears to tell user they have successfully added said product, as well as an alert message popping up in the navbar telling user how many products are in their cart| ![](docs/navigation/add-product-popup.png)| ![](docs/navigation/cart-confirmation.png)

</details>

<br>

<details>
  <summary>Cart Update</summary>

 DESCRIPTION | UPDATE CART | SUCCESS
  :---:|:---:|:--:
Cart will display user's product selections. Update button should give user the option to increase an/or decrease the amount of one product| ![](docs/navigation/update-cart.png)| ![](docs/navigation/update-cart-success.png)

</details>

<br>

<details>
  <summary>Cart Delete Product</summary>

 DESCRIPTION | CART PRODUCT DELETE |DELETE SUCCESS
  :---:|:---:|:--:
Cart will display user's product selections. Delete button should give user the option to remove selected product, as well as prompt for a defensive modal to pop up asking whether the user is sure they want to delete| ![](docs/navigation/cart-remove-product.png)| ![](docs/navigation/cart-product-remove-success.png)

</details>

<br>

<details>
  <summary>Registration</summary>

 DESCRIPTION | REGISTER |SUCCESS
  :---:|:---:|:--:
Clicking on 'Register' navlink in navigation bar will prompt user to fill in credentials combined with instructions to follow. Once user has completed the registration, a welcome/success message will appear routed within the user's new profile page| ![](docs/navigation/register.png)| ![](docs/navigation/register-success.png)

</details>

<br>

<details>
  <summary>Login Existing User</summary>

 DESCRIPTION | LOGIN |SUCCESS
  :---:|:---:|:--:
Clicking on 'Login' navlink in navigation bar will prompt user to fill in credentials. Once user has completed the login, a welcome/success message will appear in the navbar welcoming the user back| ![](docs/navigation/login.png)| ![](docs/navigation/post-login.png)

</details>

<br>