# 연습문제
class AdvancedList(list):

    def replace(self, a, b):
        for i in range(len(self)):
            if self[i] == a:
                self[i] = b
        return self

print(AdvancedList([1,2,3,1,2,3,1,2,3]).replace(1, 100))

# 연습문제 - 답안
class AdvancedList(list):

    def replace(self, a, b):
        while a in self:
            self[self.index(a)] = b

x = AdvancedList([1,2,3,1,2,3,1,2,3])
x.replace(1, 100)(

print(x)

# 심사문제
class Animal:
    def eat(self):
        print("먹다")

class Wing:
    def flap(self):
        print("파닥거리다")

class Bird(Animal, Wing):
    def fly(self):
        print('날다')

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))

##핵심문법: class의 상속 => 상속받은 자료구조 혹은 클래스의 기능과 속성을 그대로 쓸 수 있음
##공부코드: list.index(x) => x가 있는 인덱스 한개(가장 앞자리)를 출력 -> for x in list와 함께 사용