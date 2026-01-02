'''
SKELETON: steps of creating the flask->
1. sabse pehle import karo flask
2. class ko call karo and usme apna poora __name__ wala part daalo.
3. if condition which will define the entry point.
'''

#1.
from flask import Flask 
'''
here we are creating the instance of the flask  class.
which will be our WGSI (web server gateway interface) application.

this app = Flask()... it creates an insstance of a flask class wihich will
be our WGSI application that will furtehr interactw ith the web server itself.
'''

#wsgi application
#2.
app = Flask(__name__)

'''
now here we are giving a parameter which we cannot skip. MUST.
THIS IS THE ENTRY POINT OF ANY .py FILE
When we run he entire codebase... 
poore codebase me se yahi wala file dhoonda jayga and isi ko run kiya jayga. 
this is the starting point. neech wala line...
'''
@app.route("/") #/ means the home page.whenever i visit my homepage which is "/", it should return welcome.
def welcome():
    return "welcome to this flask cou    rse. I am doing good till now. This should be an amazing code/Testing smth,abcd"
 
@app.route("/endure")
def aayush():
    return "i am doing tp."

#3.
if __name__ == "__main__":
    app.run(debug = True)



