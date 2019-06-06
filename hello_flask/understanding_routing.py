from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
def hello_world():
  return 'Hello World!'  

@app.route('/dojo')
def dojo():
  return "Dojo!"

@app.route('/say/<name>')
def hello(name):
  if(type(name) == str):
    print(name)
    return "Hi "+name+"!"
  return "Sorry! No response. Try Again."

@app.route('/repeat/<int:times>/<word>')
def repeat(times,word):
  if(type(times)==int) and(type(word)==str):
    phrase = ""
    for i in range(int(times)):
      phrase += word+"\n"
    return phrase
  return "Sorry! No response. Try Again."
# import statements, maybe some other routes
@app.route('/<anything>')
def fail(anything):
  return "Sorry! No response. Try Again."
# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
