# Configuring nginx
sudo ln -sf /home/ivan/web/etc/nginx_wsl.conf /etc/nginx/conf.d/test.conf
# Restart nginx
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
# Run gunicorn
cd ~/web
gunicorn -c /home/ivan/web/etc/hello_wsl.conf.py hello:app
cd ~/web/ask
gunicorn -c /home/ivan/web/etc/ask_wsl.conf.py ask.wsgi