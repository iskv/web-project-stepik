# Configuring nginx
sudo ln -sf /home/box/web/etc/nginx_wsl.conf /etc/nginx/sites-enabled/test.conf
# Restart nginx
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
# Run gunicorn
cd ~/web/ask
gunicorn ask.wsgi