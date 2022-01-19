
import pandas as pd
demo=pd.read_excel(r'C:\Users\Abdul\Downloads\Data_Engineering.xlsx')
demo_fil=demo[['Customer_ID','Customer_Name']]
demo_fil
demo.columns
trns=pd.read_excel(r'C:\Users\Abdul\Downloads\Data_Engineering.xlsx',sheet_name=1)
trns
trns_fil=trns.groupby('Customer_ID')['Transaction_Date'].count()
trns_fil
no_trns_fil=pd.DataFrame(trns_fil)
no_trns_fil
fin=pd.read_excel(r'C:\Users\Abdul\Downloads\Data_Engineering.xlsx',sheet_name=2)
fin
fin_fil=fin[['Customer_ID','Income']]
fin_fil
demotrns=demo_fil.merge(no_trns_fil,how='inner',on='Customer_ID')
demotrns
demotrnsfin=demotrns.merge(fin_fil,how='inner',on='Customer_ID')
demotrnsfin
demotrnsfin_con1=demotrnsfin[((demotrnsfin.Income>10000)&(demotrnsfin.Income<30000))&(demotrnsfin.Transaction_Date>=2)]
demotrnsfin_con1
demotrnsfin_con2=demotrnsfin[((demotrnsfin.Income>30000)&(demotrnsfin.Income<50000))&(demotrnsfin.Transaction_Date>=1)]
demotrnsfin_con2
demotrnsfin_con3=demotrnsfin[((demotrnsfin.Income>50000)&(demotrnsfin.Income<60000))&(demotrnsfin.Transaction_Date>=1)]
demotrnsfin_con3
demotrnsfin_con4=demotrnsfin[(demotrnsfin.Income>60000)&(demotrnsfin.Transaction_Date>=1)]
demotrnsfin_con4
finlresult=pd.concat([demotrnsfin_con1,demotrnsfin_con2,demotrnsfin_con4],axis=0)
finlresult
finlresult.head()
finlresult.tail()
