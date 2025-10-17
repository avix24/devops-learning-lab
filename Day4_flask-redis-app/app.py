from flask import Flask
import redis
import os


app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST','redis')
r = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/')
def hello():
	r.incr('hits')
	return f"This page has been visited {r.get('hits').decode('utf-8')} times."
	
if __name__ == "__main__":
	app.run(host="0.0.0.0",port=5000)