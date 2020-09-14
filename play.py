import requests

resp = requests.get("http://api.icndb.com/jokes/random")
print resp.text
