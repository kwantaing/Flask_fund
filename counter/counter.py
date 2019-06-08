from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def home():
    if not "visits" in session:
        session["visits"] = 0
    if not "clicks" in session:
        session["clicks"] = 0
    session["visits"]+=1
    return render_template("index.html")

@app.route("/click")
def click():
    session["clicks"]+=1
    return redirect("/")
    
@app.route('/destroy_session')
def clear():
    session.clear()		# clears all keys
    return redirect("/")

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
