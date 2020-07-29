sudo -H pip3 install mysqlclient
sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask CHARACTER SET utf8;"
mysql -uroot -e "CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ask.* TO 'box'@'localhost' WITH GRANT OPTION;"
# Django MySQL migrations
python3 ~/web/ask/manage.py makemigrations
python3 ~/web/ask/manage.py migrate