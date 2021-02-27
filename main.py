from flask import Flask, render_template ,redirect
import math


app=Flask(__name__)
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/")
def index():
    return redirect('/home')


@app.route("/tippoffservice/<int:x>/<int:y>/<typ>")
def tippoffservice(x,y,typ):
    hypo=math.sqrt((math.pow(x,2)+math.pow(y,2)))
    wa_safeval=1/12
    a_safeval=2/12
    current_ratio=x/hypo
    safe_flag=False
    if(typ=="wa" and current_ratio < wa_safeval):
        safe_flag=True
    elif(typ=="a" and current_ratio < a_safeval):
        safe_flag=True
    txt=""
    if(safe_flag==True):
        txt="the slope is safe to climb over"
    else:
        txt="the slope is not safe to climb over"
        print('\a')
    return render_template('tippoffservice.html', value=txt)


if __name__=="__main__":
    app.run()
