# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file.
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions
# and limitations under the License.
#
# Description: This Lambda function sends an SNS notification to a given AWS SNS topic when an API call event by IAM root user is detected.
#              The SNS subject is- "API call-<insert call event> by Root user detected in Account-<insert account alias>, see message for further details". 
#              The JSON message body of the SNS notification contains the full event details.
# 
#
# Author: Sudhanshu Malhotra
# Updated:  Bob Peterson, Sungard Availability Services.
# Update to see if it shows up

import json
import boto3
import logging
import os
import botocore.session
import urllib2
from botocore.exceptions import ClientError
from CloudwatchLogAlert import CloudwatchLogger
session = botocore.session.get_session()

logging.basicConfig(level=logging.DEBUG)
logger=logging.getLogger(__name__)


def lambda_handler(event, context):
    #create alerter instance
    alerter=CloudwatchLogger()
    
    logger.setLevel(logging.DEBUG)
    eventname = event['detail']['eventName']
    sourceip = event['detail']['sourceIPAddress']
    user = event['detail']['userIdentity']['type']
    
    logger.debug("Event is --- %s" %event)
    logger.debug("Context is --- %s" %context)
    logger.debug("Event Name is--- %s" %eventname)
    logger.debug("User Name is -- %s" %user)
    
    client = boto3.client('iam')
    snsclient = boto3.client('sns')
    response = client.list_account_aliases()
    logger.debug("List Account Alias response --- %s" %response)
    

    
    try:
        if not response['AccountAliases']:
            accntAliase = (boto3.client('sts').get_caller_identity()['Account'])
            logger.info("Account Aliase is not defined. Account ID is %s" %accntAliase)
        else:
            accntAliase = response['AccountAliases'][0]
            logger.info("Account Aliase is : %s" %accntAliase)
    
    except ClientError as e:
        logger.error("Clien Error occured")
    

    # Send alert to Cloudwatch log
    message="Root login detected from IP "+sourceip + "\n\n## Event Details\n"+json.dumps(event)
    subject="Root console login detected in account "+accntAliase
    
    logMessage = {
        "awsid": context.invoked_function_arn.split(":")[4],
        "region": os.environ['AWS_DEFAULT_REGION'],
        "subject": subject,
        "message": message,
        "sentBy": context.invoked_function_arn
      };
    
    alerter.logmessage(logMessage)
    