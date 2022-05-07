#!/usr/bin/env python3
import os
from dotenv import dotenv_values

import aws_cdk as cdk

from stacks.lambda_stack import LambdaStack

props = dotenv_values(".env")

account_id = props["ACCOUNT_ID"]
region = props["REGION"]

app = cdk.App()
LambdaStack(app,
        construct_id="Lambda-Stack",
        env={'account':account_id, "region": region},
        stack_name="Lambdas-Stack",
       
    )

app.synth()
