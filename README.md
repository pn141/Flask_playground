# Flask-playground
A Flask boilerplate that lets you register your users and login to your site.

# Description
Flask-playground came to life while trying to learn Flask using Miguel Grinberg's "Flask Web Development". I would recommend this book to anyone on the same learning path. I have tried different online Flask resources; Miguel's book is by far the best.

Flask-playground follows Miguel's book up to (and including) chapter 8: "User authentication". I stopped there because the important scaffholding for a large Flask application structure is already in place; the application at this point is still generic enough to become anything and has not turned yet into the social blogging application Miguel uses as an illustration for his book. 

So while I will document what I have learned (as a work in progress), the best and most comprehensive reference to understand application structure, templates, web forms, database overview, email or user authentication is "Flask Web Development" by Miguel Grinberg.

In the meantime and on your journey to better Flask programming, feel free to experiment with Flask-playground.

# installation instructions
 **Note**: Flask-playground has been written using **Python 3.7**, make sure you have Python 3.7 or above installed before proceeding with these instructions.
 
   - Clone or download "Flask-playground"
 
 ```git clone https://github.com/pn141/Flask-playground```
 
 - Start a command line, change directory to "Flask-playground" and create a virtual virtual environment. Use this link for more information on [virtual environment](https://docs.python.org/3/library/venv.html).
**Linux note** You might have to add the 'Execute' permission to the "Flask-playground" directory or use 'sudo'.
Add Execute permission: ```chmod u +x /path/to/Flask-playground```
 
  - Linux: ```python3 -m venv``` 
  - Windows: ```python -m venv```
 
 Your directory tree should now be similar to one below:
 
 ```
 Flask-playground/
     venv/
     app/
     migrations/
     __init__.py
     config.py
     data-dev.sqlite
     data-prod.sqlite
     data-test.sqlite
     flask-playground.py
     LICENSE
     README.md
     requirements.txt
 ```
     
 - From the command line, activate the virtual environment. In the example, <venv> represents the venv directory inside Flask-playground as described above.
 
  - Linux activate venv: ```source <venv>/bin/activate```
  - Windows activate venv: ```<venv>\Scripts\activate.bat```
  
 - Make sure you are at the root of Flask-playground and install the requirements using 'pip'. 
 
 ```pip install -r requirements.txt```
 
 - Set environment variable FLASK_APP to "flask-playground.py"
 
  - Linux: ```export FLASK_APP=flask-playground.py```
  - Windows: ```set FLASK_APP=flask-playground.py```
  
  - Edit file .env and add an appropriate value at the following locations:
  
  ```
  MAIL_SERVER = '' #Enter your stmp server name
  MAIL_USERNAME =  '' #username for the mailbox that will send the email
  MAIL_PASSWORD = '' #password for the mailbox
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_SUBJECT_PREFIX = '[Flask_playground]'
  MAIL_SENDER = 'Flask-playground Admin <email address>'
  ```
  Before moving to the next step, remove the comments for the first 3 entries above and replace <email address> with a valid email address. Do not close the file yet.
  
  - Finally change the location for the dev db environment appropriately then save and close ".env". 
  
  Linux:
  ```
  # dev db environment
  DEV_DATABASE_URL = 'sqlite:///tmp//flask-playground//data-dev.sqlite'
  ```
  Windows:
  ```
  # dev db environment
  DEV_DATABASE_URL = 'sqlite:///C:\\TEMP\\flask-playground\\data-dev.sqlite'
  ```
  - Type command ```flask run``` to start the Flask application then open your internet browser and go to address `http://127.0.0.1:5000`
  
  ![image](https://user-images.githubusercontent.com/22979434/73269012-e68b1180-41d3-11ea-8ae4-48b73c4f1dc6.png)
