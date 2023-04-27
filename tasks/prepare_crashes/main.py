import json
from google.cloud import storage
import functions_framework


@functions_framework.http
def prepare_data(request):
    client = storage.Client()
    raw_bucket = client.bucket('509final_raw_data')  # update
    processed_bucket = client.bucket('509final_processed_data')  # update

    raw_blob = raw_bucket.blob('crashes/crashes.json')
    content = raw_blob.download_as_string()
    # print(content)
    data = json.loads(content)
    print(data)

    # rows = []
    # FEELS LIKE THIS SHOULD BE UPDATED AFTER WE CHECK THE ACTUAL JSON DATA
    # for feature in data['features']:
    #     row = feature['assessments']
    #     row['geog'] = json.dumps(feature['geometry'])
    #     rows.append(json.dumps(row))

    # processed_blob = processed_bucket.blob('crashes/data.jsonl')
    # processed_blob.upload_from_string(
    #     '\n'.join(rows), content_type='application/jsonl')

    return 'OK'
