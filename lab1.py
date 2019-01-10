import requests



print (requests.__version__)
a= requests.get('http://www.google.com')
print (a.text)
b= requests.get('https://raw.githubusercontent.com/hyusuf4/lab1/master/lab1.py')
print(b.text)











