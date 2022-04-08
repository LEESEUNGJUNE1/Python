# 상속
class Person: # <= 최상위 super class 이다.
    say = ' 난 사람이야'
    nai = 20

    def __init__(self, nai): 
        print('Person 생성자')
        self.nai = nai # 위에 nai=20 과는 다르다.

    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say)) # self 를 this 와 비교하자

    def hello(self):
        print('안녕')

print(Person.say, Person.nai)
p = Person(22)
p.printInfo()
p.hello()

print('***' * 10)
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자' # 임플로이 고유
    
    def __init__(self):
        print('Employee 생성자 ~~~')

    def printInfo(self): # method Override (재정의)
        print('Employee 클래스 내의 printInfo')

    def eprintInfo(self):
        self.printInfo() # 현재 class에서 'printInfo'가 있는지 먼저 찾는다. ( 없으면 부모로 올라간다.)
        super().printInfo() # 처음부터 Person(부모)의 printInfo를 부른다.
        print(self.say, super().say)
        self.hello()

e = Employee()
print (e.say, e.nai)
print (e.subject)
e.printInfo()
e.eprintInfo()


print('---' * 10)
class Worker(Person):
    def __init__(self, nai):
        print('Worker  생성자')
        super().__init__(nai)

    def wprintInfo(self):
        super().PrintInfo()

w = Worker('25')
print(w.say, w.nai)
w.printInfo()
w.wprintInfo()


print('~~~' * 10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        worker.__init__(self, nai) # unBound method call

    def wprintinfo(self): # 오버라이딩
        print('programmer 내에 작성된 wprintinfo')

pr = Programmer(33)
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintInfo()