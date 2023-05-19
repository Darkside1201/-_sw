'''
작성일: 2023년 5월 19일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 5과목의 성적을 입력받아 각 과목의 점수, 총저ㅁ, 평균을 출력하는 프로그램을 반복문을 이용하여 작성하시오.
입력된 각 과목의 성적이 0부터 100 사이의 점수가 아닌 경우에만 '유효한 성적이 아닙니다'를 출력하고 다음 과목을 입력받으시오.
'''
subject = 1
total = 0 
while subject <=5 :                            # 반복문 사용
        score = int(input(str(subject) + " 번째 성적 입력 : "))
        
        # 정수를 문자열로 변환하여 사용
        if(score >=0 and score <= 100) :           # 반복문 내 선택문 사용
            total = total + score
            print(subject,"번째 성적 :",score)
            subject = subject + 1                  # 유효한 성적일 경우에만 증가
        else :
            print("유효한 성적이 아닙니다")
print("총점 :", total)
    
print("평균 :", total / 5)
    