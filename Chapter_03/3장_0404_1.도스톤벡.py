















# 국어 점수와 수학 점수를 입력 받으시오.

#score, score2   /  kor, math   
kor = input('국어 점수를 입력 하시오 : ')
math = input('국어 점수를 입력 하시오 : ')

# 두 과목 점수의 한계를 계산하시오.
# 국어와 수학 점수를 합하여 변수에 저장.
total = kor +  math

#합계 출력
print('두 과목 점수의 합계는 ', total, '점 입니다')
print("두 과목 점수의 합계는  {}점 입니다" .format(total))


# 정수를 입력 받기 위해서는 반드시 int() 함수를 사용해야 한다.
#영어 점수를 입력 받아 정수로 변환하여 변수에 저장하시오.
# 컴퓨터 점수를 입렬 받아 정수로 변환하여 변수에 저장하시오.
eng = int(input('영어 점수 입력 : '))
com = int(input('컴퓨터 점수 입력 : '))

total= eng+com
#합계 출력
print('두 과목 점수의 합계는 ', total, '점 입니다')
print("두 과목 점수의 합계는  {}점 입니다" .format(total))