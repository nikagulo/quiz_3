import requests
import json

r = requests.get('https://random.dog/woof.json?ref=apilist.fun')
if r.status_code != 200:
  print('faulty API')
else:
  print('your API is ready')
a = r.json()
print(a)
print(r.headers)
with open('dog.json', 'w') as f:
    json.dump(a, f)
print('Random dog video:\t' + a['url'])