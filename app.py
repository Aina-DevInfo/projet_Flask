from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "RASOLOFOMANDIMBY Onitriniaina Jean hermana"

if __name__ == '__main__':
    app.run()
