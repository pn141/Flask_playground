# Flask_playground
A Flask boilerplate that lets you register your users and login to your site.

# Description
Flask_playground came to life while trying to learn Flask using Miguel Grinberg's "Flask Web Development". I would recommend this book to anyone on the same learning path. I have tried different online Flask resources; Miguel's book is by far the best.

Flask_playground follows Miguel's book up to (and including) chapter 8: "User authentication". I stopped there because the important scaffholding for a large Flask application structure is already in place; the application at this point is still generic enough to become anything and has not turned yet into the social blogging application Miguel uses as an illustration for his book. 

So while I will document what I have learned (as a work in progress), the best and most comprehensive reference to understand application structure, templates, web forms, database overview, email or user authentication is "Flask Web Development" by Miguel Grinberg.

In the meantime and on your journey to better Flask programming, feel free to experiment with Flask_playground.

# installation instructions
 **Note**: Flask_playground has been written using **Python 3.7**, make sure you have Python 3.7 or above installed before proceeding with these instructions.
 
 **Linux note** The first installation step will create directory "Flask_playground" and all its content. You might have to add the 'Execute' permission to the "Flask_playground" directory or use 'sudo' to execute some of the commands below. To add Execute permission, use the following command: ```chmod u +x /path/to/Flask_playground```
 
   1. Clone or download "Flask_playground"
 
 ```git clone https://github.com/pn141/Flask_playground```
 
   2. Start a command line, change directory to "Flask_playground" and create a virtual virtual environment. Use this link for more information on [virtual environment](https://docs.python.org/3/library/venv.html).


 
  - Linux create virtual environment venv: ```python3 -m venv venv``` 
  - Windows create virtual environment venv: ```python -m venv venv```
 
 Your directory tree should now be similar to one below:
 
 ```
 Flask_playground/
     venv/
     app/
     migrations/
     __init__.py
     config.py
     data-dev.sqlite
     data-prod.sqlite
     data-test.sqlite
     flask_playground.py
     LICENSE
     README.md
     requirements.txt
 ```   
   3. Use the following command to activate the virtual environment. 
 
  - Linux activate venv: ```source venv/bin/activate``` 
  - Windows activate venv: ```.\venv\Scripts\activate.bat```
  
   4. Install the requirements for Flask_playground using 'pip'. 
 
 ```pip install -r requirements.txt```
 
   5. Set environment variable FLASK_APP to "flask_playground.py"
 
  - Linux: ```export FLASK_APP=flask_playground.py```
  - Windows: ```set FLASK_APP=flask_layground.py```
  
   6. Edit file .env and add an appropriate value within the single quotes for the following entries:
  
  ```
  MAIL_SERVER = '' #Enter your stmp server name
  MAIL_USERNAME =  '' #username for the mailbox that will send the email
  MAIL_PASSWORD = '' #password for the mailbox
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_SUBJECT_PREFIX = '[Flask_playground]'
  MAIL_SENDER = 'Flask_playground Admin <email address>'
  ```
  The authentication process in Flask_playground is a 2 steps process where a confirmation email needs to be sent to new users registering with the application. This operation will fail unless these entries are changed. 
  Once the changes, remove the comments (that is everything including and following the # character) for the first 3 entries above and replace <email address> with a valid email address. These entries should now be similar to this:
 
   ```
  MAIL_SERVER = 'smtp.example.com'
  MAIL_USERNAME =  'mailbox_username'
  MAIL_PASSWORD = 'mailbox password'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_SUBJECT_PREFIX = '[Flask_playground]'
  MAIL_SENDER = 'Flask_playground Admin <mailbox_username@smpt.example.com>'
  ```
  
  In Flask, a secret key is used for encrypted communications with the browser. In the .env file, this is key is set to "my secret key' (```SECRET_KEY = 'my secret key'```). You can decide to leave it as it is or, if you are concerned or have more restrictive security settings, change it for a key of your choice.
  
  Do not close this file yet.
  
   7. Change the location for the "dev db environment" entry then save and close ".env". 
  
  Linux:
  ```
  # dev db environment
  DEV_DATABASE_URL = 'sqlite:///tmp//flask_playground//data-dev.sqlite'
  ```
  Windows:
  ```
  # dev db environment
  DEV_DATABASE_URL = 'sqlite:///C:\\TEMP\\flask_playground\\data-dev.sqlite'
  ```
 
  8. Finally type command ```flask run``` to start the Flask application then open your internet browser and navigate to address `http://127.0.0.1:5000`
  
  ![image](https://user-images.githubusercontent.com/22979434/73269012-e68b1180-41d3-11ea-8ae4-48b73c4f1dc6.png)
  
  **Note**  Although the project contains a sqlite database for a potential production environment, "Flask_playground" is not production ready. 
