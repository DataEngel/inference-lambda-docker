import boto3
import warnings
import os

from joblib import load 

warnings.filterwarnings('ignore')


def lambda_handler(event, context):

    d = {
        5008807: [65, 0, 1, 10000, 1]
        }
    
    AWS_S3_BUCKET = "engel-tests-20851"
    ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY,
    )
    filename = "model_risk.joblib"
    s3_client.download_file(AWS_S3_BUCKET, filename, '/tmp/' + filename)   

    my_model = load('/tmp/model_risk.joblib') 

    prediction_result = my_model.predict([d[5008807]]) 

    print("prediction_result: ", prediction_result)

    return None

event={}

lambda_handler(event, context=None)





