# Telegram Web Bot
[![MIT License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](https://opensource.org/licenses/MIT)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-6.4-blue.svg?style=flat-square&logo=telegram)](https://core.telegram.org/bots/api)
[![Docker](https://img.shields.io/badge/Docker-3.8-blue?style=flat-square&logo=docker)](https://www.docker.com/)
[![Supported python versions](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Nginx](https://img.shields.io/badge/Nginx-1.22.1-brightgreen?style=flat-square&logo=nginx)](https://nginx.org/en/download.html)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-20.1.0-brightgreen?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![Flask](https://img.shields.io/badge/Flask-2.2.2-ff69b4?style=flat-square&logo=flask)](https://flask.palletsprojects.com/en/2.2.x/)
[![Certbot](https://img.shields.io/badge/Certbot-2.2.0-orange?style=flat-square&logo=letsencrypt)](https://certbot.eff.org/)
[![Aiogram](https://img.shields.io/badge/Aiogram-2.20-blue?style=flat-square)](https://docs.aiogram.dev/en/latest/)

💡 Notion: This project is asynchronous, and for further integration of any modules, you must take this into account.
This uses the asynchronous successor to WSGI - asgiref for Flask and Aiogram - asynchronous framework for Telegram Bot API.
### Steps


1) `git clone https://github.com/roomdie/telegram-web-bot` clone to your project
2) Get your https domain then generate SSL certificates. I recommend to use **certbot** for this.
By default certbot generate certificates to _/etc/letsencrypt/live/your_domain/_  You need paste your domain to services/nginx/**nginx.conf**, **.env** and **docker-compose.yml** 
    More here https://certbot.eff.org/instructions
3) Rename .env-template file to .env `mv .env-template .env` and set variables
4) Generate **dhparam.pem** file for _services/nginx/**security.conf**_ by this command `openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096`
The **dhparam.pem** file used for increase the security of SSL/TLS connections. It may take time to generate from a few seconds to minutes depending on your hardware, my generation time on server x1 3.3GHz CPU, 1GB RAM is 8 minutes on average. This file needs to be generated once, then you just copy it to the container. 
If you have a very long generation, you can reduce the number to 2048 bits for modern security, but 4096 bits or higher is recommended or disabled this, but then you need change services/nginx/**nginx.conf** and **Dockerfile**.
5) `docker compose build`
6) `docker compose up -d`

When writing this project, I partially used this repository https://github.com/andrew000/Telegram-WebApp-Bot

