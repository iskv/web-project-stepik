# Configuring nginx
sudo ln -sf /home/box/web/etc/nginx_stepik.conf /etc/nginx/sites-enabled/test.conf
# Restart nginx
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
# Run gunicorn
cd ~/web
gunicorn -b 0.0.0.0:8080 --access-logfile acc_8080.log hello:app --daemon
cd ~/web/ask
gunicorn -b 0.0.0.0:8000 --access-logfile acc_8000.log ask.wsgi --daemon