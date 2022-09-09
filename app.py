from flask import Flask,render_template,url_for


# instantiate flask class
app = Flask(__name__)

@app.route('/')
def home():
    name = "Joseph"
    todo =['eat','sleep','code']
    return render_template('index.html',name=name,todo=todo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)