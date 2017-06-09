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




def docker_remote(tfvars, host_name):
    key_path = expanduser("~") + '/.docker/machine/machines/{}/'.format(tfvars['bootstrap-instance-name'])
return "docker --tlsverify --tlscacert={} --tlscert={} --tlskey={} -H={} ".format(key_path + 'ca.pem',
                                                                                  key_path + 'cert.pem',
                                                                                  key_path + 'key.pem',
                                                                                  host_name + ':2376')