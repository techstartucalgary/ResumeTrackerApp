Instructions for setting up project on your computer:
WARNING: Things you will need to have before starting:
	- Python 3. To make sure you have it, run the following command to check:
		  		$python3 -V to check
		(if you don't have it, get it here: https://www.python.org/download/releases/3.0/)
	
	
	- Pip: the default Python package installer. To make sure you have it, run the following command:
		  		$ pip -V to check
		(if you don't have it, get it here: https://pypi.org/project/pip/)
				
	
	- NodeJS: You'll need a version 6 or plus. To make sure you have it, run the command :
				$ node -v
		(if you don't have it, get it here: https://nodejs.org/en/)
	
	
	- npm: You'll need a version 5.2 or plus. To make sure you have it, run the command :
				$ npm -v
		(if you don't have it, get it here: https://www.npmjs.com/)
				
				
	- You will need bootstrap. Get it through the following command:
				$ npm install bootstrap reactstrap axios			

	- YOU WILL NEED TO SET UP A VRITUAL ENVIRONMENT to set up Django. Read this link on setting that up:
			https://docs.python.org/3/tutorial/venv.html
	
				** OR **
				
				if you are a Mac/Linux user, you can set up the virtual environment (venv) by the following instructions:
					$ sudo apt install -y python3 -venv
					
					Then in a folder of your choice: run the following commands: 
					$ mkdir environments 
					$ cd environments
					$ python3 -m venv logrocket_env
					$ source logrocket_env/bin/activate
					
					After running these four commands, you should be able to confirm that you are in your virtual env by the following output:
						$ (logrocket_env) diogo@localhost: _
						
						
			NOW, once you are in your venv, you must get Django and the Django Rest API framework through the following commands:
					$ pip install django djangorestframework django-cors-headers
					$ pip install djangorestframework
					$ python -m pip install django-cors-headers
					
			
			Now, you must also install PYDF2 in your venv. This will be necessary for reading the files in our back-end. 
					$ pip install PyPDF2
					(read about the library here: https://pypi.org/project/PyPDF2/)



***********
Once all that is done, you can now begin to checkout the repository!
*
					
		
1. Clone the repository either through the Desktop App or by entering the following lines on your command/terminal:
		$ cd Documents (or whichever directory you choose)
		$ git clone https://github.com/armeenrn/ResumeTrackerApp


Set up the listener to the back-end by opening your terminal and entering the following instructions
note: YOU MUST BE IN YOUR VENV/VIRTUAL ENVIRONEMNT HERE. AND YOU MUST HAVE INSTALLED DJANGO, ITS MENTIONED DEPENDNCIES AND PYDF2 
	$ cd Documents (or whichever directory you cloned the repository at.)
	$ cd ResumeTrackerApp
	$ cd WorkingProject
	$ cd BackEnd
	$ cd quotes
	$ python3 manage.py runserver
	
At this point, your backend server should now be set up on your localhost:8000. 


Now, set up the front-end connection while leaving the back-end program RUNNING. 
You can open a new terminal window (doesn't have to be in virtual env), and enter the following commmands. Remember that you must have React, Node, and all the other stuff installed.
	$ cd Documents  (or whichever directory you cloned the repository at.)
	$ cd ResumeTrackerApp
	$ cd WorkingProject
	$ cd FrontEnd
	$ cd testServer
	$ cd app
	$ cd src
	$ npm start

At this point, your browser should open to to localhost:3000.
There, you will see a basic interface for uploading file.
To test this out, upload a pdf file. 
The front end will send all of the bytes of that file to our back-end program, which reads it and returns a JSON body back to the front end.
For now, I commented out the lines in our back-end that sends this JSON file, instead replacing it with a dummy JSON file. 

 

	
TASKS for Front-End Team:
Now that we got a working app set up, you can focus on implementing your design without having to worry about anything in the back-end or uploading files.
All of that will be handled for you. 
Check out the file in the path: ResumeTrackerApp/WorkingProject/FrontEnd/testServer/app/src/App.js
This is where the basic front-end program is implemented it. Check it out in order to get a feel for how it works, and how you can implement your design around it. 

	
	
TASKS for Back-End Team:
Since our front-end/back-end connection and uploading files is now handled, we can continue improving our parsing and AI programs. 
I set up a working Parser module in the path: ResumeTrackerApp/WorkingProject/BackEnd/quotes/core/Parser.py
For each of you, please send me your in progress work (don't worry if its incomplete or not yet implemented with python).
I will put everything together in the next several days, and we should have our working app completed.
From that point on, we can focus on tests and improvements (and perhaps finally implementing our machine learning!), while our front-end implements the design. 




