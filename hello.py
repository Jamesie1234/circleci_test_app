from flask import Flask, jsonify
import time
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from minikube cluster!!!"
    #return jsonify({"Time of Call": time.time()})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)