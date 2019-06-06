from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play/<int:x>/<color>')
def play_x_color(x,color):
    return render_template('box_color.html',times = x,color = color)  # Return the string 'Hello World!' as a response

@app.route('/play/<int:x>')
def play_x(x):
    return render_template('box_color.html',times=x)  # Return the string 'Hello World!' as a response

@app.route('/play')
def play():
    return render_template('box_color.html',times = 3, color = "blue")  # Return the string 'Hello World!' as a response

@app.route('/<anything>')
def default(anything):
    return "Sorry, Page not found"
@app.route('/')
def home():
    return "Home Page"
# app.run(debug=True) should be the very last statement! 

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
