from flask import Flask, render_template, request
import riskcalculator
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


@app.route('/send', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        answer = riskcalculator.calculate(
            scene=int(request.form['scene']), mask=int(request.form['mask']), talk=int(request.form['talk']), distance=int(request.form['distance']))
        return "Risk of getting Covid-19 is " + str(answer[0]) + " in a million that is " + str(answer[1]) + "%"
    else:
        return "error"
