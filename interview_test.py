import requests
import json

apiEndpoint = 'http://interview-black-box:5000'

print('Print the rules and help text')
recieve = requests.get(url=apiEndpoint)
print(recieve.text)

print('-----------------------------------------------')
print('Starting interview test Python program')

print('Start the initial query to generate sequence')
recieve = requests.get(url=f"{apiEndpoint}/start")
print(recieve.text)

print('Parse the query data')
data = json.loads(recieve.text)

print('Setup the variables')
L = data['sequenceLength']
a_n = data['first']
a_n_plus_1 = data['second']

print('Generate numbers in a sequence of the requested length')
for i in range(L):

    if i % 3 == 0:
        a_n_plus_2 = 0
    elif i % 3 == 1:
        a_n_plus_2 = 0
    else:
        a_n_plus_2 = 0

    # Update numbers next in sequence
    print(i, a_n, a_n_plus_1, a_n_plus_2)
    a_n = a_n_plus_1
    a_n_plus_1 = a_n_plus_2

print('Submit the solution')
postData = {
    "id": data['id'],
    "solution": a_n_plus_2
}
print(postData)

print('Get the submission status')
recieve = requests.post(
    url=f"{apiEndpoint}/solution",
    data=json.dumps(postData)
)
print(str(recieve.text))
