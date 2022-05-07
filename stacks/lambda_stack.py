from aws_cdk import (
    Stack,
    aws_lambda,
    Duration,
    aws_iam
)
from constructs import Construct

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        lambda_name = "lambda_function_testing"
        
        lambda_execution_role = aws_iam.Role(
            self, 
            id="lambda_function_testing",
            assumed_by=aws_iam.ServicePrincipal(service="lambda.amazonaws.com"),
            description="This role will be used by the lambda_function_testing for XXXX Permissions (S3,CloudWatch, ETC...)",
            role_name=lambda_name,
            #permissions_boundary=
            inline_policies={
                "AWSBasicExecutionRoles":
                    aws_iam.PolicyDocument(
                        statements=[
                            aws_iam.PolicyStatement(
                                actions=["logs:CreateLogGroup"],
                                resources=["arn:aws:logs:us-east-1:139988404192:*"]
                            ),
                            aws_iam.PolicyStatement(
                                actions=["logs:CreateLogStream","logs:PutLogEvents"],
                                resources=["arn:aws:logs:us-east-1:139988404192:log-group:/aws/lambda/"+lambda_name+":*"]
                            ),
                            
                        ]
                    ),   
                
            }
        )
        
        lambda_function = aws_lambda.Function(
            self, 
            id = "lambda_testing",
            code=aws_lambda.Code.from_asset('./lambdas'),
            handler="lambda_testing.handler",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            function_name ="lambda_testing",
            timeout= Duration.seconds(30),
            role= lambda_execution_role,
        )
        
        lambda_function.add_function_url(auth_type=aws_lambda.FunctionUrlAuthType.NONE)
        