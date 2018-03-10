    #pylint:disable=print-statement


from flask import Flask, render_template, request, redirect, session
import random,math,datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below
# our index route will handle rendering our form
@app.route('/')
def index():
    if "num" not in session:
        session["num"] = 0
    if "log" not in session:
        session['log'] = []
    session['length'] = len(session['log'])   
    return render_template("ninjagold.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        rando = math.floor(random.randrange(10,21))
        session['num'] += rando
        session['log'].append([str("Earned "+str(rando)+" gold from the farm! "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))),str("green")])
    elif request.form['building'] == 'cave':
        rando = math.floor(random.randrange(5,11))
        session['num'] += rando
        session['log'].append([str("Earned "+str(rando)+" gold from the cave! "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))),str("green")])
    elif request.form['building'] == 'house':
        rando = math.floor(random.randrange(2,6))
        session['num'] += rando
        session['log'].append([str("Earned "+str(rando)+" gold from the house! "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))),str("green")])
    elif request.form['building'] == 'casino':
        rando = math.floor(random.randrange(-50,51))
        session['num'] += rando
        if rando < 0:
            rando = abs(rando)
            session['log'].append([str("Lost "+str(rando)+" gold from the casino! Oh Noes! "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))),str("red")])
        else:
            session['log'].append([str("Won "+str(rando)+" gold from the casino! Yay! "+str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))),str("green")])
    session['length'] = len(session['log'])
    return redirect('/')
    

    
app.run(debug=True) # run our server