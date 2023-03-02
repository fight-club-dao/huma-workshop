from pathlib import Path

import aws_cdk.aws_s3 as s3
import aws_cdk.aws_lambda
from aws_cdk import (
    Stack,
)
from aws_cdk.aws_lambda import Function
from constructs import Construct


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        root_dir = Path(__file__).parent.parent.parent
        Function(
            self,
            "evaluation_agent",
            runtime=aws_cdk.aws_lambda.Runtime.PYTHON_3_9,
            handler="main.handler",
            code=aws_cdk.aws_lambda.Code.from_asset(str(root_dir / "evaluation_agent.zip")),
        )
