import os

from flask import Flask, session
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
DATABASE_URL="postgres://iqjjflfpbmahqg:df0d1b84013577dbdba1a2e28aad4cf91b55bb1ff8eabc876f2266c0e3a4dcc3@ec2-54-221-201-212.compute-1.amazonaws.com:5432/d924rojmpjo7o9postgres://iqjjflfpbmahqg:df0d1b84013577dbdba1a2e28aad4cf91b55bb1ff8eabc876f2266c0e3a4dcc3@ec2-54-221-201-212.compute-1.amazonaws.com:5432/d924rojmpjo7o9"
# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return "Project 1: TODO"
