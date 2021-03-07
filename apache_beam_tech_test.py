import boto3
import pandas as pd
import beam
import os
import cloudstorage as storage


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'secured.json'


class CsvToJsonConvertion(beam.DoFn):
 
    def __init__(self, inputFilePath,outputFilePath):
        self.inputFilePath = inputFilePath
        self.outputFilePath = outputFilePath
 
    def start_bundle(self):
        self.client = storage.Client()
 
    def process(self, something):
       df = pd.read_csv (self.inputFilePath)
       df.columns =['Transaction unique identifier','Price','Date of Transfer','Postcode','Property Type','Old/New','Duration','PAON','SAON','Street','Locality','Town/City','District','County','PPD Category Type','Record Status']
       df2 = df.sort_values(by=['Postcode','Street','SAON','PAON'])
       df2.to_json(self.outputFilePath,orient='records', lines=True)




