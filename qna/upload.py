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
        url = f"https://gomunity.shop.s3.ap-northeast-2.amazonaws.com/{image}"
    except Exception as e:
        print(e)
    return url
