# Configuring nginx
sudo ln -sf /home/box/web/etc/nginx_wsl.conf /etc/nginx/sites-enabled/test.conf
# Restart nginx
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
# Run gunicorn
cd ~/web/ask
gunicorn -b 0.0.0.0:8080 hello:app
gunicorn ask.wsgi