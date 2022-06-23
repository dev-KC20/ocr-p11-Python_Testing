# gudlift-registration

1. Why


    This is a proof of concept (POC) project to show a light-weight version of our competition booking platform. The aim is the keep things as light as possible, and use feedback from the users to iterate.

2. Getting Started

    This project uses the following technologies:

    * Python v3.x+

    * [Flask](https://flask.palletsprojects.com/en/1.1.x/)

        Whereas Django does a lot of things for us out of the box, Flask allows us to add only what we need. 
     

    * [Virtual environment](https://virtualenv.pypa.io/en/stable/installation.html)

        This ensures you'll be able to install the correct packages without interfering with Python on your machine.

        Before you begin, please ensure you have this installed globally. 


3. Installation

    - After cloning, change into the directory and type <code>virtualenv venv</code>. This will then set up a a virtual python environment within the venv directory.

    - Next, type <code>venv\Scripts\activate.bat</code> if you are on Windows or <code>source bin/activate</code> on a unix-like system. You should see that your command prompt has changed to the name of the folder. This means that you can install packages in here without affecting affecting files outside. To deactivate, type <code>deactivate</code>

    - Rather than hunting around for the packages you need, you can install in one step. Type <code>pip install -r requirements.txt</code>. This will install all the packages listed in the respective file. If you install a package, make sure others know by updating the requirements.txt file. An easy way to do this is <code>pip freeze > requirements.txt</code> or give a try to <code>pip-chill --no-chill > requirements.txt</code> ; the latter requires to <code>pip install pip-chill </code> before.

    - Flask requires that you set an environmental variable to the python file. However you do that, you'll want to set the file to be <code>server.py</code>. Check [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application) for more details.
    - on windows: 
    <code> set FLASK_APP=server.py  
    set FLASK_ENV=development</code>
    - on x-like: 
    <code> export FLASK_APP=server.py  
    export FLASK_ENV=development</code>

    - You should now be ready to test the application. In the directory, type either <code>flask run</code> or <code>python -m flask run</code>. The app should respond with an address you should be able to go to using your browser.

4. Current Setup

    The app is powered by [JSON files](https://www.tutorialspoint.com/json/json_quick_guide.htm). This is to get around having a DB until we actually need one. The main ones are:
     
    * competitions.json - list of competitions
    * clubs.json - list of clubs with relevant information. You can look here to see what email addresses the app will accept for login.

5. Testing

    As per our developer guidelines, we did consider three kind of tests :
    * unit and integration tests
    * functional tests
    * performance tests.

    The [`pytest`](https://he-arc.github.io/livre-python/pytest/index.html) testing framework has been widely used with following plugins: `pytest-flask`, `pytest-mock`. We also used `pytest-cov` to link with the hereunder coverage module.  [`selenium`](https://selenium-python.readthedocs.io/index.html) made it possible to write our functional tests using the [geckodriver](https://github.com/mozilla/geckodriver/releases) for `Firefox`.
    The perfomance testing was done with the [`Locust`](https://docs.locust.io/en/stable/index.html) an open source performance testing tool.
    

    We also like to show how well we're testing, so there's a module called 
    [coverage](https://coverage.readthedocs.io/en/coverage-5.1/) you should add to your project.

    ## How to run the test

    a. The path to the Geckdriver was not permanantly set. Therefore before any fonctional test, on the command line (Windows), run:
     <code> set PATH=%PATH%;C:\uor_path\ocr-p11-Python_Testing\tests\functional_tests\ </code>.

     b. Still for functional or performance testing, the server app shall run : 
     <code>flask run </code>. 

     c. Open a new terminal command line, be located at the root of the server app directory and type:
     <code>pytest </code> which will run unit, integration and functional tests.

     d.  To run performance tests type and follow the instructions : 
     <code>locust -f tests\performance_tests\locustfile.py</code>.
     On the web client, you will provide the number of concurrent users to test as well as the running server's url (default is `[localhost:5000](http://127.0.0.1:5000)`)

     e.  To evaluate the coverage of our tests, be located at the root of the server app directory and type : 
     <code>pytest --cov=. --cov-report html</code>. 
     It will output an html report in the `htmlcov` directory whre you would hit index.html. 


6. Credits and good reads.


    Openclassrooms and even more the  DA Python discord!

    Offical Flask et pytest readthedocs!

    Nicely written and opiniated post about TDD on [Le TDD, cet éternel incompris](https://www.synbioz.com/blog/tech/le-tdd-cet-eternel-incompris)

    [Python Programming Tutorials](https://pythonprogramming.net/flask-user-log-in-system-tutorial/) for its series on login into a Flask app.
    
    [1. Installation — Selenium Python Bindings 2 documentation](https://selenium-python.readthedocs.io/installation.html) for the geckdriver and how to use it.

    [Testing a Flask Application using pytest – Patrick's Software Blog](https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/)
