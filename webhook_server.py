from flask import Flask, request
from bot import application

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json(force=True)
    application.update_queue.put_nowait(update)
    return "ok", 200