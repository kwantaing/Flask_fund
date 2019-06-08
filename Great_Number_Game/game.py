from flask import Flask, render_template, request,redirect
import random
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/guess', methods=["post"])
def guess():
    number = random.randint(1,101)
    form = request.form
    guess = form["guess"]
    print(number,guess)
    if(int(guess) == number):
        response = str(number)+" was the Number!"
        color = "green"
    elif(int(guess)<number):
        response = "Too low!"
        color = "red"
    else:
        response = "Too high!"
        color = "red"
    return render_template("result.html",number=number,guess=guess, color=color, response= response)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
