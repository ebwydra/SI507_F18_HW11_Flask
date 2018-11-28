from flask import Flask, render_template, url_for
import requests
from secrets import api_key
import json

def get_section_headlines(section):
    params = {}
    base_url = "https://api.nytimes.com/svc/topstories/v2/{}.json".format(section)
    params["api-key"] = api_key
    resp = requests.get(base_url, params = params)
    resp_dict = json.loads(resp.text)
    return resp_dict

def get_tech_headlines():
    params = {}
    base_url = "https://api.nytimes.com/svc/topstories/v2/technology.json"
    params["api-key"] = api_key
    resp = requests.get(base_url, params = params)
    resp_dict = json.loads(resp.text)
    return resp_dict

app = Flask(__name__)

@app.route('/')
def hello_world():
    html = '''
    <h1>Welcome!</h1>
    '''
    return html

@app.route('/user/<name>')
def user(name):

    section = "technology"
    nyt_data = get_section_headlines(section)

    list_of_articles = []

    for result in nyt_data['results'][0:5]:
        title = result['title']
        url = result['url']
        article = title + ' ({})'.format(url)
        list_of_articles.append(article)

    section_list = ["home", "opinion", "world", "national", "politics", "upshot", "nyregion", "business", "technology", "science", "health", "sports", "arts", "books", "movies", "theater", "sundayreview", "fashion", "tmagazine", "food", "travel", "magazine", "realestate", "automobiles", "obituaries", "insider"]

    return render_template('user.html', name = name, section = section, my_list = list_of_articles, list_of_sections = section_list)

@app.route('/user/<name>/<section>')
def section(name, section):
    list_of_articles2 = []
    section_data = get_section_headlines(section)
    for result in section_data['results'][0:5]:
        title = result['title']
        url = result['url']
        article = title + ' ({})'.format(url)
        list_of_articles2.append(article)
    section_list = ["home", "opinion", "world", "national", "politics", "upshot", "nyregion", "business", "technology", "science", "health", "sports", "arts", "books", "movies", "theater", "sundayreview", "fashion", "tmagazine", "food", "travel", "magazine", "realestate", "automobiles", "obituaries", "insider"]
    return render_template('user.html', name = name, section = section, my_list = list_of_articles2, list_of_sections = section_list)

if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
