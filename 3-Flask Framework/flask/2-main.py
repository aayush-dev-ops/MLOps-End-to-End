'''
how we can intergrate the html file here!
'''
from flask import Flask, render_template #render_template will help to redirect the route to html.
                                         #it wokrs with jinja2 template. it will seacrch for a "templates" folder
                                         #which should be inside the some folder like we have here.

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this course. Here we learn Flask."

@app.route("/index")
def index():
    return render_template('index.html')
 
@app.route("/about") 
def about():
    return render_template('about.html')

if __name__=="__main__":
    app.run(debug=True)