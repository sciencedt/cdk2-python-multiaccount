#!/usr/bin/env python3
import os

import aws_cdk as cdk

from multiaccount_deployment.multiaccount_pipeline_stack import MultiAccountDeploymentStack

app = cdk.App()
MultiAccountDeploymentStack(app, "MultiaccountDeploymentStack-dev", env=cdk.Environment(account='680143075966', region='us-east-1'))

app.synth()
