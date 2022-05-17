# 일급함수 지원 성립 조건

def func1(a, b):
    return a + b

func2 = func1       # 주소를 치환

print(func1(2,3))
print(func2(2,3))

print()
def func3(f):       # 매개변수로 함수
    def func4():    # 내부함수
        print('나는 내부함수야~~~')
    func4()
    return f        # 반환값이 함수

mbc = func3(func1)
print(mbc(2,3))

print('----람다(Lambda) 함수 - 축약함수:이름이 없는 한 줄 짜리 함수-----------')
# def 를 쓸 정도로 복잡하지 않거나, def 를 쓸 수 없는 곳에 사용
# 형식 : lambda 인자,... : 표현식    <== return 없이 결과를 반환
def Hap(x,y):
    return x + y 

print(Hap(1,2))

print((lambda x, y:x + y)(1,2))     #lambda 함수 사용 (1회용) *대개는 1회성으로 사용

g = lambda x, y: x * y              #lambda 함수를 변수로 사용
print(g(3,4))
imsi = g(3,4)
print(imsi)

print()
kbs = lambda a, su=10:a + su        #lambda도 가변인수 사용 가능
print(kbs(5))
print(kbs(5,6))

sbs = lambda a, *tu, **di:print(a, tu, di)
sbs(1,2,3,m=4,n=5)

print()
li = [lambda a,b:a+b, lambda a,b:a*b]   #lambda 안에 여러값 넣어보기
print(li[0](3,4))
print(li[1](3,4))

print()
# filter(함수, sequence자료)
print(list(filter(lambda a:a < 5, range(10))))  
print(list(filter(lambda a:a % 2, range(10))))  #홀수값 출력
print(list(filter(lambda a:a % 5 == 0 or a % 7 == 0, range(1,101))))    #1~100 사이에 5의 배수 이거나 7의 배수 