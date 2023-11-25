# Deployment
### Forking the Project
- Follow the steps below to fork this project,:
    - Locate the hidden-gems repository: https://github.com/s-batish/hidden-gems.
    - Click the 'Fork' button at the top right of the page.
    - You should now have a copy of the repository in your own GitHub account.
### Cloning the Project
- Follow the steps below to clone this project:
    - Locate the hidden-gems repository: https://github.com/s-batish/hidden-gems
    - Click the green 'Code' button.
    - Copy the URL for the repository.
    - Open the repository and open a new terminal.
    - Change the current directory to the location that you want the cloned directory to be.
    - Type 'git clone' and paste the copied URL.
    - Press 'enter' to create the clone.
### Initial steps
- Once you have cloned the project, add all project requirements to your requirements.txt file by entering ```pip3 freeze > requirements.txt``` into the terminal.
- Then create a ```.gignore``` file and an ```env.py``` file in the root directory.
- Add the ```env.py``` file to the ```.giginore``` file to ensure that all environment variables remain hidden.
- Within the ```env.py``` file add the following environment variables:
``````
import os

os.environ["SECRET_KEY"] = "Paste in a randomly generated secret key"
os.environ["DEVELOPMENT"] = '1'
``````
- In ```settings.py``` add the following at the top below ```from pathlib import Path```:
``````
import os
if os.path.isfile('env.py'):
    import env
