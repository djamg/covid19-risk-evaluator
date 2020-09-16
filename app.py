from flask import Flask, render_template, request
import riskcalculator
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('./index.html')


@app.route('/', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        answer = riskcalculator.calculate(
            scene=int(request.form['scene'])=1, mask=int(request.form['mask'])=1, talk=int(request.form['talk'])=1, distance=int(request.form['distance'])=1)
        statement = "Risk of getting Covid-19 is " + \
            str(answer[0]) + " in a Million that is " + str(answer[1]) + "%"
        return render_template('index.html', result=statement)
    else:
        return "error"


if __name__ == '__main__':
    app.run(port=8080, debug=True)
