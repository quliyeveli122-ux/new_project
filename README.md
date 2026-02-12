 # CoffeeShop Management API:

* A robust backend system for managing a coffee shop's menu, built with Python, Django, and Django REST Framework (DRF). This API allows users to browse products, add new items, and filter the menu by specific categories.

# Technology Stack:

* Language: Python 3.13

* Framework: Django 6.0.2

* Toolkit: Django REST Framework (DRF)

* Database: SQLite (Default)

# Model Structure:
# The Coffee model consists of the following fields:

* name (CharField) – The name of the coffee.

* price (DecimalField) – The price of the product.

* ingredients (TextField) – List of ingredients.

* category (CharField) – Category of the drink (e.g., Hot/Cold).

* stock (SmallIntegerField) – Current stock quantity.

* discount (SmallIntegerField) – Discount percentage.

* created_at (DateTimeField) – The timestamp when the record was created.

# API Endpoints:
# The following API endpoints are available in this project:

* List All Coffees:
URL: http://127.0.0.1:8000/api/v1/coffees

Method: GET

* Filtering Features:
URL: http://127.0.0.1:8000/api/v1/coffees/iced

Method: GET

# Installation:
# Create and activate virtual environment:

* python -m venv venv
* venv\Scripts\activate (for windows)
* source venv/bin/activate (fro macOs)

# Install required packages:

* command: pip install -r requirements.txt

# Run database migrations:

* To create the necessary database tables based on your models, run the following commands sequentially:

* python manage.py makemigrations (To package your model changes into migration files)

* python manage.py migrate (To apply those changes to the actual database)

# Start the development server:

After completing the database setup, you are ready to launch the application. This step starts the local Django web server, allowing you to interact with your API through a browser or tools like Postman.

* How to execute this step:

Open your Terminal: Ensure you are in the project's root directory (the folder where the manage.py file is located).

Ensure Environment is Active: Your virtual environment (venv) must be active for the server to recognize Django and other installed packages.

Run the Launch Command: Execute the following command to host the project on your local machine:

Check the Output: Once successful, the terminal will display a local URL (usually http://127.0.0.1:8000/). You can copy this link into your browser to view the API.

* Important Notes:

Auto-Reload: The server is "live." If you modify your Python code and save the file, the server will automatically detect the changes and restart itself.

Terminating the Session: To stop the server and return to the standard terminal prompt, press CTRL + C on your keyboard.