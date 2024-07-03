from datetime import datetime
import pandas as pd
import batch

def dt(hour, minute, second=0):
    return datetime(2023, 1, 1, hour, minute, second)

def test_prepare_data():
    data = [
    (None, None, dt(1, 1), dt(1, 10)),
    (1, 1, dt(1, 2), dt(1, 10)),
    (1, None, dt(1, 2, 0), dt(1, 2, 59)),
    (3, 4, dt(1, 2, 0), dt(2, 2, 1)),      
    ]

    columns = ['PULocationID', 'DOLocationID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime']
    df = pd.DataFrame(data, columns=columns)
    
    df_actual = batch.prepare_data(df)
    print(df_actual)
    
    data_expected = [
        ('-1', '-1', 9.0),
        ( '1',  '1', 8.0),
    ]
    test_columns = ['PULocationID', 'DOLocationID', 'duration']
    df_expected = pd.DataFrame(data_expected, columns=test_columns)

    assert (df_actual['PULocationID'] == df_expected['PULocationID']).all()
    assert (df_actual['DOLocationID'] == df_expected['DOLocationID']).all()
    assert (df_actual['duration'] - df_expected['duration']).abs().sum() < 0.0000001