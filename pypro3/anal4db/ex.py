import MySQLdb
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

with open('mydb.dat', mode = 'rb') as obj:
    config = pickle.load(obj)

conn = MySQLdb.connect(**config)
cursor = conn.cursor()
sql = """
select buser_name, jikwon_gen, jikwon_pay
from jikwon inner join buser on buser_no=buser_num
"""
cursor.execute(sql)

df = pd.read_sql(sql, conn)
df.columns = ['번호','이름','부서','직급','성별','연봉']
print(df.pivot_table(['연봉'],index=['성별','직급'], aggfunc = np.mean))