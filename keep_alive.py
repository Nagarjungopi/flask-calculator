from flask import Flask
from threading import Thread

app = Flask("")


def run():
    app.run(host="18.118.130.176", port=3000)


def keep_alive():
    t = Thread(target=run)
    t.start()
