'''
작성일: 2023년 5월 17일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 6장 시퀀스 자료형
       02. 시퀀스 자료형의 연상
'''
# 문자열 생선
name = '도스톤벡'
name2 = '''도
스
톤 
벡'''
print("name : ", name)
print("name2 : ", name2)

# 빈 문자열 생선
text1 = ''
print("text1의 길이 : ", len(text1))
text2 = str()
print("text2의 길이 : ", len(text2)) 

#정수를 문자열로 생선
text3 = str(1234)
print("twxt3 : ", text3)
print("text3의 자료형 : ", type(text3))

# 리스트를 문자열로 생선.
text4 = str[1,2,3]
print("text4의 자료형 : ", type(text4))
# 레스트 자제를 문자열로 인식하여 '[' 출력됨.



# 2. 문자열 메소드
# 대소문자 변환
text1 = 'i like python'
print("text1 내용의 첫 문자를 대문자로 변환 :", text1.capitalize())
print("text1 내용의 모든 단어를 첫 문자를 대문자로 변환 :", text1.capitalize())
text2 = text1.upper() # 대문자 변환
print("text1 내용의 모든 문자를 대문자로 변환 :", text2)
text3 = text2.lower() #소문자 변환
print("text2 내용의 첫 문자를 소문자로 변환 :", text3)


# 문자열 정렬
print(text3.center(30, '*'))

# 문자 찾기
print("text3에 'a'가 몇 개 있나요?", text3.count('a'))
print("text3에 'i'가 몇 개 있나요?", text3.count('i'))
print("text3의 인덱스 5부터 10까지 중에서 'i'가 몇 개 있나요?"text3.count('i'))
print("text3의 인덱스 5이후에 '0'가 몇 개 있나요?"text3.count('0'))

# 문자열 내의 위치 - index(), fine(), atarswitch(), enaswutch()
print("text3에 'k'의 인덱스 위치는?", text3.index('k'))
print("text3에 'k'의 인덱스 위치는?", text3.index('k'))


print("text3에 'python'의 인덱스 위치는?", text3.index('python'))
print("text3에 'python'의 인덱스 위치는?", text3.index('python'))

#없으면 오류
#print("text3에 'python1'의 인텍스 위치는?", text.find('python'))

#print("text3가 'i like'로 시작하는가?", text.startwitch('i'))
#print("text3에 'abc'끝나는가?", text.andwitch('i'))


# 딕셔너리 생선 
dict1 = {'apple':'사과', 'grape':'포도', 'peach':'봉숭아'}
#키(key)에 해당하는 문자열에 조인
print("dict1 내용에 '-'를 결합 : ", '-'.join(dict1))

# 문자열 분리 - split()
text1 = "Ilike python programming language"
#문자열을 스페이스로 분리하여 리스트로 반환
list = text1.split()
print("text1 ")