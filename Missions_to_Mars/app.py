from flask_pymongo import PyMongo
from flask import Flask, render_template, redirect
from scrape_mars import scrape

app = Flask(__name__)

mongo = PyMongo(app, uri='mongodb://localhost:27017/mars_db')

@app.route('/')
def home():
    mars = mongo.db.mars.find_one()
    return render_template('index.html',mars=mars)

@app.route('/scrape')
def scrape_mars():
    mars = mongo.db.mars
    data = scrape()
    mars.update({},data,upsert=True)
    return redirect('/',code=302)

if __name__ == '__main__':
    app.run(debug=True)
