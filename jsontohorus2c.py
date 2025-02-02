import pandas as pd
sInputFileName='https://github.com/Apress/practical-data-science/raw/refs/heads/master/VKHCG/05-DS/9999-Data/Country_Code.json'
InputData=pd.read_json(sInputFileName,orient='index',encoding="latin-1")
print("Input Data vlaues ============================================")
print(InputData)
print("Input Data vlaues ============================================")

ProcessData=InputData

ProcessData.drop('ISO-2-CODE',axis =1,inplace=True)
ProcessData.drop('ISO-3-CODE',axis=1,inplace=True,errors='ignore')
ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)

ProcessData.set_index('CountryNumber',inplace=True)

ProcessData.sort_values('CountryName',axis=0,ascending =False,inplace=True)
print('Process Data Values =================================')
print(ProcessData)
print('=====================================================')
OutputData = ProcessData
sOutputFileName = 'https://github.com/Apress/practical-data-science/raw/refs/heads/master/VKHCG/05-DS/9999-Data/HORUS-JSON-Country.csv'
OutputData.to_csv(sOutputFileName,index=False)
print('JSON TO HORUS - Done')
