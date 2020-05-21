# Python 코드를 IDE와 같은 편집기 상에서 직접 실행하는 경우: __name__의 값이 __main__가 됨
# >>> 인터프리터에 import 되어 실행되는 경우: __name__의 값이 모듈명이 되어 if문의 스위트가 실행되지 않음

print('We start off in: ', __name__)
if __name__ == '__main__':
    print('And end up in: ', __name__)
