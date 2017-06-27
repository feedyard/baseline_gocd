# baseline_gocd
Bootstrap GoCD orchestration for baseline management

Deploys GoCD-server and a single agent to the bootstrap dockerhost.

Includes plugins and pipeline configuration to manage the following baseline pipelines:
* Baseline Terraform pipeline
* Auth0 integration/rules deploy
* Baseline Dashboard deploy
* Nevergreen radiator deploy
* Management-GO-Swarm (pipeline to manage the Test and Prod, 3-node swarm upon which will run the go-instance that is used to deploy the various ‘management’ components of the ref arch.)
* Management-GO server/agents (there is a Test and Prod ‘environment’ of the gocd service used to deploy/manage the various ‘management’ components, e.g., the mgmt-k8 cluster.)



### implementation

Note: currently in development. Deploy directly to bootstrap node via command line and then update gocd configuration to let instances manage themselves.
For testing purposes this repo just manages the server/agent image stack updates and another repo is used to manage gocd-server configuration.


#### Requirements

Assumes the bootstrap_tf configurations are in place, including the EFS share used by the bootstrap docker host.<br/>

Within the local directory the required *.pem keys are available, and ENV variables are defined: listed below

For ssh access to bootstrap01 node
bootstrap.pem (or whatever name is used for this key-pair)

For accessing secure docker daemon:
ca.pem
cert.pem
key.pem
