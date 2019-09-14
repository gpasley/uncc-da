def scrape():
  from bs4 import BeautifulSoup
  from splinter import Browser
  import requests
  import pandas as pd

  # URL of page to be scraped
  url = 'https://mars.nasa.gov/news/'
  image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
  twitter_url = 'https://twitter.com/MarsWxReport'
  facts_url = 'https://space-facts.com/mars/'
  hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
  executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
  browser = Browser('chrome', **executable_path, headless=False)

  # Retrieve page with the requests module
  response = requests.get(url)

  # Create BeautifulSoup object; parse with 'html.parser'
  soup = BeautifulSoup(response.text, 'lxml')

  results = soup.find_all('div', class_='image_and_description_container')
  results[0]
  titles = soup.find_all('div', class_='content_title')
  pgs = soup.find_all('div', class_='rollover_description_inner')
  news_title = titles[0].text
  news_p = pgs[0].text

  #get featured image
  browser.visit(image_url)
  # HTML object
  html = browser.html
  # Parse HTML with Beautiful Soup
  soup = BeautifulSoup(html, 'html.parser')
  # Retrieve all elements that contain book information
  sections = soup.find_all('section', class_='primary_media_feature')
  a = sections[0].find('article')
  jpg = a['style'].split('\'')[1]
  featured_image_url = "https://www.jpl.nasa.gov" + jpg

  #get twitter
  browser.visit(twitter_url)
  # HTML object
  html = browser.html
  # Parse HTML with Beautiful Soup
  soup = BeautifulSoup(html, 'html.parser')
  # Retrieve all elements that contain book information
  items = soup.find_all('li', class_='js-stream-item')
  a = items[0]
  mars_weather = a.find('p', class_='tweet-text').text

  # get Mars facts
  tables = pd.read_html(facts_url)
  facts_table = tables[0].to_html()

  hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
  ]

  info = {
    "news_title": news_title,
    "news_p": news_p ,
    "featured_image_url": featured_image_url,
    "mars_weather": mars_weather,
    "facts_table": facts_table,
    "hemisphere_image_urls": hemisphere_image_urls
  }
  return info