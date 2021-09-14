from flask import Flask
from flask.templating import render_template
import movie_api as mapi
import temp
app = Flask(__name__)

@app.route("/")
def index():
    movieapi=mapi.callMovieApi()
    return render_template("index.html", movies=mapi.convert_model(movieapi)) 

if __name__ == "__main__":
    app.run(debug=True)