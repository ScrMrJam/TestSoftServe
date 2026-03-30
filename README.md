## Setup

pip install -r requirements.txt

## Run

uvicorn app.main:app --reload

## Test

pytest

## Example

GET http://localhost:8000/urlinfo/1/bad.com/malware


## Answers:

1) The size of the URL list could grow infinitely. How might you scale this beyond the memory capacity of the system? 

Use Redis as a cache and buffer layer so that workers can process data in a controlled manner towards DynamoDB,
thus enabling control and scalability of storage without data loss.

2) Assume that the number of requests will exceed the capacity of a single system, describe how might you solve this, and how might this change if you have to distribute this workload to an additional region, such as Europe. 

I would use Route 53 to route traffic between regions, ELB to distribute within the region, and EKS to scale the processing pods.

3)  What are some strategies you might use to update the service with new URLs? Updates may be as much as 5 thousand URLs a day with updates arriving every 10 minutes.

I would use SQS to decouple and buffer the URLs to be processed, and Lambda as workers that consume the queue,
allowing thousands of URLs to be processed in a controlled manner, avoiding overloading the system.

4) You’re woken up at 3am, what are some of the things you’ll look for in the app?

I would use CloudWatch for early detection and automatic responses to potential cases, such as failed login attempts (100 in 5 min), or during nighttime hours (1AM-6AM) as examples.

5) Does that change anything you’ve done in the app?

I would change it a little, I would apply X-Ray for example to maintain a better mapping of what happens in the application

6) What are some considerations for the lifecycle of the app?

I use IAM to apply least privilege to each service and WAF to protect endpoints from malicious traffic and limit requests, all automated and versioned with CDK/CloudFormation to maintain security and control throughout the application lifecycle.

7) You need to deploy a new version of this application. What would you do?

I would deploy the new version using CodeDeploy blue/green with two Target Groups behind the ALB, manage traffic with canary deployments on the ALB ingress, and ensure quality through automated unit tests before the full rollout.