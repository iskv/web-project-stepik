sudo apt update
sudo apt install python3.5
sudo apt install python3.5-dev
sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3
sudo pip3 install --upgrade pip
sudo -H pip3 install --upgrade django==2.0
sudo -H pip3 install --upgrade gunicorn