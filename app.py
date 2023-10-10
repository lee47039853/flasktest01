from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Replica Set 연결 정보
#mongo_uri = "mongodb+srv://lee47039853:NmqMAKDtGbSXI1Gb@mogodbtutorial.5ltgk8u.mongodb.net/"
mongo_uri = "mongodb+srv://lee47039853:NmqMAKDtGbSXI1Gb@mogodbtutorial.5ltgk8u.mongodb.net/"
client = MongoClient(mongo_uri)

# Replica Set에서 데이터베이스 및 컬렉션 설정
database = client["blog"]
collection = database["users"]

@app.route('/')
def index():
    # MongoDB에서 데이터 가져오기
    query = {}
    cursor = collection.find(query)
    users = [doc for doc in cursor]

    return render_template('index.html', users=users)

