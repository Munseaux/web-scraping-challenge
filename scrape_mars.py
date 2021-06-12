from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=True)

def newsScrape():
    url = "https://redplanetscience.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    news_title = soup.find('div', class_='content_title')
    news_p = soup.find('div', class_="article_teaser_body")
    return [news_title.text, news_p.text]

def imgageScrape():

    url="https://spaceimages-mars.com/image/featured/mars2.jpg"
    browser.visit(url)
    soup = BeautifulSoup(browser.html, 'html.parser')
    img_url = soup.find('img')['src']
    return img_url

def factsScrape():
    url = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(url)
    
    mars_prof_df = tables[1]
    
    return mars_prof_df.to_html(header=False, index=False)

def hemiScrape():
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"}
    ]
    return hemisphere_image_urls

def scrape():
    news_title , news_p = newsScrape()
    featured_img_url = imgageScrape()
    mars_facts = factsScrape()
    hemisphere_image_urls = hemiScrape()

    return {"news_title" : news_title, "news_p": news_p, "featured_img_url" : featured_img_url, "mars_facts" : mars_facts, "hemisphere_image_urls" :hemisphere_image_urls}

if __name__ == "__main__":
    factsScrape()
