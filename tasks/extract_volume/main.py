import json
import requests
from google.cloud import storage
import functions_framework
import dotenv
dotenv.load_dotenv()


@functions_framework.http
def extract_data(request):
    client = storage.Client()
    bucket = client.bucket('509final_raw_data')
    url = 'https://www.pasda.psu.edu/json/PaTraffic2023_04.geojson'
    resp = requests.get(url, stream=True)
    json_data = resp.text
    blob = bucket.blob('volumn/volumn.json')
    blob.chunk_size = 8 * 1024 * 1024
    blob.upload_from_string(json_data, content_type='application/json')
    return 'OK'
