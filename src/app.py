import sys
import requests

def main():
    print("hello world!")
    print(sys.prefix)
    print("good bye")

    response = requests.get('https://httpbin.org/ip')

    print('IP {0}'.format(response.json()['origin']))


print(__name__)

if __name__ == "__main__":
    main()

print(sys.path)