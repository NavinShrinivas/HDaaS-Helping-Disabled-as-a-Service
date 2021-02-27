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

def texttobraille(y):
   
    x=y.lower()
    code_table={'a': '1 0 0 0 0 0','b': '1 1 0 0 0 0','c': '1 0 0 1 0 0','d': '1 0 0 1 1 0','e': '1 0 0 0 1 0','f': '1 1 0 1 0 0','g': '1 1 0 1 1 0','h': '1 1 0 0 1 0', 'i': '0 1 0 1 0 0 ', 'j': '0 1 0 1 1 0', 'k': '1 0 1 0 0 0', 'l': '1 1 1 0 0 0','m': '1 0 1 1 0 0', 'n': '1 0 1 1 1 0','o': '1 0 1 0 1 0 ','p': '1 1 1 1 0 0 ','q': '1 1 1 1 1 0','r': '1 1 1 0 1 0','s': '0 1 1 1 0 0', 't': '0 1 1 1 1 0','u': '1 0 1 0 0 1','v': '1 1 1 0 0 1','w': '0 1 0 1 1 1','x': '1 0 1 1 0  1','y': '1 0 1 1 1 1','z': '1 0 1 0 1 1','#': '0 0 1 1 1 1','1': '1 0 0 0 0  0','2': '1 1 0 0 0 0','3': '1 0 0 1 0 0','4': '1 0 0 1 1 0','5': '1 0 0 0 1 0','6': '1 1 0 1 0 0','7': '1 1 0 1 1 0','8': '1 1 0 0 1 0','9': '0 1 0 1 0 0','0': '0 1 0 1 1 0',' ': '0 0 0 0 0 0',',':'0 1 0 0 0 0',';':'0 1 1 0 0 0',':':'0 1 0 0 10','.':'0 1 0 0 1 1','?':'0 1 1 0 0 1','!':'0 1 1 0 1 0','-':'0 0 1 0 0 1','and':'1 1 1 1 0 1','for':'1 1 1 1 1 1','of':'1 1 1 0 1 1','the':'0 1 1 1 0 1','with':'0 1 1 1 1 1','child':'1 0 0 0 0 1','shall':'1 0 0 1 0 1','this':'1 0 0 1 1 1','which':'1 0 0 0 1 1','out':'1 1 0 0 1 1','still':'0 0 1 1 0 0','be':'0 1 1 0 0 0','in':'0 0 1 0 1 0','was':'0 0 1 0 1 1','his':'0 1 1 0 0 1','^':'1 0 0 1 1 1','&':'0 0 1 1 0 1','$':'1 1 0 1 0 1'}
    l=list()
    h=list()
    l=x.split()
    length=len(l)
    flag=0
    while length>flag :
       f=l[flag]
       if f=='and' or f=='for' or f=='the' or f=='of' or f=='with' or f=='child' or f=='shall' or f=='this' or f=='which' or f=='out'or f=='still' or f=='be' or f=='in' or f=='was' or f=='his':
            decode=code_table[f]
            h.append(decode+" ")
       else:
          if  f=='about':
              f='ab'
          elif 'ing' in f:
              f=f.replace('ing','&')
          elif 'ed' in f:
              f=f.replace('ed','$')
          elif 'th' in f:
              f=f.replace('th','^')
          elif f=='above':
              f='abv'
          elif f=='according':
              f='ac'
          elif f=='after':
              f='af'
          elif f=='afternoon':
              f='afn'
          elif f=='afterward':
              f='afw'
          elif f=='herself':
              f='herf'
          elif f=='him':
              f='hm'
          elif f=='much':
              f='mch'
          elif f=='said':
              f='sd'
          elif f=='today':
              f='td'
          elif f=='tomorrow':
              f='tm'
          elif f=='your':
              f='yr'
          for i in f:
              decode=code_table[i]
              h.append(decode+" ")
       flag+=1
    return render_template("texttobraille.html", note=h)


if __name__=="__main__":
    app.run()
