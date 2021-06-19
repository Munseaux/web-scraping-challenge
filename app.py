from flask import Flask, render_template, redirect
from bs4 import BeautifulSoup
import requests
import pymongo
from scrape_mars import scrape

app = Flask(__name__)

@app.route('/scrape')
def echo():
    redirect("/scrape")
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_info
    collection.drop()
    collection.insert_one(scrape())
    
    return redirect("/", code=302)


@app.route("/")
def index():
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    db = client.mars_db
    collection = db.mars_info
    listings = collection.find_one()
    img_urls = listings['hemisphere_image_urls']
    return render_template('index.html', listings=listings, img=img_urls)
    



if __name__ == '__main__':
    app.run(debug=True)
