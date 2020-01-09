# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
p_a=len(df[df['fico']>700])/len(df)
p_b=len(df[df['purpose']=='debt_consolidation'])/len(df)
df1=df[(df['purpose']=='debt_consolidation')&(df['fico']>700)]
a_i_b=len(df1)/len(df)
p_a_b=a_i_b/p_a
p_b_a=a_i_b/p_b
result=(p_b_a==p_a)
print(result)







# code ends here


# --------------
# code starts here
prob_lp=len(df[df['paid.back.loan']=='Yes'])/len(df)
prob_cs=len(df[df['credit.policy']=='Yes'])/len(df)
new_df=df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')] 
intersect=len(new_df)/len(df)
prob_pd_cs=intersect/prob_lp
bayes=(prob_pd_cs*prob_lp)/prob_cs
print(bayes)



# code ends here


# --------------
# code starts here
df1=df[df['paid.back.loan']=='No']
plt.bar(df1.index,df1['purpose'])
plt.show()

# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
df['installment'].plot(kind='hist')
plt.show()
df['log.annual.inc'].plot(kind='hist')
plt.show()

# code ends here


