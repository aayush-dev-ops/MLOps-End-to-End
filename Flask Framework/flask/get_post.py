'''
how we can intergrate the html file here, with get post methods!
'''
from flask import Flask, render_template,request #render_template will help to redirect the route to html.
                                #it wokrs with jinja2 template. it will seacrch for a "templates" folder
                                #which should be inside the some folder like we have here.

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this course. Here we learn Flask."

@app.route("/index",methods = ['GET'])
def index():
    return render_template('index.html')
 
@app.route("/about") 
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello {name}!"
    return render_template('form.html')

@app.route('/submit',methods=['GET','POST'])
def route():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello {name}!"
    return render_template('form.html')

if __name__=="__main__":
    app.run(debug=True)