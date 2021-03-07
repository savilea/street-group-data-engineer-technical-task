import boto3
import pandas as pd


df = pd.read_csv('C:/Users/adams/OneDrive/Documents/GitHub/street-group-data-engineer-technical-task/pp-monthly-update-new-version.csv')

df.columns =['Transaction unique identifier','Price','Date of Transfer','Postcode','Property Type','Old/New','Duration','PAON','SAON','Street','Locality','Town/City','District','County','PPD Category Type','Record Status']

df2 = df.sort_values(by=['Postcode','Street','SAON','PAON'])

print(df)

df2.to_json(orient='records', lines=True,path_or_buf='C:/Users/adams/OneDrive/Documents/GitHub/street-group-data-engineer-technical-task/street_group_test.json')



