from invoke import task
import json
import boto3
from os.path import expanduser


# assumes ENV var $KEY
@task
def enckeys(ctx):
    ctx.run("openssl aes-256-cbc -e -in ca.pem -out ca.ci -k $KEY", pty=True)
    ctx.run("openssl aes-256-cbc -e -in cert.pem -out cert.ci -k $KEY", pty=True)
    ctx.run("openssl aes-256-cbc -e -in key.pem -out key.ci -k $KEY", pty=True)
    ctx.run("openssl aes-256-cbc -e -in secrets.env -out secrets.ci -k $KEY", pty=True)