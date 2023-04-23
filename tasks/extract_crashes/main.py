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
    url = 'https://www.arcgis.com/sharing/rest/content/items/cbb78b74142b46a3b1698cd769d983c8/data'
    resp = requests.get(url)
    json_data = resp.text
    blob = bucket.blob('crashes/crashes.json')
    blob.upload_from_string(json_data, content_type='application/json')

    return 'OK'
