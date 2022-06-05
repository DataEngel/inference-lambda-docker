import boto3
import warnings
import os

from joblib import load 

warnings.filterwarnings('ignore')


def lambda_handler(event, context):

    payload = event

    values_for_model = payload["5008807"].values()

    values_for_model = list(values_for_model)
    
    AWS_S3_BUCKET = "engel-tests-20851"
    #ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    #SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    
    s3_client = boto3.client(
        "s3",
        #aws_access_key_id=ACCESS_KEY_ID,
        #aws_secret_access_key=SECRET_ACCESS_KEY,
    )
    filename = "model_risk.joblib"
    s3_client.download_file(AWS_S3_BUCKET, filename, '/tmp/' + filename)   

    my_model = load('/tmp/model_risk.joblib') 

    prediction_result = my_model.predict([values_for_model]) 

    print("Success Prediction")
    print("prediction_result: ", prediction_result)

    return None

event_local_example = {
    "5008807" : { 
        "1" : 32, 
        "2" : 12, 
        "3" : 2, 
        "4" : 119,
        "5" : 45
        }
    }

lambda_handler(event_local_example, context=None)

