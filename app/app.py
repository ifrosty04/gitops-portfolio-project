from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.environ.get('APP_VERSION', '2.0.0')
    hostname = socket.gethostname()
    return f"GitOps Pipeline Active!\nVersion: {version}\nPod: {hostname}\n"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)# force pipeline trigger
