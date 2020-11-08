# IAP

* use Identify Aware Proxy to restrict access to web app.

* IAP provides user id info to admin.

* IAP got feautre of Cypto to against Spoofing.

# Core Steps:

(1) deploy a simple (python) web page

(2) enable IAP service to restrice access to app

(3) get users id info from IAP

(4) avoid from spoofing using Crypto-Verification

# Main Cmd line

    gcloud app deploy
    
    gcloud app browse

---------

# GAE (most simplest deployment solution)

prework: study how to make app wrapped in GAE using yaml file.

step from 1

> Deployment using AGE

* 1.1, in cloud console, open the cloud shell tab, and type follwing cmd line to clone app from github.

      git clone https://github.com/googlecodelabs/user-authentication-with-iap.git
      
      cd user-authentication-with-iap
      // change to main project folder
      
      cd 1-HelloWorld
      // change from main folder to subfolder
      
      cat [file name]
      // to do edit or read the code line
      
* tips & attentions:

the main code is in main.py file, it use framework called flask, which responds requests with contents of template.

1. the template file is in templates/index.html, which shows a plain HTML.
2. the other template is in templates/privacy.html, which contains privacy policy.
3. requirements.txt lists all the libs that app uses.
4. app.yaml file tells GCP this app is wrapped in GAE.

* 1.2, deploy GAE

      gcloud app deploy
      
* 1.3, select the nearest region for App and type Y.

* 1.4, see result after deployment.

      gcloud app browse
      
      [result]
      
    ![](https://cdn.qwiklabs.com/BUrEJObysrNmE%2FqmU234RAj3kMiAvwOswH%2FAmSdJ%2FNY%3D)

# IAP

from step 2:

> restrict access using IAP

* 2.1, in cloud console, navigate to Secuity > IAP

* 2.2, enable the IAP service, then click on the tab "configure consent screen" for Oauth.

* 2.3, select "internal" for user type, and click on "create".

* 2.4, config the property of the Oauth.

 ![](https://raw.githubusercontent.com/QueenieCplusplus/IAP/main/oauth_val.png)

* 2.5, in cloud shell, disable the flexible api.

      gcloud services disable appengineflex.googleapis.com (optional)
      
* tips & attentions:

    App Engine has its standard and flexible environments which are optimized for different application architectures. Currently, when enabling IAP for App Engine, if the Flex API is enabled, GCP will look for a Flex Service Account. Your project comes with a multitude of APIs already enabled for the purpose of convenience. However, this creates a unique situation where the Flex API is enabled without a Service Account created.
    
* 2.6, return to IAP config page in cloud console, and refresh it to see blow GAE row, and select toggle button to enable the IAP service in column.

 ![](https://raw.githubusercontent.com/QueenieCplusplus/IAP/main/protect%20http%20resources.png)

    
