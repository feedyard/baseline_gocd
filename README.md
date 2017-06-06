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

#### Requirements

This is the gocd orchestration used in the baseline instance of the referenc architecture. It assumes the bootstrap_tf configurations are in place, including the EFS share used by the bootstrap docker host.


```bash
$ docker-compose up gocd-server
```
When the server becomes available, add the autoregister key to the gocd-agent docker-compose section.
```bash
$ docker-compose up gocd-agent
```

#### pipelines included while implementating baseline orchestration
```xml
<config-repos>
  <config-repo plugin=“yaml.config.plugin”>
    <git url=“https://github.com/tomzo/gocd-yaml-config-example.git” />
  </config-repo>
</config-repos>
```

