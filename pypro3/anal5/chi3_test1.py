# 카이제곱 문제1) 부모학력 수준이 자녀의 진학여부와 관련이 있는가?를 가설검정하시오
#   예제파일 : cleanDescriptive.csv
#   칼럼 중 level - 부모의 학력수준, pass - 자녀의 대학 진학여부
#   조건 :  level, pass에 대해 NA가 있는 행은 제외한다.
import pandas as pd
import scipy.stats as stats

data = pd.read_csv("../testdata/cleanDescriptive.csv")
df = pd.DataFrame(data)
print(df)
data = df.dropna(subset=['level', 'pass'], how='any')
print(data.head(5))
print(data['level'].unique())
print(data['pass'].unique())
ctab = pd.crosstab(index =data['level'], columns=data['pass'])
ctab.index = ['고졸','대졸','대학원졸']
ctab.columns = ['합격','실패']
print(ctab)
chi_result = [ctab.loc['대학원졸'],ctab.loc['대졸'],ctab.loc['고졸']]
chi2, p, ddof, _ = stats.chi2_contingency(ctab)

print('chi2:{}, p:{}, ddof:{}'.format(chi2,p,ddof))
# 귀무가설 : 부모학력 수준이 자녀의 진학여부와 관련이 없다.
# 대립가설 : 부모학력 수준이 자녀의 진학여부와 관련이 있다.
# p:0.25070568406521365 > 0.05 이므로 귀무가설 채택, 대립가설 기각