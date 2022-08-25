#!/usr/bin/env python3

import aws_cdk as cdk

from newapp.newapp_stack import NewappStack


app = cdk.App()
NewappStack(app, "newapp")

app.synth()
