#Configuration and management cloud: ##COURSE 4 OF IT *Google IT Automation with Python Professional Certificate*

#automation at scale
**configuration management**
>managed configuration =>using a conf management system to handle all configs of devices on you nodes
## infrastructure as code
>- when all the necessary configuration to deploy and manage a node in the infrastructure 
>- is stored in version control
>
## Introduction To Puppet
> Puppet client send facts to master then it will send back rules.
> puppet ressources:
> -basic unit to model the configuration that we want to manage
> ex:
>	class {
>	file { '/etc/timezone' :	
>		ensure => file, ->ensure its a file not directory or symlink
>		content => "UTC\n", ->set file content to utc 
>		replace => true, -> content replaced if file exists already
>	}
>	}
>	
> 	when puppet agent processes ressource it will first look at which provider
>	it needs to use then passes the attributes we configured in ressource 
>	to the provider The code of each provider is in charge of making our  
>   computer reflect the state requested in the resource
>
>**Puppet Classes**
> 
>	class {
>		package{
>			ensure=>latest,
>		}
>	   file { '/etc/timezone.conf' :
>	   		ensure => 'puppet:///modules/ntp/ntp.conf', ->ensure its a file not directory or symlink
>	   		replace => true, -> content replaced if file exists already
>	   }
>	   service {
>			enable=>true,
>			ensure=>running,
>		}
>
>	}
> class for group ressources managing log files 
> |settings related to your web server | 
> email infrastructure, or even your company's firewall
>
>
>
>**updating deployement: **
> --noop parametere =>Simulating manifest evaluation without taking any actions
> rspec tests => Check the manifests for specific content
> canary environments used in testing => As a test environment to detect problems before they reach the production environment
> to check the syntax of the manifest => Run full No Operations simulations |Run rspec tests |puppet parser validate 
>
> ###types of cloud deployement:
>1.Public cloud
>2.Hybrid cloud
>3.Private cloud
>4.Multi-cloud
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>









# TOOLS 
>puppet
>chef
>ansible 
>cfengine
>##on cloud:
> amazon ec2
> microsoft azure
> google cloud platforme
>##platform specific tools:windows
>sccm
>group policy
> ##platform specific tools:linux
>




# Ressources:

    # Performance Monitor on Windows:

>	https://puppet.com/docs/puppet/latest/lang_resources.html
>	https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/
>
    # Intro to puppet
>https://puppet.com/docs/puppet/latest/lang_resources.html
>https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/

    # building blocks of configuration management
>https://en.wikipedia.org/wiki/Domain-specific_language
>http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html

    #Deploying puppet locally
>https://puppet.com/docs/puppet/latest/style_guide.html
>https://puppet.com/docs/puppetserver/latest/install_from_packages.html

    #puppet client/server with ssl certificat
>

    #Managing VMs in GCP Google Cloud Platform
>https://cloud.google.com/compute/docs/quickstart-linux
>https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template
>https://cloud.google.com/sdk/docs
    #
>
>
>
>
>
    #
> Getting started on GCP with Terraform : https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform
> Creating groups of unmanaged instances :https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances
> Official documentation is here: https://cloud.google.com/load-balancing/docs/https/
> https://geekflare.com/gcp-load-balancer/
> ###Interesting articles about hybrid setups:
> https://blog.inkubate.io/create-a-centos-7-terraform-template-for-vmware-vsphere/
> https://www.terraform.io/docs/enterprise/before-installing/reference-architecture/gcp.html
> https://www.hashicorp.com/resources/terraform-on-premises-hybrid-cloud-wayfair