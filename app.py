from flask import Flask, render_template
from flask_socketio import SocketIO
from cowsay_generator import generate_cowsay
import os

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')  # ważne, aby eventlet

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('message')
def handle_message(data):
    name = data.get("name", "Anonim")
    message = data.get("message", "")
    color = data.get("color", "black")
    cow_msg = generate_cowsay(name, message, color)
    socketio.send(cow_msg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port)
