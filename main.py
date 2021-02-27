from flask import Flask, render_template ,redirect , request
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
        txt="True : the slope is safe to climb over"
    else:
        txt="False : the slope is not safe to climb over" #adding the False and True so that any other service and strip and l[0] to see status
        print('\a')
        print('\a')
        print('\a')
    return render_template('tippoffservice.html', value=txt)


@app.route("/txt-braille/<y>")
# def message(a):  
#     return render_template('texttobraille.html', value=a)
# def checkfornext(a):
#     return render_template('inputforbraille.html',letter=a) 
def texttobraille(y):
    # if request.method == 'POST':
    #     y = str(request.form.get("data"))
    x=y.lower()
    code_table={'a': '1 0 0 0 0 0','b': '1 1 0 0 0 0','c': '1 0 0 1 0 0','d': '1 0 0 1 1 0','e': '1 0 0 0 1 0','f': '1 1 0 1 0 0','g': '1 1 0 1 1 0','h': '1 1 0 0 1 0', 'i': '0 1 0 1 0 0 ', 'j': '0 1 0 1 1 0', 'k': '1 0 1 0 0 0', 'l': '1 1 1 0 0 0','m': '1 0 1 1 0 0', 'n': '1 0 1 1 1 0','o': '1 0 1 0 1 0 ','p': '1 1 1 1 0 0 ','q': '1 1 1 1 1 0','r': '1 1 1 0 1 0','s': '0 1 1 1 0 0', 't': '0 1 1 1 1 0','u': '1 0 1 0 0 1','v': '1 1 1 0 0 1','w': '0 1 0 1 1 1','x': '1 0 1 1 0  1','y': '1 0 1 1 1 1','z': '1 0 1 0 1 1','#': '0 0 1 1 1 1','1': '1 0 0 0 0  0','2': '1 1 0 0 0 0','3': '1 0 0 1 0 0','4': '1 0 0 1 1 0','5': '1 0 0 0 1 0','6': '1 1 0 1 0 0','7': '1 1 0 1 1 0','8': '1 1 0 0 1 0','9': '0 1 0 1 0 0','0': '0 1 0 1 1 0',' ': '0 0 0 0 0 0'}
    l=list()
    for i in x :
        decode=code_table[i]
        l.append(decode+" ")
    return render_template("texttobraille.html", note=l)


if __name__=="__main__":
    app.run()
