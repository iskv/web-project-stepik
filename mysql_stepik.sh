sudo -H pip3 install mysqlclient
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask CHARACTER SET utf8;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED 'password'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate