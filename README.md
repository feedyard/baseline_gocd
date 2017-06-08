# baseline_gocd
Bootstrap GoCD orchestration for baseline management

Deploys GoCD-server and a single agent to the bootstrap dockerhost.

Includes plugins and pipeline configuration to manage the following baseline pipelines:
* baseline terraform
* lifecycle management-gocd cluster
* lifecycle management-gocd service
* Auth0 integration/rules
* Smashing Dashboard
* Nevergreen radiator


### implementation

Two methods of deploying the baseline gocd server are demonstrated below.

#### 1. Deploy via circleci

One approach to bootstrap the infrastructure is by managing the initial orchestration service via a SaaS provided orchestration tool. Circle-ci is used to demonstrate.

#### 2. deploy from workstation

Alternatively, you can choose to manage the baseline gocd deployment from the command line. An Invoke tasks file is provided to demonstrate. 


#### Requirements

Assumes the bootstrap_tf configurations are in place, including the EFS share used by the bootstrap docker host. Reference assumes use of quay.io registry.

Within the local directory the required *.pem keys are available, and ENV variables are defined: listed below

For circleci, the secrets are encrypted via openssl aes-256-cbc and the decryption key has been added to the circleci project.

For access secure docker daemon:
ca.pem
cert.pem
key.pem

quay.io docker registry:
QUAY_USER
QUAY_TOKEN

#### pipelines included while implementating baseline orchestration
```xml
<config-repos>
  <config-repo plugin=“yaml.config.plugin”>
    <git url=“https://github.com/tomzo/gocd-yaml-config-example.git” />
  </config-repo>
</config-repos>
```

sudo docker push quay.io/feedyard/repository:tag
