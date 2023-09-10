from aws_cdk import (Stack,Stage, aws_lambda as _lambda)
from constructs import Construct


class LambdaDeploymentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = _lambda.Function(self, "MyFunction",
                              runtime=_lambda.Runtime.PYTHON_3_10,
                              handler="handle.lambda_handler",
                              code=_lambda.Code.from_asset("lambda_code")
                              )


class AccountSpecificDeploymentStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_stack = LambdaDeploymentStack(self, "LambdaStack")
