'''

https://tartan-steel-3da.notion.site/14108b43002680b59ce8cad669547c28 참조

식별자와 변수명

식별자는 프로그래밍 언어에서 변수, 함수, 클래스, 모듈 등의 이름을 지정하는 모든 명칭 뜻함니다.
변수명은 변수의 이름을 뜻한다.(값을 저장할 메모리 공간을 참조하기 위해 사용되는 이름)
변수는 데이터를 저장하는 컨테이너이고 변수명은 컨테이너를 가르키는 이름이다

- 특수 문자는 **언더 바(_ )**만 허용됩니다.
- **숫자**로 시작하면 안 됩니다.
- **공백**을 포함할 수 없습니다.
- + 가급적 **알파벳**을 사용해주세요.
- + **유의미**한 뜻으로 짓되 누구나 알 수 있어야 합니다.


import keyword
print(keyword.kwlist)


print("{}".format(8)) # 8
print("{}{}".format(8,"기")) # 8기
print("{}{} {}".format(8,"기","백엔드")) # 8기 백엔드

str = "{}".format(8) # 변수에 저장
print(str)

num = 8
str_a = "기"
str_b = "백엔드"


print(f"{num}{str_a} {str_b}")

내장함수는 무엇이 있는지?(공부 꼭 해보기)

print(type(777)) # 코드 타입 확인
print(type(777.777))


# 21 + 29 = 50, 50은 계산결과로 출력
num_1 = "21"
num_2 = "29"
print("21 + 29 =", 50)



position = "백엔드"
get_in = "3명 타세요"

print(position * 3)
print(position + get_in)
print(position + get_in * 3)


str = "초격차백엔드"

print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
print(str[5])
print(str[-1], str[-2], str[-3], str[-4], str[-5], str[-6])

#len() 미리 만들어 놓은 기능 = 내장함수

str = "초격차백엔드"

#변수 [시작위치:끝나는위치] : 시작위치부터 출력되고 끝나는 위치 -1까지만 출력된다
#str[2:4] => 차백
#print(str[2:4])
#print(str[:4])
#print(str[0:7:2]) # 0,2,4 

alpa = 'A'

print(alpa.isupper()) # 대소문자를 구별 > True or False

'''
#url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
#keyword = input("검색하고 싶은 키워드를 입력하세요 : ") #입력을 받을 수 있도록 미리 만들어준 기능. 내장함수

#print(url+keyword)

#if 조건 해당된다면
#   아래 있는 코드를 실행해

str = "초격차백엔드"

if len(str) > 7 :
    print("참이구나")
elif len(str) > 5 :
    print("이번에는 맞췄구나")
else :
    print("바보")