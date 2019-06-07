from flask import Flask, render_template, request # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/result',methods = ['POST'])
def result():
    print("Got request Info")
    print(request.form)
    result = request.form
    return render_template("result.html",result = result)
# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
