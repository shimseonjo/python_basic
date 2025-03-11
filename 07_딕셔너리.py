name_card = {'name':'홍길동',
             'tel':'010-888-9999',
             'address':'부산',
             'email':'hong@gmail.com'}

print(name_card)

name_card['etc'] =['이사갈수도 있음....','1년안에']

print(name_card)

print(name_card['address'])

print(name_card['etc'][1])

del name_card['address']

print(name_card)

print(type(name_card))

print(len(name_card))

# print(name_card['address'])

print('address' in name_card )

print(name_card.keys())
print(name_card.values())
print(name_card.items())

for k in name_card.keys():
  print(k)
print('-----')

for k in name_card.values():
  print(k)
print('-----')

for k in name_card.items():
  print(k)

print('-----')

for k,v in name_card.items():
  print(k,v)

name_card.clear()
print(name_card)

# print(name_card['address'])
print(name_card.get('address'))


s1 = set([1,2,3,3,2])
print(s1)

s2 = set('hello')
print(s2)