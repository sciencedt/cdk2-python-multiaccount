from aws_cdk import (Stack, aws_codecommit as codecommit)
import aws_cdk as cdk
from aws_cdk.pipelines import CodePipeline, ShellStep, CodePipelineSource
from constructs import Construct

from multiaccount_deployment.multiaccount_deployment_stack import AccountSpecificDeploymentStage


class MultiAccountDeploymentStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        code_repo = codecommit.Repository.from_repository_name(self, "ExistingRepo",
                                                               repository_name="multiaccount-deployment")
        pipeline = CodePipeline(self, "Pipeline", cross_account_keys=True, pipeline_name="MultiaccountPipeline",
                                synth=ShellStep("Synth",
                                                input=CodePipelineSource.code_commit(
                                                    code_repo,
                                                    'master'),
                                                commands=[
                                                    "npm i -g aws-cdk",
                                                    "python -m pip install -r requirements.txt",
                                                    "cdk synth"]))
        pipeline.add_stage(AccountSpecificDeploymentStage(self, 'dev', env=cdk.Environment(account='1111111111111',
                                                                                           region='us-east-1')))
        pipeline.add_stage(AccountSpecificDeploymentStage(self, 'preprod', env=cdk.Environment(account='222222222222',
                                                                                               region='us-east-1')))