``````
- Also replace the insecure secret key with:
``````
SECRET_KEY = os.environ.get('SECRET_KEY')
``````
- And replace the debug line with:
``````
DEBUG = 'DEVELOPMENT' in os.environ
``````
### Creating the Database
- Log in to [ElephantSQL](https://www.elephantsql.com/) or sign up if you don't have an account already.
- Click 'Create New Instance'
- Give your plan a name, select the free plan, select the region, then click 'Review' and 'Create Instance'.
- Return to the dashboard, click on the database instance name for this project and copy the database URL.
- Add the copied database URL to the ```env.py``` file as below:
``````
os.environ["DATABASE_URL"] = "Paste in the database URL"
``````
- In ```settings.py``` replace the following with the database section:
``````
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
``````
- Also add the following underneath the import for os:
``````
import dj_database_url
``````
- Install dj_database_url and psycopg2 by entering the following into the terminal:
``````
pip3 install dj_database_url==0.5.0 psycopg2
``````
and then update your requirements.txt file by entering ```pip3 freeze > requirements.txt``` into the terminal.
- Then migrate the database models to the new database by entering:
``````
python3 manage.py migrate
``````
- Next you need to import the fixtures from the products folder. Load in the categories first and then the products:
``````
python3 manage.py loaddata categories
python3 manage.py loaddata products
``````
- Now create a superuser for the new database:
``````
 python3 manage.py createsuperuser
``````
### Heroku Deployment
- Create an account with [Heroku](https://id.heroku.com/login).
- On the Heroku dashboard, click the button that says 'New', then click 'Create new app'.
- Choose a unique name for the app.
- Select your region, then click 'Create app'.
-  Click on the 'Settings' button on the menu.
- Scroll down to the section 'Config Vars' and click 'Reveal Config Vars'.
- Add the following Config Vars:
    - DATABASE_URL: The URL from your ElephantSQL dashboard
    - SECRET_KEY: Your Secret Key
    - DISABLE_COLLECTSTATIC: 1
- Go to the 'Deploy' button on the menu at the top.
- Select GitHub as the deployment method and click the 'Connect to GitHub' button.
- Search for the repository name and then click 'Connect'.
- Scroll to the bottom of the page and either click 'Enable Automatic Deploys' in the Automatic deploys section.
- Back in the CLI install gunicorn and add it to the requirements file:
``````
pip3 install gunicorn
pip3 freeze > requirements.txt
``````
- Next create the Procfile and add the following line:
``````
web: gunicorn hidden_gems.wsgi:application
``````
In ```settings.py``` add your Heroku app name and local host to the ALLOWED_HOSTS section.
- Push to GitHub and once complete, the webiste should be available to view in Heroku.

### AWS Bucket Creation
- Login to [Amazon AWS](https://aws.amazon.com/) or create an account.
- Create a new bucket:
    - Search for S3 and create a new bucket
    - Give it a name (ideally something to match your Heroku app name)
    - Select a region
    - Under Project Ownership set ACLs enabled and Bucket owner preferred
    - Uncheck block all public access
    - Acknowledge that the bucket will be public
    - Click 'Create Bucket'
- Add some settings to the bucket:
    - In the Properties tab turn on Static website hosting
    - In index document and error document enter index.html and error.html respectively and click 'Save'
    - In the Permissions tab paste in the following CORS configuration:
    ``````
    [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
    ]
    ``````
    - In the Bucket Policy tab, click 'Policy generator'
        - The policy type is S3 Bucket Policy
        - Add * to the Principal field to allow all principals
        - Set the action as GetObject
        - Paste in the ARN from the previous page
        - Click 'Add Statement' then 'Generate Policy'
        - Copy the policy into the bucket policy editor
        - Add /* onto the end of the resource key to allow access to all resources
        - Click 'Save'
    - In the Acccess Control list click 'Edit' and enable List for Everyone (public access) and accept the warning box
- Create a user to access the bucket:
    - Search for IAM in the 'Services' and select it
    - Click 'User Groups' then create a new group
- Create the policy used to access the bucket:
    - Click 'Policies' and then 'Create policy'
    - Go to the JSON tab and select import managed policy
    - Search for 'AmazonS3FullAccess' and import it
    - Copy the ARN from the bucket policy page and paste it into the resource section as below:
    ``````
    [
        arn:aws:s3:::<your-bucket-name>",
        "arn:aws:s3:::<your-bucket-name>/*"
    ]
    ``````
    - Click 'Review policy'
    - Enter a name and description and then click 'Create policy'
- Attach the policy to the created user group:
    - Click 'User Groups' and select the group
    - On the Permissions tab open the 'Add Permissions' dropdown and click 'Attach Policies'
    - Select the policy and click 'Add Permissions' at the bottom
- Create a user to put in the group:
    - On the User's page click 'Add user' and create a user
    - Give them programatic access and select 'Next'
    - Select the user group created and then clicke 'Create user'
- Retrieve access keys:
    - Go to IAM and select 'Users'
    - Select the user for whom you wish to create a CSV file
    - Select the 'Security Credentials' tab
    - Scroll to 'Access Keys' and click 'Create access key'
    - Select 'Application running outside AWS', and click next
    - On the next screen, you can leave the 'Description tag value' blank. Click 'Create Access Key'
    - Click the 'Download .csv file' button
- Connect the S3 bucket to Django:
    - In the project CLI install the following and then freeze the requirements:
    ``````
    pip3 install boto3
    pip3 install django-storages
    pip3 freeze > requirements.txt
    ``````
    - Add the following settings to the ```settings.py``` file:
    ``````
    if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'your bucket name'
    AWS_S3_REGION_NAME = 'your region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ``````
    - In Heroku add the following Config Vars:
        - AWS_ACCESS_KEY_ID: Your AWS Access Key
        - AWS_SECRET_ACCESS_KEY: Your AWS Secret Access Key
        - USE_AWS: True
    - Also remove the DISABLE_COLLECTSTATIC variable
    - Back in the CLI create a ```custom_storages.py``` file in the root directory and add the following:
    ``````
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
        location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
        location = settings.MEDIAFILES_LOCATION
    ``````
    - Commit and push these changes
- Add the media files to S3:
    - Go to S3 and create a new folder called media
    - Inside it click 'Upload'
    - Add files and then select all of the product images
    - Click 'Next' and then under Manage public permissions select 'Grant public read access' and then click 'Upload'

### Stripe Configuration
- Log in to Stripe and under the Developers section click the 'API Keys'
- Copy the values of the Publishable key and Secret key
- Go to the Webhooks section, click 'Add endpoint', add the URL for the Heroku app followed by /checkout/wh
- Select to receive all events and then 'Add endpoint'
- Copy the webhook's signing secret
- Add these 3 keys to the ```env.py``` file:
    ``````
    os.environ["STRIPE_SECRET_KEY"] = "Stripe Secret Key"
    os.environ["STRIPE_PUBLIC_KEY"] = "Stripe Publishable Key"
    os.environ["STRIPE_WH_SECRET"] = "Webhook signing secret"
    ``````
- Add the following to the ```settings.py``` file:
    ``````
    STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
    STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
    STRIPE_WH_SECRET = os.environ.get('STRIPE_WH_SECRET')   
    ``````
- Add the following to the Heroku config vars:
    - STRIPE_PUBLIC_KEY: Stripe Secret Key
    - STRIPE_PUBLIC_KEY: Stripe Publishable Key
    - STRIPE_WH_SECRET: Webhook signing secret