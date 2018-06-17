from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "ShaneBobMissouri"

@app.route('/')
def index():
    
    if 'count' in session:
        session['count'] +=1
    else:
        session['count'] = 1    
    return render_template("index.html", count=session['count'])

@app.route('/taketwo', methods=["POST"])
def taketwo():
    session['count'] +=2
    return render_template('index.html', count=session['count'])

@app.route('/clear', methods=['GET'])
def clearSession():
    session.clear()
    return redirect('/')

app.run(debug=True)