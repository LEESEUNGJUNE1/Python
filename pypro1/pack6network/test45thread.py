#Thread
# process는 실행 가능한 파일을 말한다. 프로세스는 현재 실행중인 프로그램을 의미하면서 tesk 라고도 불린다.
# process의 작은 실행단위를 thread라고 한다. thread 기법을 이용하면 여려개의 thread를 통해 여러개의 작업을 할수있다.
# multi thread에 의한 multi tasking이 가능하다.

import threading, time

def run(id):
    for i in range(1,11):
        print('id:{}-->{}'.format(id,i))
        time.sleep(0.5)

# 1) thread X
# run('일') # 순차적
# run('이')

# 2) thread O
th1 = threading.Thread(target = run, args = ('일',))
th2 = threading.Thread(target = run, args = ('이',))
th1.start()
th2.start()

th1.join()
th2.join()

print('프로그램 종료')