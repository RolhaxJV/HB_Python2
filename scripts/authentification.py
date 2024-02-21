import requests
from project.settings import DOMAIN, PORT, API_KEY
import os

headers = {'Authorization': API_KEY}

data = requests.get(os.path.join(f"{DOMAIN}:{PORT}", 'api/List/?table=Club'), headers=headers)
data = data.json()

### Retituer le résultat..
print(data)
