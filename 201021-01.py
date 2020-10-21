# ref : 잔재미 코딩
# 파이썬 mehod는 항상 첫번째 파라미터로 self 사용
# 인자가 필요없을 때에도 self는 사용
# 클래스의 attribute 는 내부에서 접근시, self.attribute 명으로 접근

class Quadrangle:
    width = 0
    height = 0
    color = "black"
    
    def get_area(self):
        return self.width * self.height

    def set_area(self, data1, data2):
        self.width = data1
        self.height = data2

class SingleWord:
    pass

class Dave:
    width = 0
    height = 0
    color = ''

square1 = Dave()
square2 = Dave()

# print(dir(Dave))

# dir() 내장 함수는 어떤 객체를 인자로 넣어주면 해당 객체가 어떤 변수와 메소드(method)를 가지고 있는지 나열해준다.

# print(dir (SingleWord))

square = Quadrangle()
dave = Quadrangle()
dave1 = Quadrangle()

# print(dir(dave))
# print(type(square))
# print(type(dave))

square1 = Quadrangle()
square2 = Quadrangle()

dave_object = Dave()

# print(square1.color)

square2.color = 'red'

# print(square2.color)

# print(square1.color)

square1.height = 5
# print(square1.height, square2.height)


square1.width = 10
square1.height = 5
square1.color = 'red'

square2.width = 7
square2.height = 7
square2.color = 'blue'

# print(square1.width, square1.height, square1.color)
# print(square2.width, square2.height, square2.color)

# print(type(square))

square.set_area(5,5)

print(square.width)
print(square.get_area())
