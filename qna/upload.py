import datetime
import boto3

def upload_s3(image):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(
            image, 'gomunity.shop', image,
            ExtraArgs={
                'ACL': 'public-read',
                'ContentType': "image/jpeg"
                    })
    except Exception as e:
        print(e)


now = datetime.datetime.now()
# now = now.strftime('%Y%m%d_%H%')