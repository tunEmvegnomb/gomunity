import datetime
import boto3
import os
from rest_framework.response import Response
from django.utils import timezone

def upload_thumbnail_s3(image, user):
    s3 = boto3.client('s3')
    
    now = datetime.datetime.now()
    now = now.strftime('%Y%m%d_%H%M%S')
    key = f"media/{user}/{now}.jpg"
    
    try:
        s3.upload_file(
            image, 'gomunity.shop', key,
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': "image/jpeg"
                    })
        url = f"https://gomunity.shop.s3.ap-northeast-2.amazonaws.com/{key}"
        return url
    except Exception as e:
        print(e)


def upload_s3(image, user):
    s3 = boto3.client('s3')
    
    now = datetime.datetime.now()
    now = now.strftime('%Y%m%d_%H%M%S')
    key = f"media/{user}/{now}.jpg"
    try:
        s3.put_object(
            ACL="public-read",
            Bucket = 'gomunity.shop',
            Body=image,
            Key=key,
            ContentType="image/jpeg"
            )
        url = f"https://gomunity.shop.s3.ap-northeast-2.amazonaws.com/{key}"
        return url
    except Exception as e:
        print(e)

