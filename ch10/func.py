"""
Fucntion Decorator(함수 장식자) 구현을 위해 알아야할 함수의 특징
  - 함수를 함수로 전달하기, 함수는 parameter로 함수를 받을 수 있음
  - 함수 안에 함수를 중첩하여 구현할 수 있음
  - 함수에서 함수를 반환(Return)할 수 있음
"""


# 함수에 함수를 parameter로 전달하는 예제
def apply(func, value):
    return func(value)


# 중첩함수(Nested Fucntion) 예제 --> 여러 행에 걸쳐 함수의 호출이 많은 경우 함수 호출을 추상화하여 표현할 때 중첩함수를 활용하면 코드를 읽기 쉬워지고 코드를 간소화 할 수 있다.
def outer():
    def inner():
        print('This is inner function')
    print('This is outer function')
    return inner()


if __name__ == "__main__":
    apply(print, 42)
    print(apply(id, 42))
    print(apply(type, 42))
    print(apply(len, 'dschoi'))
    print(apply(type, apply))
    print()

    outer() # 중첩함수를 호출하였을 때 내부 중첩된 함수를 반환하여 결과를 출력할 수 있음
