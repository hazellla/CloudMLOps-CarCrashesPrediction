import json
import requests
from google.cloud import storage
import functions_framework
import dotenv
dotenv.load_dotenv()


@functions_framework.http
def extract_data(request):
    client = storage.Client()
    bucket = client.bucket('musa509s23_team01_raw_data')
    url = 'https://www.pasda.psu.edu/json/PaTraffic2023_04.geojson'
    resp = requests.get(url)
    json_data = resp.json()
    json_data2 = json.dumps(json_data)
    blob.upload_from_string(json_data2, content_type='application/json')

    return 'OK'
