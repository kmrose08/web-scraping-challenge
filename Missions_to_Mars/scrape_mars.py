from bs4 import BeautifulSoup
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}

def scrape():
    browser = Browser('chrome', **executable_path, headless=False)
    title, paragraph = news(browser)
    mars = {
        'title':title,
        'paragraph': paragraph,
        'image': image(browser),
        'facts': facts(),
        'hems': hems(browser)
    }
    return mars

def news(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    news_title = soup.find('div',class_='content_title').text
    news_p=soup.find('div',class_='article_teaser_body').text
    return news_title, news_p

def image(browser):
    jpl_url='https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(jpl_url)
    browser.click_link_by_partial_text('FULL IMAGE')
    return browser.find_by_css('img.fancybox-image')['src']

def facts():
    facts_url = "https://space-facts.com/mars/"
    table = pd.read_html(facts_url)
    return table[0].to_html()

def hems(browser):
    hem_url = ('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    browser.visit(hem_url)
    links = browser.find_by_css('a.itemLink h3')
    hems = []
    for i in range(len(links)):
        hem = {}
        hem['title'] = browser.find_by_css('a.itemLink h3')[i].text
        browser.find_by_css('a.itemLink h3')[i].click()
        hem['url'] = browser.find_by_text('Sample')['href']
        browser.back()
        hems.append(hem)
    browser.quit()
    return hems



