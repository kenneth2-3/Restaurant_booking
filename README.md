# Restaurant_booking

# AYCE Resturant Booking System
A **Full-Stack Django Web Application** for managing table reservations, menu display, and user bookings at a restaurant called AYCE.In here []() is the live link of the game.

---

## Project Overview

AYCE Restaurant Booking System is designed to:
- Allow customers to book tables online (up to 5 guests per table).

- Avoid double bookings and prevent booking in the past.

- Let staff manage bookings and cancel if necessary.

- Showcase restaurant menu items with images and prices.

- Provide user authentication and a “My Bookings” page.

- Store media on Cloudinary for scalable management.

---

## User Stories

### Customers
1. As a customer, I want to **create an account** so that I can book tables online.  
2. As a customer, I want to **log in securely** so that my bookings are tied to my account.  
3. As a customer, I want to **book a table for 1–5 guests** so that I can dine with friends/family.  
4. As a customer, I want to **choose a specific date and time slot** so that I know when my table is reserved.  
5. As a customer, I want to be **prevented from booking in the past** so that I don’t accidentally make invalid bookings.  
6. As a customer, I want to be **stopped from booking a slot that’s already taken** so that double bookings are avoided.  
7. As a customer, I want to **view my bookings** so that I can check my upcoming reservations.  
8. As a customer, I want to **cancel my bookings** so that I can free up a table if I change my mind.  
9. As a customer, I want to **receive confirmation/notification messages** when I book or cancel so that I know my action was successful.  
10. As a customer, I want to **view the restaurant menu with pictures and prices** so that I know what’s available before visiting.

### Restaurant Staff/Admin
1. As the site owner, I want to **log in as an admin/staff** so that I can manage the restaurant’s bookings.  
2. As the site owner, I want to **see all bookings in one place** so that I can manage reservations efficiently.  
3. As the site owner, I want to **cancel or adjust reservations** if necessary (e.g., emergencies, closing times).  
4. As the site owner, I want to **manage the menu (add, update, delete items)** so that the website always reflects the current offerings.  
5. As the site owner, I want to **store images externally (Cloudinary)** so that performance and storage are optimized.  
6. As the site owner, I want to **display hero images and promotional banners** so that the site looks professional.  

---

## Technologies used

### Languages:

- [Python]: the primary language used to develop the server-side of the website.

- [JS]: the primary language used to develop interactive components of the website.

- [HTML]: the markup language used to create the website.

- [CSS]: the styling language used to style the website.

### Frameworks and Libraries

- [Django]: python framework used to create all the logic.

### Databases:

- [SQLite]: was used as a development database.

- [PostgreSQL]: the database used to store all the data.

### Other tools:

- [Git](https://git-scm.com/): the version control system used to manage the code.

- [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.

- [Gunicorn](https://gunicorn.org/): the webserver used to run the website.

- [Spycopg2](https://peps.python.org/pep-0249/): the database driver used to connect to the database.

- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.

- [Django-crispy-forms](https://django-cryptography.readthedocs.io/en/latest/): was used to control the rendering behavior of Django forms.

- [Heroku](https://www.heroku.com): the cloud platform used to host the website.

- [GitHub](https://github.com/): used to host the website's source code.

- [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.

- [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.

- [Font Awesome](https://fontawesome.com/): was used to create the icons used in the website.

- [Cloudinary](https://console.cloudinary.com/app/product-explorer): was used to make a background images for the website.

-[Wireframes.cc](https://wireframe.cc/): was used to create the sketch for the website.

- [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.

- [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.

- [PEP8](https://pep8.org/): was used to validate Python code for the website.

## Wireframes

- [Desktop Wireframes]()
- [Tablet Wireframes]()
- [Mobile Wireframes]()

## File Structure

```
AYCE_RESTAURANT/
├── accounts/           # User auth app
├── bookings/           # Table booking app
├── menu/               # Menu app
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── ayce/               # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── env.py          # Local environment variables
├── manage.py
├── Procfile            # For Heroku deployment
├── requirements.txt
├── README.md           # Project documentation
└── TESTING.md          # Manual + automated test documentation
```

## Bugs

+ **Solved bugs**

### 1. Cloudinary images not loading
- **Bug:** Images uploaded via Cloudinary were not showing in templates.  
- **Fix:** Installed `django-cloudinary-storage`, added Cloudinary configuration in `settings.py`, and updated template `img src` paths.

### 2. Double booking allowed
- **Bug:** Multiple users could book the same date and time.  
- **Fix:** Added `unique_together = ('date', 'time')` in `Booking` model and validation in `clean()` to prevent conflicts.

### 3. Past booking dates selectable
- **Bug:** Users were able to select booking dates in the past.  
- **Fix:** Added validation in `Booking.clean()` to raise an error if `self.date < today`.

### 4. Guest number exceeded limit
- **Bug:** Users could enter any number of guests (e.g., 100).  
- **Fix:** Added validation to restrict `guests <= 5` with a clear error message.

### 5. Login link not working
- **Bug:** The Login button in the navbar was not linked.  
- **Fix:** Connected it to `accounts:login` in `base.html` using Django `url` tag.

+ **Unsolved bugs**
  - None

---

## Testing

Please refer to the [TESTING.md]() file for all test-related documentation.

## Deployment

- The program was deployed to [Heroku](https://dashboard.heroku.com/).
- The program can be reached by the [Link]().

### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/kenneth2-3/Restaurant_booking).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/kenneth2-3/Restaurant_booking.git`

---

## Credits

- [GitHub](https://github.com/) for giving the idea of the project's design.
- [Django](https://www.djangoproject.com/) for the framework.
- [Heroku](https://www.heroku.com): for the free hosting of the website.
- [Cloudinary](https://console.cloudinary.com/app/product-explorer): for the free access to the background images build tool.
- [Font awesome](https://fontawesome.com/): for the free access to icons.
- [jQuery](https://jquery.com/): for providing varieties of tools to make standard HTML code look appealing.
- [Postgresql](https://www.postgresql.org/): for providing a free database.

## Author

Kenneth Adanma

Thank you for exploring AYCE Resturant!