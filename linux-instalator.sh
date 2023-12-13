#!/bin/bash

# Instalacja Pythona
sudo apt-get update
sudo apt-get install -y python3

# Instalacja potrzebnych bibliotek
sudo apt-get install -y python3-tk
sudo apt-get install -y python3-pil
sudo apt-get install -y python3-pil.imagetk
sudo apt-get install -y python3-pip

# Instalacja dodatkowych bibliotek przy użyciu pip
pip3 install configparser

echo "Instalacja zakończona"
