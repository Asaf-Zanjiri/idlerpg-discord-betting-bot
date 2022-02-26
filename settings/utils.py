import json

with open('./settings/config.json', 'r') as f:
    config = json.loads(f.read())
    token = config['token']
    prefix = config['prefix']