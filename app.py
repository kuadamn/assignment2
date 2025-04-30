from flask import Flask, render_template
from scraper import fetch_wired_titles

app = Flask(__name__)

@app.route('/')
def home():
    headlines = fetch_wired_titles()
    return render_template('index.html', headlines=headlines)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
