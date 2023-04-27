import zipfile
import io
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
    resp = requests.get(url, stream=True)
    crash_io = io.BytesIO(resp.content)
    zip = zipfile.ZipFile(crash_io)
    csv_crash = zip.read("CRASH_2021_Statewide.csv")  # read csv file
    blob = bucket.blob('crashes/crashes.csv')  # create bucket
    blob.upload_from_string(
        csv_crash, content_type='application/csv')  # upload

    return 'OK'
