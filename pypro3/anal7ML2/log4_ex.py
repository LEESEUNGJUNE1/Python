# [로지스틱 분류분석 문제2] 
# 게임, TV 시청 데이터로 안경 착용 유무를 분류하시오.
# 안경 : 값0(착용X), 값1(착용O)
# 예제 파일 : https://github.com/pykwon  ==>  bodycheck.csv
# 새로운 데이터(키보드로 입력)로 분류 확인. 스케일링X

from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.model_selection import train_test_split
import statsmodels.api as sm
import statsmodels.formula.api as smf
import numpy as np

df = pd.read_csv("../testdata/bodycheck.csv")
print(df.head(3), df.shape) # (20, 6)

df2 = pd.DataFrame()
df2 = df.drop(['신장','체중','번호'], axis =1)
print(df2)

arr = df.values
x = arr[:, 0:3]
print(x[:3],x.shape)

y = arr[:,3]
print(y[:3],y.shape)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size = 0.33, random_state=7)
print(x_train.shape, x_test.shape)

model = LogisticRegression()
model.fit(x_train, y_train)
print('예측값 : ', model.predict(x_test[:5]))
print('실제값 : ', y_test[:5])
print((model.predict(x_test) != y_test).sum())  # 
print('test 로 분류 정확도 : ', model.score(x_test, y_test))            #
print('train 으로 분류 정확도 : ', model.score(x_train, y_train))        # 

from sklearn.metrics import accuracy_score
pred = model.predict(x_test)
print('분류 정확도 : ', accuracy_score(y_test, pred))

print(x_test[:1])   # 분류를 원하는 새로운 데이터라고 가정
print('분류 예측 : ', model.predict(x_test[:1])) 

