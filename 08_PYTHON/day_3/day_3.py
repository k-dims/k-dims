
receipts = [] #빈 리스트, 영수증
balance = 1000 # 3000

while True:
    num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)") # "1"
    if num == "1":
        #입금 기능
        deposit_amount = int(input("입금할 금액을 입력해주세요 : ")) # 3000 문자형태 "3000"
        balance += deposit_amount # balance = balance + deposit_amount
        receipts.append(("입금",deposit_amount,balance))
        print(f'입금하신 금액은 {deposit_amount}원이고, 현재 잔액은 {balance}원 입니다.')
    elif num == "2":
        #출근 기능
        withdraw_amount = int(input("출금할 금액을 입력해주세요 : ")) # 3000 문자형태 "3000"
        withdraw_amount = min(balance, withdraw_amount) #(4000)  / (5000) / (3000) 
        balance -= withdraw_amount # balance = balance - withdraw_amount
        receipts.append(("출금",withdraw_amount,balance))
        print(f'출금하신 금액은 {withdraw_amount}원이고, 현재 잔액은 {balance}원 입니다.')
    elif num == "3":
        #영수증 내역 출력
        print(receipts)
    elif num == "4":
        break

print(f"서비스를 종료합니다. 현재 잔액은 {balance}원 입니다.")