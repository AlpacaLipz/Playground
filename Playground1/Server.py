# with help of peyton

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def alpaca():
    return render_template('index.html', times = 3, color = "blue")

@app.route('/play/<int:times>')
def alpacino(times):
    return render_template('index.html', times = times, color = "black")

@app.route('/play/<int:times>/<string:color>')
def alpaquio(times, color):
    return render_template('index.html', times = times, color = color)


if __name__=="__main__":
    app.run(debug=True, port=4200)