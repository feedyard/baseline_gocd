from invoke import task
from paramiko import SSHClient, AutoAddPolicy
import os


@task
def getkeys(ctx):
    ctx.run("cp ~/.docker/machine/machines/bootstrap01/ca.pem ca.pem", pty=True)
    ctx.run("cp ~/.docker/machine/machines/bootstrap01/cert.pem cert.pem", pty=True)
    ctx.run("cp ~/.docker/machine/machines/bootstrap01/key.pem key.pem", pty=True)

@task
def stack_deploy(ctx):

    # if directory structure for gocd is not already in place, create
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(os.environ['SWARM_HOST'], username='ubuntu', key_filename='./bootstrap.pem')
    ssh.exec_command("mkdir -p /mnt/data/go/godata")
    ssh.exec_command("mkdir -p /mnt/data/go/home-dir")

    cmd = docker_remote() + "stack deploy --compose-file docker-compose.yml baseline"
    ctx.run(cmd, pty=True)

@task
def stack_rm(ctx):
    cmd = docker_remote() + "stack rm baseline"
    ctx.run(cmd, pty=True)

def docker_remote():
    return "docker --tlsverify --tlscacert=ca.pem --tlscert=cert.pem --tlskey=key.pem -H=$SWARM_HOST:2376 "