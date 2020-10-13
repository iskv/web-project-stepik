# Web project Stepik

This project was created during the Stepik.org course: "Web-технологии". In this project, the following web application architecture is implemented:

* Front-end server (gate): nginx
* Back-end servers:
  * Gunicorn (http server)
    * Django
    * WSGI application
  * MySQL Database
  
# Nginx

Serves as a gate. Working on 80 port (default). Using /etc/nginx_stepik.conf (for Stepik.org sandbox) or for WSL: /etc/nginx_wsl.conf (difference in directory paths). Error logging is configured to the file: /error_log.

Configured routes:
* All URLs starting with `/uploads/` (for example `/uploads/1.jpeg`) are served from the `../uploads` directory
* All URLs with an extension (for example `/img/1.jpeg`) are served from the `../public` directory
* All URLs without extension (e.g. `/question/123`) returned HTTP 404
* `/` => `http://0.0.0.0:8000` (gunicorn - django)
* `/hello/` => `http://0.0.0.0:8080` (gunicorn - wsgi app)

# Gunicorn

Runs as a daemon on port 8000 with ask.wsgi (django) and on port 8080 with hello: app (wsgi app).

# Django

Django implements a simple web application - Question & Answer. 

Available functionality:
* Django user registration
* Django sessions, auth
* Django admin panel
* Django templates
* Paginator
* Model manager

URL:
* 



