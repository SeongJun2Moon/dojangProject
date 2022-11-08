#연습문제
a = {i for i in range(1,101) if i%3==0}
b = {i for i in range(1,101) if i%5==0}
print(a & b)

#심사문제
a,b = map(int, input("숫자 두개: ").split())
se1 = {i for i in range(1,a+1) if a%i==0}
se2 = {i for i in range(1,b+1) if b%i==0}
print(sum(se1&se2))

## 핵심문법:
# 데이터타입 set{} => 생성방법: a = set() -> a = {} 요렇게하면 딕셔너리됨
# 순서가 없음 => 시퀀스x
# set안에 set넣기 x
# 집합문법 => | : 합집합, & : 교집합, - : 차집합, ^ : 대칭차집합(=안겹치는거)