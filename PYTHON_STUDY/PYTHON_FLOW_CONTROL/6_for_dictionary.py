person = {'name':'Hebu', 'address': 'Seoul', 'interest': 'vrchat'}
print(person['name'])

for key in person:
    print(key, person[key])

persons = [
    {'name':'Hebu', 'address': 'Seoul', 'interest': 'vrchat'},
    {'name':'Heaven', 'address': 'nowhere', 'interest': 'dream'},
    {'name':'HeaveKK', 'address': 'tokyo', 'interest': 'artist'}
]


for person in persons:
    for key in person:
        print(key, ':', person[key])
    print('-------------')