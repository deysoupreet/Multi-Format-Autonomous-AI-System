import redis
import json

r = redis.Redis()

def store(input_id, metadata):
    r.set(input_id, json.dumps(metadata))

def retrieve(input_id):
    return json.loads(r.get(input_id))
