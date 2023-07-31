# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Azaan" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
def father_flask():
    return "This is the father WebPage"


# define the route to mother webpage
def mother_flask():
    return "This is the Mother WebPage"



# define the route to friends webpage
def friends_flask():
    return "This is the Friends WebPage"


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
