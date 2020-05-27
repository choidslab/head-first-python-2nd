class CountFromBy:
    def __init__(self, v=0, i=1):
        self.val = v
        self.incr = i

    def increase(self):
        self.val += self.incr

    def __repr__(self):  # 객체에 대한 표현 정의, 기본값은 객체의 주소(hex)
        return str(self.val)


if __name__ == "__main__":
    h = CountFromBy(100, 10)
    print(h.val)

    h.increase()
    print(h.val)
    print(h)

    test = CountFromBy()  # 객체 초기화 X
    print(test.val)
    print(test.incr)
    print(test)
