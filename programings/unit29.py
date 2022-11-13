# # 연습문제
x = 10
y = 3

def get_quotient_remainder(x, y):
    return 10//3, 10%3

quotient, remainder = get_quotient_remainder(x, y)
print(f"몫: {quotient}, 나머지: {remainder}")

# 심사문제
x, y = map(int, input("숫제 두개: ").split())

def calc(x, y):
    return x+y, x-y, x*y, x/y

a,s,m,d = calc(x, y)
print(f"덧셈: {a}, 뺄셈: {s}, 곱셈: {m}, 나눗셈: {d}")