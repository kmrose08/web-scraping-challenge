from bs4 import BeautifulSoup
import requests
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

# ## Featured image

# In[32]:


jpl_url='https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(jpl_url)
    
# HTML object
jpl_html = browser.html

# Parse HTML with Beautiful Soup
jpl_soup = BeautifulSoup(html, 'html.parser')


# In[ ]:


# # pull images from website
# base_url = soup.find_all('a', class_="showing fancybox-thumbs")
# print(image_url)


# In[35]:


# featured_image_url = 'https://www.jpl.nasa.gov' + base_url
# print(featured_image_url)


# ## Mars Facts

# In[44]:


facts_url = "https://space-facts.com/mars/"
table = pd.read_html(facts_url)
table[0]


# ## Mars hemispheres

# In[46]:


hem_url = ('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')


# In[ ]:


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# In[48]:


# Cerberus
# https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif

# Schiaparelli 
# https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif 
    
# Syrtis Major
# https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif
    
# Valles Marineris
# https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif
    
    


# In[ ]:


# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]


# In[ ]:





# In[ ]:





# In[ ]:




