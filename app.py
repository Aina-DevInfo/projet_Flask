from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Solofo Ny Aina, André sy Faneva randrianatenaina"

if __name__ == '__main__':
    app.run()
