from flask import Flask , request ,render_template
app=Flask(__name__)

@app.route("/txt-braille",methods=['GET','POST'])
# def message(a):  
#     return render_template('texttobraille.html', value=a)
# def checkfornext(a):
#     return render_template('inputforbraille.html',letter=a) 
def texttobraille():
    if request.method == 'POST':
        y = str(request.form.get("data"))
        x=y.lower()
        code_table={'a': '1 0 0 0 0 0','b': '1 1 0 0 0 0','c': '1 0 0 1 0 0','d': '1 0 0 1 1 0','e': '1 0 0 0 1 0','f': '1 1 0 1 0 0','g': '1 1 0 1 1 0','h': '1 1 0 0 1 0', 'i': '0 1 0 1 0 0 ', 'j': '0 1 0 1 1 0', 'k': '1 0 1 0 0 0', 'l': '1 1 1 0 0 0','m': '1 0 1 1 0 0', 'n': '1 0 1 1 1 0','o': '1 0 1 0 1 0 ','p': '1 1 1 1 0 0 ','q': '1 1 1 1 1 0','r': '1 1 1 0 1 0','s': '0 1 1 1 0 0', 't': '0 1 1 1 1 0','u': '1 0 1 0 0 1','v': '1 1 1 0 0 1','w': '0 1 0 1 1 1','x': '1 0 1 1 0  1','y': '1 0 1 1 1 1','z': '1 0 1 0 1 1','#': '0 0 1 1 1 1','1': '1 0 0 0 0  0','2': '1 1 0 0 0 0','3': '1 0 0 1 0 0','4': '1 0 0 1 1 0','5': '1 0 0 0 1 0','6': '1 1 0 1 0 0','7': '1 1 0 1 1 0','8': '1 1 0 0 1 0','9': '0 1 0 1 0 0','0': '0 1 0 1 1 0',' ': '0 0 0 0 0 0'}
        l=list()
        for i in x :
            decode=code_table[i]
            l.append(decode+" ")
        return render_template("texttobraille.html", note=l)
    return render_template("texttobraille.html", note="")



if __name__=="__main__":
    app.run()