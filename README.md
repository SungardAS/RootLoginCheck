
# Alert Trigger

Alert Trigger that Sends alert messages to Alert Kinesis Stream

![aws-services][aws-services-image]

## Prerequisites For Setup

If this project is deployed in an account that is different from the main account where the Alert System was deployed, we need to add a permission for the account to access the Destination in the main account.

  - Go to the Lambda console of the main account and ‘us-east-1’ region

  - Find a function called ‘SungardAS-Alerts- Permission-xxxx’ and configure the test event as below:

  ```javascript
  {
      "region": "<region name where this project is deployed>",
      "account": "<account number where this project is deployed>",
      "destinationName": "<destination name defined in main Alert System; 'alertDestination' if not changed>"
  }
  ```

  - Run Test to execute this lambda function


## How To Setup a CodePipeline

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

- ProjectImage: `aws/codebuild/nodejs:4.3.2`

## [![Sungard Availability Services | Labs][labs-logo]][labs-github-url]

This project is maintained by the Labs group at [Sungard Availability
Services](http://sungardas.com)

GitHub: [https://sungardas.github.io](https://sungardas.github.io)

Blog:
[http://blog.sungardas.com/CTOLabs/](http://blog.sungardas.com/CTOLabs/)

[labs-github-url]: https://sungardas.github.io
[labs-logo]: https://raw.githubusercontent.com/SungardAS/repo-assets/master/images/logos/sungardas-labs-logo-small.png
[aws-services-image]: ./docs/images/logo.png?raw=true
