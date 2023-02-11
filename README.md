# Telegram Web Bot
This is simple stack of telegram web app bot: _Nginx, Docker, Gunicorn, Aiogram, Flask, Certbot_.

💡 Notion: This project is asynchronous, and for further integration of any modules, you must take this into account.
This uses the asynchronous successor to WSGI - asgiref for Flask and Aiogram - asynchronous framework for Telegram Bot API.
### Steps

1) `git clone https://github.com/roomdie/telegram-web-bot` clone to your project
2) Get your https domain then generate SSL certificates. I recommend to use **certbot** for this.
By default certbot generate certificates to _/etc/letsencrypt/live/your_domain/_  You need paste your domain to services/nginx/**nginx.conf**, **.env** and **docker-compose.yml** 
    More here https://certbot.eff.org/instructions
3) Setup .env file
4) Generate **dhparam.pem** file for _services/nginx/**security.conf**_ by this command `openssl dhparam -out /etc/ssl/certs/dhparam.pem 4096`
The **dhparam.pem** file used for increase the security of SSL/TLS connections. It may take time to generate from a few seconds to minutes depending on your hardware, my generation time on server x1 3.3GHz CPU, 1GB RAM is 8 minutes on average. This file needs to be generated once, then you just copy it to the container. 
If you have a very long generation, you can reduce the number to 2048 bits for modern security, but 4096 bits or higher is recommended or disabled this, but then you need change services/nginx/**nginx.conf** and **Dockerfile**.
5) `docker compose build`
6) `docker compose up -d`

When writing this project, I partially used this repository https://github.com/andrew000/Telegram-WebApp-Bot

