import logging
from flask import Flask, render_template, request
from datetime import datetime, timedelta
from aiogram.utils.exceptions import ChatNotFound
from aiogram import Dispatcher
from web_app import safe_parse_webapp_init_data
from config import dp, BOT_TOKEN

SEND_MESSAGE_DELTA = {}


# /web-start
async def web_start():
    return render_template('start.html')


# /checkUserData
async def web_check_user_data(data: dict):
    data = safe_parse_webapp_init_data(token=BOT_TOKEN, init_data=data["_auth"])
    return dict(ok=True, user=data.as_json())


# /sendMessage
async def web_send_message(data: dict, dispatcher: Dispatcher):
    try:
        web_app_data = safe_parse_webapp_init_data(token=BOT_TOKEN, init_data=data["_auth"])
    except ValueError:
        return dict(ok=False, error="Unauthorized", status=401)

    web_app_user_id = web_app_data["user"]["id"]

    if web_app_user_id not in SEND_MESSAGE_DELTA:
        SEND_MESSAGE_DELTA.update({web_app_user_id: datetime.utcnow() - timedelta(seconds=100)})

    delta = SEND_MESSAGE_DELTA.get(web_app_user_id)

    if (datetime.utcnow() - delta) < timedelta(seconds=5):
        return dict(ok=False, error="🥶 You are to fast. Please wait for 5 seconds")

    user_id = data.get("user_id")
    text = data.get("text")

    if (not user_id) or (not text):
        return dict(ok=False, error="💁‍♂ UserID and Text inputs required")

    try:
        SEND_MESSAGE_DELTA.update({web_app_user_id: datetime.utcnow()})
        await dispatcher.bot.send_message(chat_id=user_id, text=text)
    except ChatNotFound:
        return dict(ok=False, error="Chat not found")
    except Exception as exc:
        logging.error(exc)
        return dict(ok=False, error="Exception caused")
    else:
        return dict(ok=True)


app = Flask(__name__, template_folder="templates")


@app.get("/web-start")
async def app_web_start():
    return await web_start()


@app.post("/sendMessage")
async def app_send_message():
    return await web_send_message(request.form, dp)


@app.post("/checkUserData")
async def app_check_user_data():
    return await web_check_user_data(request.form)
