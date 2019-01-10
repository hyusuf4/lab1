import requests



print (requests.__version__)
a= requests.get('http://www.google.com')
print (a.text)













