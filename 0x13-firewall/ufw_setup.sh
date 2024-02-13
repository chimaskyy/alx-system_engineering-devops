#!/bin/bash

#update pacckage lists
sudo apt update

# Install UFW
sudo apt-get install ufw -y

# Allow incoming access to SSH, HTTP, and HTTPS
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Enable UFW
sudo ufw enable

# Display UFW status
sudo ufw status


