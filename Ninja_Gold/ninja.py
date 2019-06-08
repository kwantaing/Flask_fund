from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def home():
    if not "gold" in session:
        session["gold"] = 100
    return render_template('home.html')

@app.route('/farm')
def farm():
    rand_gold = random.randint(10,21)
    print(session["gold"])
    print("gained",rand_gold)
    session["gold"]+=rand_gold
    print(session["gold"])
    return redirect('/')

@app.route('/cave')
def cave():
    rand_gold = random.randint(5,11)
    print(session["gold"])
    print("gained",rand_gold)
    session["gold"]+=rand_gold
    print(session["gold"])
    return redirect('/')

@app.route('/house')
def house():
    rand_gold = random.randint(2,6)
    print(session["gold"])
    print("gained",rand_gold)
    session["gold"]+=rand_gold
    print(session["gold"])
    return redirect('/')

@app.route('/casino')
def casino():
    rand_gold = random.randint(-50,51)
    print(session["gold"])
    if(rand_gold > 0):
        print("Lucky! You gained ",rand_gold)
    elif(rand_gold<0):
        print("Unlucky! You lost: ",rand_gold)
    else:
        print("You won and lost nothing")
    session["gold"]+=rand_gold
    print(session["gold"])
    log = print_activity(rand_gold,"casino")
    return redirect('/')
@app.route('/clear')
def clear():
    session.clear()		# clears all keys
    return redirect('/')

def print_activity(rand_gold,task):
    if not "log" in session:
        session["log"] = []
    if(rand_gold > 0 ):
        activity = f"gained {rand_gold} Gold from {task}"
        session["log"].append(activity)
    elif(rand_gold<0):
        activity = f"lost {rand_gold} from casino. Unlucky!"
        session["log"].append(activity)
    print(session['log'])
    return session['log']

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
