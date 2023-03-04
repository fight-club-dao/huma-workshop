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
        # ea_repo = ecr.Repository(self, "ea-agent-repo", repository_name="ea-agent-repo")
        #
        # ecr_image_code = aws_cdk.aws_lambda.EcrImageCode(ea_repo,
        #                                       cmd=["/evaluation_agent/main.py"],
        #                                       entrypoint=["python"],
        #                                       tag="tag",
        #                                       tag_or_digest="tagOrDigest",
        #                                       working_directory="workingDirectory"
        #                                       )
        root_dir = Path(__file__).parent.parent.parent
        ea_agent_function = Function(
            self,
            "evaluation_agent",
            runtime=aws_cdk.aws_lambda.Runtime.PYTHON_3_9,
            handler="main.handler",
            code=aws_cdk.aws_lambda.Code.from_asset(str(root_dir / "evaluation_agent.zip")),
        )

        # ea_api = aws_cdk.aws_apigateway.LambdaRestApi(self, 'ea-agent-api', handler=ea_agent_function, proxy=True)
        # items = ea_api.root.add_resource("{proxy+}")
        # items.add_method("ANY")


