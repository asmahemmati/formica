---
title: Remove
weight: 100
---

# `formica remove`

Through the remove command you can remove an existing stack.

After starting to remove the stack it will follow the stack events until the removal is finshed. In case the removal failed it will exit with a non-zero exit status.

## Example

```
root@07e549506145:/app/docs/examples/s3-bucket# formica remove --stack formica-examples-stack
Removing Stack and waiting for it to be removed, ...
+------------------------------+--------------------------+--------------------------------+--------------------------------+----------------------------------------------------+
|          Timestamp           |          Status          |              Type              |           Logical ID           |                   Status reason                    |
+------------------------------+--------------------------+--------------------------------+--------------------------------+----------------------------------------------------+
2017-02-16 19:14:59 UTC+0000   DELETE_IN_PROGRESS         AWS::CloudFormation::Stack       formica-examples-stack           User Initiated
2017-02-16 19:15:30 UTC+0000   DELETE_IN_PROGRESS         AWS::S3::Bucket                  DeploymentBucket
2017-02-16 19:15:30 UTC+0000   DELETE_IN_PROGRESS         AWS::S3::Bucket                  DeploymentBucket2
2017-02-16 19:15:51 UTC+0000   DELETE_COMPLETE            AWS::S3::Bucket                  DeploymentBucket2
2017-02-16 19:15:51 UTC+0000   DELETE_COMPLETE            AWS::S3::Bucket                  DeploymentBucket
2017-02-16 19:15:52 UTC+0000   DELETE_COMPLETE            AWS::CloudFormation::Stack       formica-examples-stack
```

## Options

| Option                                             | Description  |
| -------------------------------------------------- | ------------ |
| --stack (-s) STACK                                 | The stack you want to create. |
| --profile PROFILE                                  | The AWS profile to use. |
| --region REGION                                    | The AWS region to use. |
| --config-file (-c) CONFIG_FILE                     | Set the config files to use |
| --role-arn ROLE_ARN                                | Set a separate role ARN to pass to the stack |