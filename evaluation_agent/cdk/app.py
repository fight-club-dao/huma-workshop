#!/usr/bin/env python3
import os

import aws_cdk as cdk

from stacks.cdk_stack import CdkStack

app = cdk.App()
CdkStack(app, "EvaluationAgentStack")

app.synth()
