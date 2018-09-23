import sys
import requests

print("hello world!")
print(sys.prefix)
print("good bye")

response = requests.get('https://httpbin.org/ip')

print('IP {0}'.format(response.json()['origin']))