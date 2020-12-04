# Serverless Framework

_WTF is a Framework?_

Is a platform for developing software applications that provides a foundation for developing. It can include a code libraries, a compiler, etc. 

Serverles Framework helps you develop and deploy your AWS Lambda functions (see below), along with the infraestructure resources they required.

It's really cool because it manage your infraestructure as well  as your code.

## Concepts 

### Functions

Is an AWS Lambda function. It's an independent unit of deployment, like a microservice (code in the cloud that does just one thing). 

__Pro tip__ the serverless framework is optimized to handle a lot of units of functions and it's recommended to have functions doing just one thing. 

### Events

Anything that triggers an AWS Lambda Function (call to an endpoint of an API, etc). The Framework will automatically create any infraestructure neccesary for the defined event and configure the AWS Lambda Function to listen to it.

### Resources

AWS infraestructure components which your Functions use. (Things that eventually you will understand how they work).

### Services

Is the Framework's unit of organization, _translation pls_, __the project configuration file__ 

`serverless.yml serverless.json serverless.js`

Here you define the Functions, the Event that trigger them and the Resources you need for those Functions.

### Plugins 

A file where you extend or overwrite the functionality of the Framework using plugins.

## AWS Lambda

Most popular serverless computing services out there. It's a provider for the Serverless Framework.

AWS Lambda executes functions and self-contained applications created by the users in an efficient and flexible manner.

__Serverless__ computing, aka Function as a Service, FaaS, is about not needing to maintain your own servers to run these functions. All the infraestructure will be take care by Amazon, _such a nice company_, in this specific case. 

So, how it works, each function has its own container and everytime you execute that funciton it creates a new container (or an instance of that container) that it's execute on a multi-tenant cluster of machines managed by AWS. To each function's container is allocated its necessary RAM and CPU capacity, after the processing is done, the amount of time that it took is multiplied by the RAM allocated at the beggining and Amazon just charge you for that.  

Cool things:

* No need to worry about infraestructure
* Same function can be executed concurrently
*  Good fit for deploying highly scalable cloud computing solutions.
* Pay per use
* Automatic scalling
* Integration with other AWS products.

Not so cool things:

* You don't know how the infraestructure is working.
* Cold start time, is a latency from 5 to 10 seconds
* Limitations:

1. Execution time/run time (up to 15 min)
2. Memory range from 128 MB to 3,008MB with a 64MB step
3. Code package size up to 250 MB (50MB zippped)
4. Concurrency limited to 1,000
5. Payload limited size of 10 MB.
6. Not always cost-effective
7. Limited number of supported runtimes

### Serverless applications

For creating this type of applications you need 
1. A computing service
2. A database service
3. an HTTP gateway service

Lambda fills the primary role of the compute service and with other AWS you can create a serverless application.

Some examples of typical scenarios are:
* Individual task run for a short time
* Each task is self-contained (generally)
* There is a large difference between the lowest and highest levels in the workload of the application.

Common use cases that fit these criteria are:
* Scalable APIs
* Data processing
* Task automation

## References and Resources

* Serverless Framework - https://serverless.com/framework/docs/providers/aws/guide/intro/
* AWS Lambda - https://serverless.com/aws-lambda/
