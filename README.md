
# Root Login Check

Check to look for Root login attempts



## Installation Options

- [Prerequisites](#prerequisites-for-setup)
- [Pipeline](#setup-codepipeline) - Setup a Pipeline that automatically updates when source is updated.
- [CloudFormation](#setup-using-cloudformation) - Setup dedicated Stack with CloudFormation.  Code is not auto-updated.

## Prerequisites For Setup

### Cloudtrail

By default, Root login events go to Cloudtrail in us-east-1.  Cloudtrail must be enabled in 'us-east-1' or Cloudtrail for all regions must be enabled in the region where the Root Login check is run.

### Alert Log Destination

If this project is deployed in an account that is different from the main account where the Alert System was deployed, we need to add a permission for the account to access the Destination in the main account.

  - Go to the Lambda console of the main account and in the ‘us-east-1’ region

  - Find a function called ‘SungardAS-Alerts- Permission-xxxx’ and configure the test event as below:

  ```javascript
  {
      "region": "<region name where this project is deployed>",
      "account": "<account number where this project is deployed>",
      "destinationName": "<destination name defined in main Alert System; 'alertDestination' if not changed>"
  }
  ```

  - Run Test to execute this lambda function


## Setup CodePipeline

Create a stack using 'codepipeline.yaml' using below input values

Input Parameter Values

- CloudWatchLogDestinationArn:

  Value of `CloudWatchDestinationArn` in 'Outputs' of `SungardAS-aws-services-alerts(-destination)` stack in the main account's `same region` with one where this project is deployed

- CloudWatchLogGroupName:

  Name of a Cloudwatchlog Group where this trigger sends alert messages

- GitHubPersonalAccessToken:

  `Access Token` for CodeBuild to access to the this Github repository. (See <a href="https://help.github.com/articles/creating-an-access-token-for-command-line-use/">here</a> to find how to generate the access token).

- GitHubSourceRepositoryBranch: `master`

- GitHubSourceRepositoryName: `aws-services-alerts-trigger`

- GitHubSourceRepositoryOwner: `SungardAS`

- ProjectImage: `aws/codebuild/python:2.7.12`


## Setup using CloudFormation

### Prep Lambda Code

1. Create a ZIP file of the source code files in RootActivityLambda.  The files should be in the root of the zip file.

2. Upload the file to your favorite S3 bucket



### Crate CloudFormation Stack

Create a Cloudformation stack using 'RootAPIMonitor.yaml' using below input values

Input Parameter Values

- CloudWatchLogDestinationArn:

  ARN of Cloudwatch Log in remote account where Cloudwatch log subscription will send log info.

- CloudWatchLogGroupName:

  Name of a local Cloudwatch Log Group where this trigger sends alert messages

- LambdaTimeout

  Enter a timeout value in seconds for the lambda function. Min is 3, max is 300 and default is 60.

- LambdaS3Bucket:

  Name of the S3 bucket where the lambda function is stored

- LambdaS3Key:

  Name of the S3 key of the Lambda function (include the prefix as well)






## [![Sungard Availability Services | Labs][labs-logo]][labs-github-url]

This project is maintained by the Labs group at [Sungard Availability
Services](http://sungardas.com)

GitHub: [https://sungardas.github.io](https://sungardas.github.io)

Blog:
[http://blog.sungardas.com/CTOLabs/](http://blog.sungardas.com/CTOLabs/)

[labs-github-url]: https://sungardas.github.io
[labs-logo]: https://raw.githubusercontent.com/SungardAS/repo-assets/master/images/logos/sungardas-labs-logo-small.png
[aws-services-image]: ./docs/images/logo.png?raw=true
