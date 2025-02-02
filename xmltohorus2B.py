import pandas as pd
import requests
import xml.etree.ElementTree as ET

# Function to convert DataFrame to XML
def df2xml(data):
    header = data.columns
    root = ET.Element('root')
    for row in range(data.shape[0]):
        entry = ET.SubElement(root,'entry')
        for index in range(data.shape[1]):
            schild = str(header[index])
            child = ET.SubElement(entry, 'child')
            if str(data[schild][row]) != 'nan':
                child.text = str(data[schild][row])
            else:
                child.text = 'n/a'
            entry.append(child)
    result = ET.tostring(root)
    return result

# Function to convert XML to DataFrame
def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []
    for i, child in enumerate(root):
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)

# Download the XML file from the URL using requests
sInputFileName = 'https://github.com/Apress/practical-data-science/raw/refs/heads/master/VKHCG/05-DS/9999-Data/Country_Code.xml'

response = requests.get(sInputFileName)
if response.status_code == 200:
    InputData = response.content
else:
    raise Exception(f"Failed to fetch the file: {response.status_code}")

print("==============================================================")
print('Input data values =====================================')
print("==============================================================")
print(InputData)
print('==============================================================')

# Processing Rules ==================================================

ProcessDataXML = InputData

# Convert XML to DataFrame
ProcessData = xml2df(ProcessDataXML)

# Remove columns 'ISO-2-CODE' and 'ISO-3-CODE'
if 'ISO-2-CODE' in ProcessData.columns:
    ProcessData.drop('ISO-2-CODE', axis=1, inplace=True)
if 'ISO-3-Code' in ProcessData.columns:
    ProcessData.drop('ISO-3-Code', axis=1, inplace=True)

# Rename columns
ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)

# Set 'CountryNumber' as the index
ProcessData.set_index('CountryNumber', inplace=True)

# Sort values by 'CountryName'
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)

print("==============================================================")
print('Processed Data values')
print("==============================================================")
print(ProcessData)
print("==============================================================")

# Save the processed data to a CSV file locally
sOutputFileName = 'HORUS-XML-Country.csv'
ProcessData.to_csv(sOutputFileName, index=False)

print("==============================================================")
print('XML to HORUS - Done')
print("==============================================================")
