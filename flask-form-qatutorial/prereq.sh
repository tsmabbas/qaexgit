#!/bin/bash
mkdir templates
touch app.py templates/{layout,ben,harry}.html
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv venvform
source venvform/bin/activate