
stock = {
    '팥' : 10,
    '슈크림' : 8,
    '초코' : 5
}

sales = {
    '팥' : 0,
    '슈크림' : 0 ,
    '초코' : 0
}

price = {
    '팥' : 1000,
    '슈크림' : 1200 ,
    '초코' : 1500
}

def main() :
    while True : 
            mode = input('원하는 모드를 선택 해주세요.(주문, 관리자, 종료) : ')
            if mode == '종료' :
                break
            if mode == '주문' : 
                order_boong()
            if mode == '관리자' : 
                 manage_boong()

def order_boong() : #주문 기능
    while True :
        boong_type = input("주문하실 붕어빵의 맛을 골라주세요.(팥, 슈크림, 초코) or 모드선택 : ")
        if boong_type == '모드선택' : 
            break
        boong_count = int(input('주문할 붕어빵 개수를 입력하세요.')) #팥붕 10개 입력

        if stock[boong_type] >= boong_count : #  10 >= 10
            stock[boong_type] -= boong_count # 재고에서 주문받은 만큼의 붕어빵 개수를 빼는 코드
            sales [boong_type] += boong_count # 주문받은 만큼 판 붕어빵의 개수를 구하는 코드
            print(f'{boong_type} {boong_count}개를 판매 되었습니다.')
        else : 
            result = boong_count - stock[boong_type]
            print(f'죄송합니다. 헌재 {boong_type}의 재고가 {result}개 부족합니다.')
          
            #남은 재고를 맛과 개수로 보여주는 코드를 작성해주세요 딕셔너리.items() -> for boong_type, boong_count in 딕셔너리.items() 키와 밸류
        print('------------------------------')
        print('현재 재고는 아래와 같습니다.')
        for boong_t, boong_c in stock.items() :
            print(f'{boong_t} : {boong_c}')
        print('------------------------------')    

def manage_boong() : 
    while True :
        boong_type = input('추가할 붕어빵 종류를 입력하세요.(팥, 슈크림, 초코) : ')
        if boong_type == '종료' :
            break
        boong_count = int(input('추가할 붕어빵 개수를 입력하세요 :'))
        stock[boong_type] += boong_count
        print(f'{boong_type}의 재고가 {boong_count}개 추가되어, 현재 {stock[boong_type]}개 입니다.')


'''
while True : 
    mode = input('원하는 모드를 선택 해주세요.(주문, 관리자, 종료) : ')
    if mode == '종료' :
        break
    if mode == '주문' : 
        while True :
            boong_type = input("주문하실 붕어빵의 맛을 골라주세요.(팥, 슈크림, 초코) or 모드선택 : ")
            if boong_type == '모드선택' : 
                break
            boong_count = int(input('주문할 붕어빵 개수를 입력하세요.')) #팥붕 10개 입력

            if stock[boong_type] >= boong_count : #  10 >= 10
                stock[boong_type] -= boong_count # 재고에서 주문받은 만큼의 붕어빵 개수를 빼는 코드
                sales [boong_type] += boong_count # 주문받은 만큼 판 붕어빵의 개수를 구하는 코드
                print(f'{boong_type} {boong_count}개를 판매 되었습니다.')
            else : 
                result = boong_count - stock[boong_type]
                print(f'죄송합니다. 헌재 {boong_type}의 재고가 {result}개 부족합니다.')
            
                #남은 재고를 맛과 개수로 보여주는 코드를 작성해주세요 딕셔너리.items() -> for boong_type, boong_count in 딕셔너리.items() 키와 밸류
            print('------------------------------')
            print('현재 재고는 아래와 같습니다.')
            for boong_t, boong_c in stock.items() :
                print(f'{boong_t} : {boong_c}')
            print('------------------------------')
            
    
    if mode == '관리자' : 
        while True :
            boong_type = input('추가할 붕어빵 종류를 입력하세요.(팥, 슈크림, 초코) : ')
            if boong_type == '종료' :
                break
            boong_count = int(input('추가할 붕어빵 개수를 입력하세요 :'))
            stock[boong_type] += boong_count
            print(f'{boong_type}의 재고가 {boong_count}개 추가되어, 현재 {stock[boong_type]}개 입니다.')
'''
main() # 메인 함수 호출

print('시스템이 종료되었습니다.')

total_sales = 0

for boong_t in sales : #bread_t = key -> 붕어빵 맛 3가지
    sales_money = sales[boong_t] * price[boong_t]
    total_sales += sales[boong_t] * price [boong_t]


print(f'오늘의 총 매출은 {total_sales} 입니다.')