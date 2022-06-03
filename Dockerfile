FROM public.ecr.aws/lambda/python:3.8 

RUN pip install --no-cache-dir --upgrade pip && \
    pip3 install -U scikit-learn && \
    pip install boto3

COPY lambda_function.py ${LAMBDA_TASK_ROOT}

CMD [ "lambda_function.lambda_handler" ]

