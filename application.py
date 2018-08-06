from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker


app = Flask(__name__)


engine = create_engine("postgresql://journal:journal@localhost/journal")
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
	return render_template("index.html")
