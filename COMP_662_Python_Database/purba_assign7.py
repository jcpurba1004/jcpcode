#from flask import Flask
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/view')
def view():
    rows = getview()
    return render_template("view.html", rows=rows)

if __name__ == '__main__':
   app.run()