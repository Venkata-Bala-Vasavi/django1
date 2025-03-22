import requests as req
url="https://dog.ceo/api/breeds/image/random"
ans=req.get(url)
if ans.status_code==200:
    dogbre=ans.json()
    print("Available breads: ",dogbre['message'])
else:
    print(f"Error in featching data.status code:{ans.status_code}")