sudo ln -sf /home/skvich/web/etc/nginx-test.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx stop
sudo /etc/init.d/nginx start
