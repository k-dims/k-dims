fish_bread = input('맛을 입력하세요 : ') #맛을 입력 받아요
count = int(input('개수를 입력하세요 : ')) #개수를 입력 받아요

stock = {
    "팥" : 10,
    "슈크림" : 8,
    "초코" : 5
}

stock[fish_bread] += count
print(f'{fish_bread}맛을 {count}개 채워 현재 재고는 {stock[fish_bread]}개 입니다.')
