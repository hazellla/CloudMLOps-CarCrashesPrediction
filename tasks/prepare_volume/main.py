import json
from google.cloud import storage
import functions_framework
import dotenv
dotenv.load_dotenv()


@functions_framework.http
def prepare_data(request):
    client = storage.Client()
    raw_bucket = client.bucket('509final_raw_data')  # update
    processed_bucket = client.bucket('509final_processed_data')  # update

    raw_blob = raw_bucket.blob('volumn/volumn.json')
    content = raw_blob.download_as_string()
    data = json.loads(content)

    rows = []
    for feature in data['features']:
        row = feature['properties']
        row['geog'] = json.dumps(feature['geometry'])
        rows.append(json.dumps(row))

    processed_blob = processed_bucket.blob('volumn/data.jsonl')
    processed_blob.chunk_size = 8 * 1024 * 1024
    processed_blob.upload_from_string(
        '\n'.join(rows), content_type='application/jsonl')

    return 'OK'
