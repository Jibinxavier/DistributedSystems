import requests
res = requests.post('http://localhost:8080/user/signup', json={"username":"lalala", "password":"hoowo"})
if res.ok:
    print( res.json())
else:
    print("error failed")

import requests
res = requests.post('http://localhost:8080/user/login', json={"username":"lalala", "password":"hoowo"})
if res.ok:
    print( res.json())
else:
    print("error failed")