# Zomato Clone

This is a Django-based web application that allows users to browse, search, and order food from various restaurants. The project includes features such as user authentication, restaurant management, dynamic food menus, search and filter options, order management, reviews and ratings, and responsive design.

## Features

- **User Authentication**: Users can register, log in, and manage their profiles.
- **Restaurant Management**: Admins can add, update, and delete restaurant information.
- **Dynamic Food Menus**: Restaurants can manage their menu items, including prices and availability.
- **Search and Filter Options**: Users can search for restaurants and filter results based on cuisine, ratings, and location.
- **Order Management**: Users can place orders, view order history, and track order status.
- **Reviews and Ratings**: Users can leave reviews and ratings for restaurants.
- **Responsive Design**: The application is designed to work on various devices, including desktops, tablets, and smartphones.

## Project Structure

```
zomato_clone/
├── zomato_clone/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── restaurants/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── restaurants/
│           ├── base.html
│           ├── index.html
│           ├── restaurant_detail.html
│           ├── menu.html
│           └── order.html
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── users/
│           ├── login.html
│           ├── register.html
│           └── profile.html
├── orders/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── orders/
│           ├── order_list.html
│           ├── order_detail.html
│           └── order_confirmation.html
├── manage.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd zomato_clone
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Visit `http://127.0.0.1:8000/` to access the application.
- Users can register, log in, and start browsing restaurants and placing orders.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you'd like to add.