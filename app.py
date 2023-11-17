## Flask App Routing

from flask import Flask,render_template,request,redirect,url_for,jsonify

## create a simple flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to my Flask page"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the Index page"

@app.route('/success/<int:score>')
def success(score):
    return "The person has passed and and the score is: "+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has fail and and the score is: "+ str(score)

@app.route('/form', methods=["GET", "POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else: 
        maths = float(request.form['math'])
        science = float(request.form['science'])
        english = float(request.form['english'])

        average_marks=(maths+science+english)/3

        # return render_template('form.html',score=average_marks)

        res=""
        if average_marks>=50:
            res='success'
        else:
            res='fail'
        return redirect(url_for(res,score=average_marks))

@app.route('/api', methods=['POST'])
def calculate_sum():
    try:
        data = request.get_json()
        a_val = float(data['a'])
        b_val = float(data['b'])
        result = a_val + b_val
        return jsonify({"result": result})
    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)


