#JINJA 2
# jinja 2 template engine has multiple ways to peint outputs in html:
'''
1. {{  }} -> this is what we sued for results:passed/failed.
2. {%...%} -> can be used for all conditional statements, looping statememt etc
3. {#...#} -> this is for comments

'''

#BUILDINGS URL DYNAMICALLY
#Variable Rule


'''
till now we have discussed -> 
submit button in html when clicked we are redirected to a new page where we display the name.
NOW -> 1. how we can build url dynemacilly.
       2. how to use jinja2
basically -> we are getting a name as of now. we wanna achieve that when we get a name we should be able to
             redirect it to a new html page. And then i should be abke to pass this name dynamically
             to a html page wehere we can display it.

right now we are just returning this name in a new html page, but in this module with go agead and call
render_template and call an html page and in that html page we can pass this name dybnamically.
this is where we can use jinja 2.
             
'''

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

@app.route('/submit',methods=['GET','POST'])
def route():
    if request.method == 'POST':
        name = request.form['name']
        return f"hello {name}!"
    return render_template('form.html')

# 1. variable rule
'''
whenever we are passing a parameter here - like <int:sxore>, and we are assigning a rule to that variable,
like here we mentioned that it will be int only.. this is called VARIABLE RULE.
'''
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res = "passed"
    else:
        res = "failed"
    
    return render_template('result.html',results = res) 
# 2. building url dynamically : see in the above line we are assiging the results to a results variable.
#this means in the result.html the res value will be send to display with the content.


@app.route('/successresults/<int:score>')
def successresults(score):
    res = ""
    if score>=50:
        res = "passed"
    else:
        res = "failed"
    
    #just a dict datatype, key value pair.. one for score and one for results.
    exp = {
        "score":score,
        "res" : res
    }
    return render_template('result1.html',results = exp)


#trying out with if else in render template
@app.route('/ifsuccess/<int:score>')
def ifsuccess(score):
    return render_template('ifresult.html',results = score) 


if __name__=="__main__":
    app.run(debug=True)