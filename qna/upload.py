import datetime
import boto3

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


def upload_s3(image):
    s3 = boto3.client('s3')
    
    now = datetime.datetime.now()
    now = now.strftime('%Y%m%d_%H%M%S')
    key = f"media/{now}.jpg"
    
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

