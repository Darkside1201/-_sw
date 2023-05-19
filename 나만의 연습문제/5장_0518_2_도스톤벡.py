'''
작성일: 2023년 5월 18일
학과 : 컴퓨터공학부
학번 : 202395035
이름 : 도스톤벡
설면 : 두 개의 숫자를 입력받아 두 수 사이의 모든 정수값을 더하여 출력하는 프로그래을 작성하시오.
입력받은 두 개의 수를 포함하여 덧셈하시오
'''
first = int(input("첫 번째 숫자 입력 : "))   # 두 개의 숫자 입력
second = int(input("두 번째 숫자 입력 : "))

if first > second :  # 크기 비교하여 작은 수는 first, 큰 수는 second에 저장
    
    temp = first     # 두 수 교환
    first = second
    second = temp
    
print(first,"부터", second,"까지의 합은 :",end='')
# end를 사용하여 인쇄 후에 줄을 바꾸지 않는다
sum = 0
while first <= second :   # first가 second보다 작거나 같을 때까지 반복 
    
    sum = sum + first
    first = first + 1
    
print(sum)