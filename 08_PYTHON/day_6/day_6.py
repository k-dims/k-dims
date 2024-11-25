'''
print('오늘도 손이 너무나 바빠핑')
print('어떻게하면 내일 쉴 수 있을까?')

print('오늘도 손이 너무나 바빠핑')
print('어떻게하면 내일 쉴 수 있을까?')

print('오늘도 손이 너무나 바빠핑') # 손과 같은 신체 부위를 바꿀 요청에 의해 바꿀 수 있도록 개선
print('어떻게하면 내일 쉴 수 있을까?') # 쉬는 일자 정보를 요청에 의해 바꿀 수 있도록 개선 

def busy_ping(body, days): 
    print(f'오늘도 {body}이 너무나 바빠핑')
    print(f'어떻게하면 {days} 쉴 수 있을까?')

# 함수 실행은 = 호출
# 발, 내일 모레

busy_ping('발', '내일 모레')

# 반복되는 코드를 작성할 때 함수를 만들면 가독성과 유지보수가 좋아짐

# 함수 만드는 방법
def 함수이름()
    print() or list.append or 딕셔너리에 값 바꾸기 등

def 함수이름(매개변수1, 매개변수2, 매개변수3):
    코드 작성
    return 매개변수를 이용한 결과값 반환
'

#len()
hello = '안녕하세요'
#oz_len()란 함수를 만들어 글자수를 반환해주세요(return)
'''
hello = '안녕하세요'
def oz_lens(hello):
    count = 0
    for i in hello: # 첫번째 반복 : 안/ 두번째 : 녕/ 세번째 반복 : 하/ ...)
        count += 1
    return count

print(oz_lens(hello))