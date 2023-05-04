import pathlib
from google.cloud import bigquery
import functions_framework
import dotenv
dotenv.load_dotenv()

DIR = pathlib.Path(__file__).parent
# print(DIR / 'create_source_data_crashes.sql')


@functions_framework.http
def load_data(request):
    client = bigquery.Client(project='musa509-378614')
    print(DIR)
    # print(DIR / 'create_source_data_crashes.sql')

    with open(DIR / 'create_source_data_crashes.sql') as f:
        sql = f.read()
    job = client.query(sql)
    job.result()

    # with open(DIR / 'create_internal_table_opa_properties.sql') as f:
    #     sql = f.read()
    # job = client.query(sql)
    # job.result()

    return 'OK'
