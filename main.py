from flask import Flask, render_template ,redirect

app=Flask(__name__)
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/")
def index():
    return redirect('/home')

if __name__=="__main__":
    app.run()



# @app.route("/tippoffservice/<x>/<y>")
# def tippoffservice(x,y):
    