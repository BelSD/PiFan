#! /bin/sh
# Installation de BelSD PiFan Control

set -e

#cd "$(dirname "$0")/.."

sudo apt-get -y update
sudo apt-get install python3-gpiozero -y

echo "=> Installation de BelSD PiFan Controller...\n"
sudo cp BelSD_PiFan.py /usr/local/bin/
sudo chmod +x /usr/local/bin/BelSD_PiFan.py

echo "=> Démarrage de BelSD PiFan Controller...\n"
sudo cp BelSD_PiFan.sh /etc/init.d/
sudo chmod +x /etc/init.d/BelSD_PiFan.sh

sudo update-rc.d BelSD_PiFan.sh defaults
sudo /etc/init.d/BelSD_PiFan.sh start

echo "BelSD PiFan controller installé."