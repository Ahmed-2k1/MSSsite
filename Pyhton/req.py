import requests

# r = requests.get('https://xkcd.com/353/')

# print(r.text)

# use dir command to get the attruibutes and methods that we can access within this object.
# use help command to get the detiled explanation about the objects.
# use .text method to get the contents of website in unicode.
# to get the image we can use .content to get the data in bytes.

# r = requests.get(' https://imgs.xkcd.com/comics/python.png')

# print(r.content)

# in order to view the image what we can do is take those bytes and save it on our machines.

# with open('comic.png', 'wb') as f:
#     f.write(r.content)

# how to check the status - 

# print(r.status_code) 

# using requests to pass some paramerters with URL :
# we can directly append the parameters at the end of the URL but doing like this can cause errors hence we pass these parameters as dictionery.
# payload = {'page': 2, 'count':25}
# r = requests.get('https://httpbin.org/get', params = payload)

# print(r.text)
# we use this when we want to post the form data to a rout 
# to check if the URL generated is correct ot not 
# print(r.url)

# POSTING THE DATA TO THE URL: (Eg: posting form)

payload = {'username': 'yasar', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload)

print(r.json())

# it has created a dict for the form in output 
# inorder to view that:

R  = r.json()
print(R['form'])

# r = requests.get('http://httpbin.org/basic-auth/yasar/testing',)

# print(r)

# r = requests.get('http://httpbin.org/delay/6', timeout=3)

# print(r)








