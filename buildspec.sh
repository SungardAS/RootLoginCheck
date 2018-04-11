
source .env.local

cd src; npm install; cd ..

aws cloudformation package \
   --template-file ./template.yaml \
   --s3-bucket $S3_BUCKET_NAME \
   --output-template-file samTemplate.yaml


aws cloudformation deploy --template-file ./samTemplate.yaml \
  --capabilities CAPABILITY_IAM \
  --stack-name SungardAS-aws-services-alerts-destination \
  --parameter-overrides CloudWatchLogDestinationArn=$CLOUDWATCHLOG_DESTINATION_ARN \
  CloudWatchLogGroupName=$CLOUDWATCHLOG_GROUP_NAME ProjectImage=$PROJECT_IMAGE
