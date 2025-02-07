from flask import Flask, render_template
import random

app = Flask(__name__)

images = [

    "https://images.app.goo.gl/hYaMr6duS4SxKTX46",
    "https://images.app.goo.gl/93eSRJZ9tHC6kosp6",
    "https://images.app.goo.gl/HfiRGavhtsM5NBif6",
    "https://images.app.goo.gl/iFobbytq4iRAU9La8"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")