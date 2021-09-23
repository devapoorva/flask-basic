from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    name = "apoorv vardhman"
    abc = "this is Apoorv <strong>Vardhman</strong>"
    return render_template('index.html',name = name,abc = abc)

@app.route("/about-us")
def aboutUs():
    return render_template("about.html")

@app.route("/user/<name>")
def user(name):
    user_loggined = True
    return render_template('login.html',user_loggined=user_loggined)
    # letters = list(name)
    # users = ['Apoorv','Rahul','Rohit','Ayush']
    # return render_template('user.html',user_name = name,letters =letters,users = users)

if __name__ == "__main__":
    app.run(debug=True)


