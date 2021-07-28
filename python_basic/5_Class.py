# 객체 지향 프로그래밍 : 데이터 효율적 관리, 중복 코드 방지, 직관적인 코드 분석, 상속을 통한 재활용

# class 가 필요한 이유 (예시)
# 만일 한 프로그램에서 2대의 계산기가 필요한 상황이 발생하면 어떻게 해야 할까?
# 각 계산기는 각각의 결괏값을 유지해야 하기 때문에 위와 같이 add 함수 하나만으로는 결괏값을 따로 유지할 수 없다.
# 이런 상황을 해결하려면 다음과 같이 함수를 각각 따로 만들어야 한다.
# result1 = 0
# result2 = 0

# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))

# -> 3
# 7
# 3
# 10

# 계산기 1의 결괏값이 계산기 2에 아무 영향을 끼치지 않음을 확인할 수 있다.
# 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까? 그때마다 전역 변수와 함수를 추가할 것인가?
# 여기에 빼기나 곱하기 등의 기능을 추가해야 한다면 상황은 점점 더 어려워질 것이다.
# 위와 같은 경우에 클래스를 사용하면 다음과 같이 간단하게 해결할 수 있다.

# Calculator 클래스로 만든 별개의 계산기 cal1, cal2(파이썬에서는 이것을 객체라고 부른다)가 각각의 역할을 수행한다.
# 그리고 계산기(cal1, cal2)의 결괏값 역시 다른 계산기의 결괏값과 상관없이 독립적인 값을 유지한다.
# 클래스를 사용하면 계산기 대수가 늘어나더라도 객체를 생성만 하면 되기 때문에 함수를 사용하는 경우와 달리 매우 간단해진다

# class Calculator:
#     def __init__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# -> 3
# 7
# 3
# 10





# self
class Self:
    def f1():
        print("f1 called!")
    def f2(self):
        print("f2 called!")

self_test = Self()

# 1. self 인자가 없는 경우
# self_test.f1() -> error : f1에 self 인자가 없으므로 어떤 인스턴스의 f1인지 알 수가 없음
Self.f1() # -> 반면 class에서 f1을 호출하는 것은 self인자가 없어도 가능

# 2. self 인자가 있는 경우
self_test.f2() # -> 인스턴스에서 바로 호출 가능
Self.f2(self_test) # -> class에서 호출할 경우 self인자를 넣어줘야 함
print()






class UserInfo : # 클래스명 단어 각각 첫글짜는 항상 대문자
    # 속성(이름, 키, 몸무게, 나이 등), 메소드(걷다, 뛰다 등)
    # def 메소드 (속성) :

    def __init__(self, name): # self : 인스턴스 변수
        self.name = name

    def user_info_p(self):
        print("Name : ", self.name)

user1 = UserInfo("Kang") # user1은 object(객체) 이며, user1은 UserInfo의 인스턴스 이다.
user1.user_info_p()

user2 = UserInfo("Park")
user2.user_info_p()



# 과자 틀 → 클래스 (class)
# 과자 틀에 의해서 만들어진 과자 → 객체 (object)
# 클래스로 만든 객체의 중요한 특징 :  객체마다 고유한 성격을 가진다. 과자 틀로 만든 과자에 구멍을 뚫거나 조금 베어 먹더라도 다른 과자에는 아무 영향이 없는 것과 마찬가지로 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.

# 메모리 주소값 확인 : id()
print(id(user1))
print(id(user2))

# 네임스페이스(객체를 인스턴스화 할 때 저장된 공간) 확인 : .__dict__
print(user1.__dict__)
print(user2.__dict__)
print()




# class 변수
class WareHouse:
    warehouse_num = 0 # class 변수 : 인스턴스들 모두 공유하는 변수

    def __init__(self, name): # 인스턴스가 생성 될 때마다 호출
        self.name = name
        WareHouse.warehouse_num += 1 # 창고가 하나 생길 때마다 창고의 숫자를 하나씩 증가

    def __del__(self): # 인스턴스가 종료 될 때마다 호출
        WareHouse.warehouse_num -= 1 # 창고가 하나 없어질 때마다 창고의 숫자를 하나씩 감소

user1 = WareHouse("Kang")
user2 = WareHouse("Kim")
user3 = WareHouse("Park")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)

print(WareHouse.__dict__) # warehouse_num은 class 변수이기 때문에 WareHouse의 __dict__를 통해 확인할 수 있음

print(user1.warehouse_num) # warehouse_num은 인스턴스들 모두가 공유하는 변수이기 때문에 모든 인스턴스를 통해 확인할 수 있음
print(user2.warehouse_num)
print(user3.warehouse_num)
print()



# class 상속
# 슈퍼클래스 (부모)
# 서브클래스 (자식) -> 모든 속성, 메소드 사용 가능
# class 상속을 사용하는 이유 : 중복 코드를 방지하고 코드를 재사용할 수 있음

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.tp = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color): 
        super().__init__(tp, color) # tp와 color은 부모 (슈퍼클래스)로 올릴 인자
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s " % self.car_name

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color): 
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s " % self.car_name

    def show(self): # super(부모)에도 있는 동일한 메소드
        # print(super().show()) -> 부모의 메소드도 호출하고 싶을 경우
        return 'Car info : %s %s %s' % (self.car_name, self.tp, self.color)


model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # super(부모)에서 상속 받음
print(model1.tp) # super(부모)에서 상속 받음
print(model1.car_name) # sub(자식)
print(model1.show()) # super(부모)
print(model1.show_model()) # sub(자식)
print(model1.__dict__) # sub(자식)에서 초기화된 것 뿐만 아니라, super(부모)에서 초기화된 것도 상속 받아 가지고 있음
print()



# Method OverRiding(오버라이딩)
# super(부모)의 메소드를 모두 사용하는 것이 아니라 상속 받을건 받고 기능을 개선하거나 내용을 새롭게 목적에 맞게 다시 재구현하는 것 (코드 재활용)
# 메소드의 이름은 같지만 내용은 다름
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show()) 
print()


# 상속 정보 (Inheritance Info)
print(BmwCar.mro())
print(BenzCar.mro())
print()



# 다중 상속
# (주의) 너무 복잡한 다중 상속은 코드 해석에 어려움을 줄 수 있음
class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class C(A,B,Y):
    pass

print(C.mro())