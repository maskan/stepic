#!/usr/bin/env bash
sudo pip3 install virtualenvwrapper
mkdir ~/.virtualenvs
echo ' export WORKON_HOME=~/.virtualenvs' >> ~/.bashrc
echo ' export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'' >> ~/.bashrc # This needs to be placed before the virtualenvwrapper command
echo ' source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
source ~/.bashrc
