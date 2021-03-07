import pandas as pd
import beam,os,logging, argparse
import cloudstorage as storage
import PipelineOptions


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
       df.drop_duplicates(subset='Transaction unique identifier', keep='first', inplace=True)
       df2 = df.sort_values(by=['Postcode','Street','SAON','PAON'])
       df2.to_json(self.outputFilePath,orient='records', lines=True)




class DataflowPipeline(PipelineOptions):
 
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument('--inputFilePath', type=str, default='gs://ingest_bucket/Input/pp-monthly-update-new-version.csv')
        parser.add_argument('--outputFilePath', type=str, default='gs://processed_bucket/json/pp-monthly-update-new-version.json')
        
        
def run(argv=None):
    parser = argparse.ArgumentParser()
    known_args, pipeline_args = parser.parse_known_args(argv)
 
    pipeline_options = PipelineOptions(pipeline_args)
    dataflow_options = pipeline_options.view_as(DataflowPipeline)
 
    with beam.Pipeline(options=pipeline_options) as pipeline:
        (pipeline
         | 'Start' >> beam.Create([None])
         | 'Convertion CSV to JSON' >> beam.ParDo(CsvToJsonConvertion(dataflow_options.inputFilePath, dataflow_options.outputFilePath))
         )
 
 
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()