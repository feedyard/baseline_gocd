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


