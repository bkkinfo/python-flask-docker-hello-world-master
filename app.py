from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "I Am Bishnu Kashyap, This is Hackathon No.:3 -> Flask inside Docker!!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6000))
    app.run(debug=True,host='0.0.0.0',port=port)
