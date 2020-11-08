# IAP

* use Identify Aware Proxy to restrict access to web app.

* IAP provides user id info to admin.

* IAP got feautre of Cypto to against Spoofing.

# Core Steps:

(1) deploy a simple (python) web page

(2) enable IAP service to restrice access to app

(3) get users id info from IAP

(4) avoid from spoofing using Crypto-Verification

---------

# GAE (most simplest deployment solution)

step from 1

> Deployment using AGE

* 1.1, in cloud console, open the cloud shell tab, and type follwing cmd line to clone app from github.

      git clone https://github.com/googlecodelabs/user-authentication-with-iap.git
      
      cd user-authentication-with-iap
      // change to main project folder
      
      cd 1-HelloWorld
      // change from main folder to subfolder
      
* tips & attentions:

the main code is in main.py file, it use framework called flask, which responds requests with contents of template.

1. the template file is in templates/index.html, which shows a plain HTML.
2. the other template is in templates/privacy.html, which contains privacy policy.
3. requirements.txt lists all the libs that app uses.
4. app.yaml file tells GCP this app is wrapped in GAE.




