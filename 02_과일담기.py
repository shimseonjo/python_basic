# 과일을 받아서 박스에 담고 싶습니다.
# 박스에 담겨지는 과일은 갯수는 과일마다 다릅니다.
# 과일의 갯수를 받고, 박스에 몇개 담겨지는도 입력을 받고
# 박스에 담아서 몇박스 몇개인지 알려주는 프로그램을 작성
# 변수 : 과일의 갯수, 박스당 몇개 담겨지는지
# 값을 입력 받아야 됨 : input()
# 값 데이타 타입이 문자열 -> 숫자 변환하는 먼가가 필요할듯 int() float()
# 결과값을 화면에 알려줘야함 : print()

count = input('과일의 갯수를 입력하세요 >>> ')
count = int(count)
print('입력받은 값의 데이터 타입은 ->',type(count))
box_count = int(input("박스당 몇개 담을껀가요?? >> "))
print(type(box_count))
print(count // box_count, "박스", count % box_count, "개")