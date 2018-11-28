from flask import Flask, render_template, url_for
import requests
from secrets import api_key
import json

def get_tech_headlines():
    params = {}
    base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    params["api-key"] = api_key
    resp = requests.get(base_url, params = params)
    resp_dict = json.loads(resp.text)
    return resp_dict

nyt_data = get_tech_headlines()

list_of_articles = []

for result in nyt_data['results'][0:5]:
    title = result['title']
    url = result['url']
    article = title + ' ({})'.format(url)
    list_of_articles.append(article)

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = '''
    <h1>Welcome!</h1>
    '''
    return html

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name = name, my_list = list_of_articles)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
