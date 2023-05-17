'''
작성일: 2023년 5월 17일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 6장 시퀀스 자료형
       02. 시퀀스 자료형의 연상
'''

# 1. 인덱싱 - 순차적인 자료구조에 인덱스 값을 가지고 접근
name = '도스톤벡'
# name 에 저장된 0번지 값 출력
print ("name[0] - 인덱싱 결과 : ", name[0])

# 리스트 저장 변수
city = ['부산시', 100, '부산시', 200]
#리스트에서 뒤에서 2번째 내용 출력
print("city[-2] - 인덱싱 결과 : ", city[-2])

#뒤에서 4번째 내용을 '서울시'로 변경하여 city에 저장
city[-4] = '서울시'
print("city - 인덱싱 결과(서울시로 변경) : ", city)

# 5개의 정수를 튜플로 생선
num = (1,2,3,4,5)   # 인텍스는 0번지-4번지
#print("num[5] : ", num[5]) #튜플의 크기를 벗어나 오류 발생


# 2. 슬라이싱 - 인덱스를 사용하여 자료형의 특정 부분을 지정
givename = name(1:3) # 1번지부터 3번지 앞까지 추출.
print("name[1:3] - 슬라이싱 결과 : ",givename)

print("city[0:] - 슬라이싱 결과 :, city[0:]")
# city 2번지부터 킅까지 추출
print("city[2:] - 슬라이싱 결과 : ", city[2:])
# num 변수의 처음부터 끝까지 2씩 증가하면서 추출
print("num[::2] - 슬라이싱 결과 :, num[::2]") 
# 범위를 벗어나면 출력 가능한 내용 모두 출력
print("num[-10:2] - 슬라이싱 결과 :, num[-10:2]") 

# 3. 연결 - '+' 연상자를 사용하여 두 개의 자료를 연결하여 
#    새로운 시퀀스 자료형을 만들다
# 튜플 생선 
num1 = (1,2,3,4,5)
num2 = (6,7,8,9,)
result = num1 + num2    #더하기가 아닌 연결
print("연결 결과(result) : ", result)

# 리스트 생선
city = ['서울시', '제주도', '부산시']
result = num1 + city #숫자와 문자는 연결되지 않는다
# 오류 발생 : 서로 다른 자료형은 합칠 수 없다.
#print("연결 결과(result) :", result)

text1 = 'I like'
text2 = text1 + 'Python'  # 문자열 자료형 연결
print("연결 결과(text2) : ", text2)

# 4. 반복 - '*' 연산자를 사용하여 원하는 만큼 반복
# 튜플 생선
language = ('Python', 'Java', 'C')
print("language 튜플 내용 3번 반복 : ", language * 3)
# Python 문자를 10번 반복하여 출력
print("Python 10번 반복 : ", 'Python ' 8 10)

# 5. 멘버 유무 검사  - True, False 로 출력
# 시퀀지 자료형의 특정 자료가 있는지 알려 주는 기능 - in 연산자 
# 리스트 생선 
color = ['red', 'blue', 'green', 'white']
print("coloe에 black이 있나요? ", 'black' in color)
language = 'Python'
print("language에 'p'이 있나요? ", 'p' in color)
print("language에 't'이 있나요? ", 't' in color)

# 6. 길의 정보 - len() 함수
print("color : ", color)
print("color 의 길이는? ", len(color))
print("text2 : ", text2)
print("text2 의 길이는?", len(text2))

