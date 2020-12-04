# Amazon Web Services Basics

## IAM

IAM are users that you can create with specific permissions to access your resources in AWS.

__IAM = Identity and Access Management (IAM)__ 

With IAM you can control authentication (who is who) and authorization (who can do what).

### Basics

Root user - the first user you create, has your email address and password as root credentials. It has ALL the permissions, access, everything, it's invincible, an avenger, be afraid.

IAM user - a name and a password to sing in into the AWS Managment Console. Who's access keys can be used with the API or CLI. 

_CLI_ - console

By default the IAM Users don't have access to anything until you give them some permissions, for that you need to create a __policy__. 

#### IAM Policy

RULES. The end.

Defines what the user is allowed or denied to do with the AWS resources. For this you have 4 different options:

1. Managed policy, nice, pre-defined and provided by AWS.
2. Inline policy, custom, created by hand.
3. Added to a group, basic idea is that the group has the policies. 
4. Cloning permissions from an existing IAM user.

### IAM Role

It's an _identity_ with permission policies that __does not have any credentials__ associated with it. The role can be taken by anyone who needs it, it can be a Lambda function for example.

Roles can be apply to users as well.

### IAM Group

Is a collection of IAM Users. You can put permissions to a group and add or remove users from it. 

## ARN

__ARN = Amazon Resources Names__ 

It's a globally unique identifier for an individuals AWS resources. 

What are they used for?
- Communication
- IAM policy

## AWS CLI


## Where we left ...
https://serverless-stack.com/chapters/render-the-note-form.html