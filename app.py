from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests
import pymongo
from scrape_mars import scrape

app = Flask(__name__)

@app.route('/scrape')
def echo():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_info
    collection.insert_one(scrape())
    mars_stuff = list(db.mars_info.find())
    return str(mars_stuff[0])


@app.route("/")
def index():
    pass



if __name__ == '__main__':
    app.run(debug=True)
