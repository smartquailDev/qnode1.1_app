import os

AWS_ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='qnode0-static'
AWS_S3_ENDPOINT_URL="https://sfo3.digitaloceanspaces.com/"
AWS_S3_OBJECT_PARAMETERS={
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"
}
AWS_LOCATION="https://qnode0-static.sfo3.digitaloceanspaces.com/"
DEFAULT_FILE_STORAGE="qnode0_app.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="qnode0_app.cdn.backends.StaticRootS3BotoStorage"