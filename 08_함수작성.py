a1 = 0
def add(a,b):
  print(a1)
  return a + b
add(1,2)

def sub(a,b):
  print('결과는 ',a-b)
  # return a - b

def mul(a,b):
  return a * b

def indata():
  a = int(input('숫자를 입력하세요 >> '))
  return a

# result = add(1,3)
# print(result)

# data1 = indata()
# data2 = indata()
# sub(data1,data2)

def add_many(*args,mode='k'):
  print(type(args))
  result = 0
  for i in args:
    # print(i)
    result += i
  return result

print(add_many(1,2,3,4,5,6,7,8,9))
print(add_many(1,2,3,4,5,6,7,mode='yy'))

def item_print(**items):
  print(type(items))
  print(items)

item_print(a='hong',b=22)