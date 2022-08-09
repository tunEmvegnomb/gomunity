import datetime
import boto3
import os
from rest_framework.response import Response
from django.utils import timezone

# def upload_s3(image):
#     s3 = boto3.client('s3')
#     try:
#         s3.upload_file(
#             image, 'gomunity.shop', image,
#             ExtraArgs={
#                 'ACL': 'public-read',
#                 'ContentType': "image/jpeg"
#                     })
#     except Exception as e:
#         print(e)

def upload_s3(image, user):
    s3 = boto3.client('s3')
    
    now = datetime.datetime.now()
    now = now.strftime('%Y%m%d_%H%M%S')
    key = f"media/{user}/{now}.jpg"
    print(f"키는 ->{key}")
    print(f"유저는 ->{user}")
    try:
        s3.put_object(
            ACL="public-read",
            Bucket = 'gomunity.shop',
            Body=image,
            Key=key,
            ContentType=image.content_type
            )
        url = f"https://gomunity.shop.s3.ap-northeast-2.amazonaws.com/{key}"
        return url
    except Exception as e:
        print("오류발생")
        print(e)

