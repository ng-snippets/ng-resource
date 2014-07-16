# INSTRUCTIONS #

The general assumptions are 

* Using unix based system

* nodejs installed 

* grunt-cli installed ( npm install -g grunt-cli )
* bower installed  ( npm install -g bower )
* compass installed ( gem install compass) 
* python 1.7 
* Google app engine development SDK installed 



### What is this repository for? ###

* Base Project for Yeoman+flask+GAE = (yo-gae) 


### How do I get set up? ###

* pip install -r requirements.txt -t lib 
* npm install 
* bower install 
* grunt serve
* Change appid and project name  in app.yaml
* dev_appserver.py . ( in different termnial ofcourse) 


###Deploying
 
* grunt build 
* appcfg.py update .