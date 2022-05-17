# 상속
class Person:
    say = '난 사람이야'
    nai = 20
    __abc = 'good'              # private 
    
    def __init__(self, nai):
        print('Person 생성자')
        self.nai = nai          # nai = 20 과 다르다.
    
    def printInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai,self.say))
        
    def hello(self):
        print('안녕') 
        print(self.__abc)
    
    @staticmethod               # static method , 어디서든 자유롭게 부를 수 있다.
    def sbs(tel):
        print('sbs _ static method ', tel)   
print(Person.say, Person.nai)
p = Person(22)
p.printInfo()
p.hello()

print('***' * 10)
class Employee(Person):
    say = '일하는 동물'
    subject = '근로자'             
       
    def __init__(self):
        print('Employee 생성자 ~~~')
    
    def printInfo(self):
        print('Employee 클래스 내의 pritnInfo')
        
    def eprintInfo(self):       # method override
        self.printInfo()
        super().printInfo()     # super().printInfo() 는 부모의 printInfo()를 찾아간다.
        print(self.say, super().say)
        self.hello()

e = Employee()
print(e.say, e.nai)
print(e.subject)
e.printInfo()
e.eprintInfo()

print('***' * 10)
class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai)       # Bound method call
    
    def wprintInfo(self):
        super().printInfo()
    
w = Worker('25')
print(w.say,w.nai)
w.printInfo()
w.wprintInfo()

print('~~~' * 10)
class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        Worker.__init__(self, nai)  # unBound method call
        
    def wprintinfo(self):           # overriding
        print('Programmer 내에 작성된 wprintInfo')
        
    def hello2(self):
        print(super().__abc)
        
    
pr = Programmer(33)
print(pr.say, pr.nai)
pr.printInfo()
pr.wprintinfo()

print('***' * 10)
p.hello()
# pr.hello2()                      # private 이기 때문에 err
w.sbs('111-1111')
pr.sbs('222-2222')

print('클래스 타입---')
a = 10
print(type(a))                     # <class 'int'>
print(type(pr))                    # <class '__main__.Programmer'>
print(Programmer.__bases__)        # (<class '__main__.Worker'>,)
print(Worker.__bases__)            # (<class '__main__.Person'>,)
print(Person.__bases__)            # (<class 'object'>,)