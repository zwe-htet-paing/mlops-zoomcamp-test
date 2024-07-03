from datetime import datetime
import pandas as pd
import batch
import os

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

data = [
(None, None, dt(1, 1), dt(1, 10)),
(1, 1, dt(1, 2), dt(1, 10)),
(1, None, dt(1, 2, 0), dt(1, 2, 59)),
(3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
]

columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
df_input = pd.DataFrame(data, columns=columns)


input_file = batch.get_input_path(2023, 1)
output_file = batch.get_output_path(2023, 1)

S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')
# print(S3_ENDPOINT_URL)

options = {
    'client_kwargs': {
        'endpoint_url': S3_ENDPOINT_URL
    }
}

df_input.to_parquet(
    input_file,
    engine='pyarrow',
    compression=None,
    index=False,
    storage_options=options
)

os.system("python batch.py 2023 1")

df_actual = pd.read_parquet(output_file, storage_options=options)

assert abs(df_actual['predicted_duration'].sum() - 36.28) < 0.1 