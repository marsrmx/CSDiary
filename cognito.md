# Cognito

## Amazon Cognito User Pool 

_Amazon Cognito User Pool makes it easy for developers to add sign-up and sign-in functionality to web and mobile applications. It serves as your own identity provider to maintain a user directory. It supports user registration and sign-in, as well as provisioning identity tokens for signed-in users_

Service from AWS to create user pools and to manage authentication and authorization from users.

1. Create an user pool
2. In your terminal run the next script to create a new user

`aws cognito-idp sign-up \
  --region YOUR_COGNITO_REGION \
  --client-id YOUR_COGNITO_APP_CLIENT_ID \
  --username admin@example.com \
  --password Passw0rd!`

3. After this you'll need to verify the user, you can do this with this administration command (after this command you will not see anything in the terminal, you can verify it in AWS)

`aws cognito-idp admin-confirm-sign-up \
  --region YOUR_COGNITO_REGION \
  --user-pool-id YOUR_COGNITO_USER_POOL_ID \
  --username admin@example.com`

## Amazon Cognito Federated Identities.

_Enables developers to create unique identities for your users and authenticate them with federated identity providers. With a federated identity you get, temporary, limited-privilege AWS credentials to securely access other AWS services such as DinaymoDB, S3 and API Gateway._

You create a Cognito Identity Pool that use Use Pool, Facebook, Google or another identity provider and once the user is authenticated via our User Pool (in this case), the Identity Pool will attach an IAM Role to the user. You have to define a policy for this IAM Role to grant access to the S3 bucket and your API, or whatever you need. 

## Difference between them
