## TESTING

The program was tested constantly during its development process.
Other users also tested it in order to spot possible grammatical mistakes that the code may present.

## Manual Testing

Testing was done throughout site development, for each feature before it was merged into the master file.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.


| Feature           | User Action | Expected Result | Y/N | Comments |
|------------------|-------------|----------------|-----|----------|
| **Sign Up**       | Click on the **Sign Up** link in the navbar | Redirected to Sign Up page | Y | |
|                   | Fill in valid username, password, and confirm password | Form accepts input | Y | |
|                   | Submit Sign Up form | User account created, redirected to login page with success message | Y | |
|                   | Passwords do not match | Error message displayed | Y | |
|                   | Leave a field blank | Error message displayed | Y | |
| **Login**         | Click on the **Login** link in the navbar | Redirected to Login page | Y | |
|                   | Enter valid credentials | Redirected to homepage | Y | |
|                   | Enter invalid credentials | Error message displayed | Y | |
| **Logout**        | Click **Logout** in the navbar | User logged out, redirected to home page with a success message | Y | |
|                   | Click back button after logout | Still logged out | Y | |
| **Bookings**      | Click on **Book a Table** | Redirected to booking form | Y | |
|                   | Choose past date | Not allowed, error message shown | Y | |
|                   | Choose today/future date | Booking accepted | Y | |
|                   | Cancel an existing booking | Booking removed, success message shown | Y | |
|                   | Attempt to cancel a non-existent booking | Error handled gracefully | Y | |
| **Menu**          | Click **Menu** in navbar | Redirected to menu page | Y | |
|                   | Menu images load from Cloudinary | Correct images displayed | Y | |
| **UI/UX**         | Navbar visible on all pages | Correct navigation links displayed | Y | |
|                   | Background color is `#353537` | Consistent styling across all pages | Y | |
|                   | Forms styled for usability | Clean, modern design | Y | |
| **Errors/Validation** | Invalid form submissions | Error messages shown | Y | |
|                   | Server error | Custom error page shown | Y | |


---

## Bugs

### Known bugs

### 1. Cancelled Booking Still Blocking Slot
- **Issue:** A cancelled booking still prevented new bookings for the same slot.  
- **Fix:** Updated conflict check in `Booking.clean()` to exclude `canceled=True`.

---

### 2. Static Image Not Loading
- **Issue:** Static image (`about_us.jpg`) not showing.  
- **Fix:** Ensured `STATICFILES_DIRS` and `{% load static %}` were configured correctly in settings and templates.

### Solved bugs

There were plenty of bugs during the development process since this project was a learning platform for me and allowed me to improve my skills and knowledge significantly.

However, I tried to solve the majority of them. And one of the bugs that I remember perfectly was related to the extension of the allauth Register form. I was able to solve it by customizing the allauth sign up form. Moreover, I encountered the problem of making the form work as the migrations were not working. What I have done to migrate the changes is to migrate the app first and then perform the rest of the migrations.

---


## Validation

### HTML Validation

- [HTML Validation Report](documentation/validation/home.html_validation.png)

- No errors or warnings were found when passing through the official [W3C](https://validator.w3.org/) validator. This checking was done manually by copying the view page source code and pasting it into the validator.


### CSS Validation

- [CSS Validation Report](documentation/validation/css_validation.png)

- No errors or warnings were found when passing through the official [W3C (Jigsaw)](https://jigsaw.w3.org/css-validator/#validate_by_uri) validator, css code works perfectly on various devices.


### Python Validation

- [Python Validation Report](documentation/validation/python_validation.png)

- No errors were found when the code was passed through code institutes python linter [online validation tool](https://pep8ci.herokuapp.com/).This checking was done manually by copying python code and pasting it into the validator.


---

## Lighthouse Report

### Home Page

![Lighthouse Report. Home Page](documentation/lighthouse_reports/lighthouse_home.png)

### Menu Page

![Lighthouse Report. Menu Page](documentation/lighthouse_reports/lighthouse_menu.png)

### Book Page

![Lighthouse Report. Book Page](documentation/lighthouse_reports/lighthouse_book.png)

### My Bookings Page

![Lighthouse Report. My Bookings Page](documentation/lighthouse_reports/lighthouse_mybookings.png)

### Login Page

![Lighthouse Report. Login Page](documentation/lighthouse_reports/lighthouse_login.png)

### Logout Page

![Lighthouse Report. Logout Page](documentation/lighthouse_reports/lighthouse_logout.png)

### Sign Up Page

![Lighthouse Report. Register Page](documentation/lighthouse_reports/lighthouse_signup.png)

---

## Compatibility

Testing was conducted on the following browsers;

- Chrome

   - [Compatibility Report](documentation/compatibility_reports/compatibility_chrome_home.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_chrome_menu.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_chrome_book.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibilty_chrome_login.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_chrome_register.png)

- Firefox

   - [Compatibility Report](documentation/compatibility_reports/compatibility_firefox_home.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_firefox_menu.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_firefox_book.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_firefox_login.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_firefox_register.png)

- Safari

   - [Compatibility Report](documentation/compatibility_reports/compatibility_safari_home.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_safari_menu.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_safari_book.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_safari_login.png)
   - [Compatibility Report](documentation/compatibility_reports/compatibility_safari_register.png)

---

### Responsiveness 

- The websites responsiveness was checked manually by using devtools implemented in (Chrome) throughout the whole development. It was also checked with [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb/related?hl=en) Chrome extension.

- Home Page

   - [Responsiveness Report](documentation/responsiveness_reports/responsive_home.png)
   - [Responsiveness Report](documentation/responsiveness_reports/responsive_home_largescreen.png)
   - [Responsiveness Report](documentation/responsiveness_reports/responsive_home_aboutus.png)
   - [Responsiveness Report](documentation/responsiveness_reports/responsive_home_aboutus_lg.png)
    - [Responsiveness Report](documentation/responsiveness_reports/responsive_home_footer.png)
    - [Responsiveness Report](documentation/responsiveness_reports/responsive_footer_lg.png)

- Menu Page

   - [Responsiveness Report](documentation/responsiveness_reports/responsive_menu.png)
   - [Responsiveness Report](documentation/responsiveness_reports/responsive_menu_lg.png)

- Book Page

   - [Responsiveness Report](documentation/responsiveness_reports/responsive_book.png)
   - [Responsiveness Report](documentation/responsiveness_reports/responsive_book_lg.png)

- Login Page

   - [Responsiveness Report](documentation/responsiveness_reports/responsive_login.png)
   - [Responsiveness Report](documentation/responsiveness_reports/responsive_login_lg.png)

- Sign Up Page

   - [Responsiveness Report](documentation/responsiveness_reports/responsive_signup.png)
   - [Responsiveness Report](documentation/responsiveness_reports/responsive_signup_lg.png)


---
