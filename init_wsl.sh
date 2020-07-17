# Configuring nginx; change 'conf.d' to 'sites-enabled' and 'ivan' to 'box' for stepic
sudo ln -sf /home/ivan/web/etc/nginx_wsl.conf /etc/nginx/conf.d/test.conf
# Restart nginx
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
# Run gunicorn
cd ~/web
gunicorn -b 0.0.0.0:8080 hello:app
cd ~/web/ask
gunicorn ask.wsgi