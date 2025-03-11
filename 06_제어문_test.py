## 명함관리 프로그램 작성
# 1.명함입력, 2.명함수정, 3.명함삭제, 4.명함목록보기, 5.종료

import sys

display = '''
-------------------------------------------------------------
1.명함입력, 2.명함수정, 3.명함삭제, 4.명함목록보기, 5.종료
-------------------------------------------------------------
메뉴를 선택하세요 >>> '''

card_list=[['홍길동', '111-222-3333', '부산', 'hong@gmail.com'], ['박나리', '22-4444-7777', '서울', 'park@gmail.com']]
menu = ''
while True:
  menu = input(display)
  if menu == '1':
    print('명함입력')
    name = input('이름 >>> ')
    tel = input('전화번호 >>> ')
    address = input('주소 >>> ')
    while True:
      email = input('이메일 >>> ')
      check = 0
      for index in range(len(card_list)):
    # for index,card in enumerate(card_list):
        if card_list[index][3] == email:
          check = 1
          break
      if check == 0:
        break
    card_list.append([name,tel,address,email])
    print(card_list)
  elif menu == '2':
    print('명함수정')
    email = input('수정할 데이터의 이메일을 입력 >>> ')
    check = 0
    for index in range(len(card_list)):
      if card_list[index][3] == email:
        check = 1
        while True:
          item = input('수정할 항목을 선택하세요(1.이름, 2.전화번호, 3.주소,  4.종료)')
          if item == '4':
            break
          item = int(item)
          if item in (1,2,3):         
            card_list[index][item-1] = input('수정할 값을 입력 >>> ')

    if check == 0:
      print('데이터가 없습니다.')    
  elif menu == '3':
    print('명함삭제')
    email = input('삭제할 데이터의 이메일을 입력 >>> ')
    check = 0
    for index in range(len(card_list)):
      if card_list[index][3] == email:
        check = 1
        print('삭제 >>> ', card_list.pop(index))
        break
    if check == 0:
      print('데이터가 없습니다.')
  elif menu == '4':
    print('명함목록보기')
    print('=' * 55)
    for card in card_list:
      print(f'{card[0]:10} {card[1]:15} {card[2]:10} {card[3]:10}')
    print('=' * 55)
  elif menu =='5':
    print('프로그램 종료')
    sys.exit()
  else:
    print('메뉴선택을 잘못하셨습니다.')
