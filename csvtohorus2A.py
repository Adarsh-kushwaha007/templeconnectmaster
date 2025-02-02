import pandas as pd
sInputFileName = 'https://media.githubusercontent.com/media/Apress/practical-data-science/refs/heads/master/VKHCG/05-DS/9999-Data/Country_Code.csv'
InputData = pd.read_csv(sInputFileName,encoding="latin-1")
print("Input Data Values ===================================")
print(InputData)
print("======================================================")

#Processing Rules

ProcessData= InputData

ProcessData.drop('ISO-2-CODE',axis=1,inplace=True)
ProcessData.drop('ISO-3-Code',axis=1,inplace=True)

ProcessData.rename(columns={'Country':'CountryName'},inplace=True)
ProcessData.rename(columns={'ISO-M49':'CountryNumber'},inplace=True)

#set new Index
ProcessData.set_index('CountryNumber',inplace=True)
ProcessData.sort_values('CountryName',axis=0,ascending=False,inplace=True)
print("Process Data values==========================")
print(ProcessData)
print("===================================================")

OutputData = ProcessData

sOutputFileName='https://media.githubusercontent.com/media/Apress/practical-data-science/refs/heads/master/VKHCG/05-DS/9999-Data/HORUS-CSV-Country.csv'
OutputData.to_csv(sOutputFileName, index=False)

print("CSV to HORUS - Done")
