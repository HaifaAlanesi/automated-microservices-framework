from flask import Flask, request
import redis
import os

app = Flask(__name__)

# This connects to the Redis service inside Kubernetes
r = redis.Redis(host='redis-service', port=6379, decode_responses=True)

@app.route('/')
def index():
    votes = r.get('total_votes') or 0
    return f"<h1>Vote for DevOps!</h1><p>Total Votes: {votes}</p><form action='/vote' method='POST'><button type='submit'>Vote Now</button></form>"

@app.route('/vote', methods=['POST'])
def vote():
    r.incr('total_votes')
    return "Vote Recorded! <a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
