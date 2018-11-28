from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
