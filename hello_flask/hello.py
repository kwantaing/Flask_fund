from flask import Flask, render_template, request# Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')
def hello_world():
    return render_template('index.html',phrase = "hello", times= 5)  # Return the string 'Hello World!' as a response
# import statements, maybe some other routes
    
@app.route('/success')
def success():
  return "success"
    

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/party')
def pass_list():
    parties = [
      "birthday","Anniversary","Saturday"
    ]
    return render_template("array.html",parties = parties)

@app.route('/party/<partytype>')
def party_type(partytype):
    print(partytype)
    return (f"Welcome to the {partytype} party!")
# app.run(debug=True) should be the very last statement! 
@app.route("/doit",methods=["POST"])
def do_it():
  #dictionary fo rpost request: request.form
  print(request)
  print(request.form["alias"])
  return f"Welcome to the party {request.form['alias']}"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
