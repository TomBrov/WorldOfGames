#! /bin/bash

chmod +x docker-compose.yml
chmod +x MainGame.py

docker-compose up -d
python3 ./MainGame.py
