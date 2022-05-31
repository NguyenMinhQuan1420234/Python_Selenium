import requests

url = 'https://httpbin.org/post'

files = {'file': open('USCarBrands.csv', 'rb')}

r = request.post(url, files= files)

print(r.status_code)
print(r.text)