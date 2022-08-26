from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_dynamodb as dynamodb_cdk,
    aws_lambda as lambda_cdk,
    aws_apigateway as apigateway_cdk,
)


class NewappStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create DynamoDB table
        customer_table_cdk = dynamodb_cdk.Table(self, "customer_table_cdk",
                partition_key=dynamodb_cdk.Attribute(name="customer_id", 
                type=dynamodb_cdk.AttributeType.STRING))
        
        # Create Lambda function
        customer_lambda_cdk = lambda_cdk.Function(self, "customer_lambda_cdk",
                code=lambda_cdk.Code.from_asset("./lambda/"),
                handler="customer_lambda.lambda_handler",
                runtime=lambda_cdk.Runtime.PYTHON_3_9)
        customer_lambda_cdk.add_environment("TABLE_NAME", customer_table_cdk.table_name)


        # Grant Lambda permission to access DynamoDB
        customer_table_cdk.grant_write_data(customer_lambda_cdk)

        # Create ApiGateway, point to above Lambda
        customer_api_cdk = apigateway_cdk.LambdaRestApi(self, "customer_api_cdk",
                        handler = customer_lambda_cdk,
                        proxy = False)
        customer_api_resource = customer_api_cdk.root.add_resource('add_customer')
        customer_api_resource.add_method("POST")


