# Web project Stepik

This project was created during the Stepik.org course: "Web-технологии". In this project, the following web application architecture is implemented (three-tier architecture):

* Front-end server (gateway): nginx
* Back-end server: gunicorn (http server)
  * Django application
  * WSGI application
* MySQL Database
  
# Nginx

Serves as a gateway. Working on 80 port (default). Using /etc/nginx_stepik.conf (for Stepik.org sandbox) or for WSL: /etc/nginx_wsl.conf (difference in directory paths). Error logging is configured to the file: /error_log.

Configured routes:
* All URLs starting with `/uploads/` (for example `/uploads/1.jpeg`) are served from the `/uploads` directory
* All URLs with an extension (for example `/img/1.jpeg`) are served from the `/public` directory
* All URLs without extension (e.g. `/question/123`) returned HTTP 404
* `/` => `http://0.0.0.0:8000` (gunicorn - django)
* `/hello/` => `http://0.0.0.0:8080` (gunicorn - wsgi app)

# Gunicorn

Runs as a daemon on port 8000 with ask.wsgi (Django) and on port 8080 with hello: app (WSGI app).

# Django application

Using the Django framework, a simple web application is implemented - "Question & Answer". Application data is stored in MySQL database.

Avalible functionality:
* Сreating questions
* Сreating answers
* Paginator
* login / sign up
* Popular questions / recent questions

Used functionality:
* Django user registration
* Django sessions, auth
* Django admin panel
* Django templates
* Django forms
* Django ORM + ModelManager

Views:
* queries like `/?page=2`:
Home page. List of "new" questions. Those the last question asked is the first on the list. Pagination work on this page. The page number is specified in the page GET parameter. 10 questions are displayed on the page. The list of questions display the titles of questions and links to pages of individual questions.
* queries like `/popular/?page=3`:
List of "popular" questions. Sorting in descending order of the rating field. Pagination work on this page. The page number is specified in the page GET parameter. 10 questions are displayed on the page. The list of questions display the titles of questions and links to pages of individual questions.
* queries like `/question/5/`:
Single question page. This page display the title, text of the question and all the answers to this question, without pagination. In case of an incorrect question id, the view return 404.
* queries like `/ask`:
Form for adding a new question.
* the answer form is located on the question page (queries like `/question/5/`). 
* queries like `/signup/`:
With a GET request, a form for entering data is displayed, with a POST request, a new user is created, the created user enters the site, and a redirect to the main page is returned.
* queries like `/login/`:
With a GET request, a form for entering data is displayed, with a POST request, the site is entered, and a redirect to the main page is returned.

# WSGI application

A simple python web application working directly with a web server (gunicorn) via the WSGI protocol without framework. Return list of received GET parameters. Each parameter on new line. 

# MySQL Database

Working on port 3306. 

Implemented tables:
* Question
* Answer

# Initializations scripts (ssh)

For deploying and run this web applications used:
* `0_env_stepik.sh` - to configure the sandbox environment
* `1_mysql_stepik.sh` - to configure the MySQL server
* `2_init_stepik.sh` - to run server / web application
