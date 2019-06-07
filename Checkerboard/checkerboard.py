from flask import Flask, render_template # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')
def square_8():
    return render_template("index.html", x = 8, y = 8)
# app.run(debug=True) should be the very last statement! 
@app.route('/4')
def _8_by_x():
    return render_template("index.html",x = 8, y = 4)
@app.route('/<int:x>/<int:y>')
def x_by_y(x,y):
    return render_template("index.html",x = x, y = y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def xy_color(x,y,color1,color2):
    return render_template("index.html",x=x,y=y,color1 = color1, color2 = color2)
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
