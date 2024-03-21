from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html", name="Anupam")

@app.route('/about')
def about():
    return render_template("about.html", name="Anupam")

@app.route('/contactus')
def contact():
    return render_template("contactus.html", name="Anupam")

if __name__ == '__main__':
    app.run(debug=True)