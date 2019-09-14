from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
mongo = client.mars_db

# Use flask_pymongo to set up mongo connection
# mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

mongo.mars_info.drop()

@app.route("/")
def index():
    info = mongo.db.mars_info.find_one()
    return render_template("index.html", info=info)


@app.route("/scrape")
def scrape():
    mars_info = mongo.db.mars_info
    mars_info_data = scrape_mars.scrape()
    mars_info.update({}, mars_info_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
