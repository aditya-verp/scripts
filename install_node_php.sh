#!/bin/bash
#Read the versions from user and stored to a variable
read -p "Enter node version: " node_ver
read -p "Enter php version: " php_ver

sudo apt-get update -y
echo "##############Installing Node ...#####################"
# Download and Install NVM
sudo curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.0/install.sh | bash

#Load the nvm to system
export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

nvm install $node_ver
nvm alias default $node_ver
echo "############### Node $node_ver successfully Installed ###############"

# Install PHP
echo "############## Installing php ...##############"
sudo apt install software-properties-common -y
sudo apt install php$php_ver -y
echo "PHP $php_ver installed successfully!"
