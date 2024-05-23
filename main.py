from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)

def process_id(x):
    if len(x) < 7 or not x.isdigit():
        return "Please enter a valid ID number."

    y = x[0:4]
    z = x[4:7]
    q = int(z)

    gender = "Female" if q > 500 else "Male"
    if q > 500:
        q -= 500

    if q <= 0 or q > 366:
        return "Invalid day of year in ID number."

    k = "Your Birthday Is On"

    if q <= 31:
        month = "January"
        day = q
    elif q <= 60:
        month = "February"
        day = q - 31
    elif q <= 91:
        month = "March"
        day = q - 60
    elif q <= 121:
        month = "April"
        day = q - 91
    elif q <= 152:
        month = "May"
        day = q - 121
    elif q <= 182:
        month = "June"
        day = q - 152
    elif q <= 213:
        month = "July"
        day = q - 182
    elif q <= 244:
        month = "August"
        day = q - 213
    elif q <= 274:
        month = "September"
        day = q - 244
    elif q <= 305:
        month = "October"
        day = q - 274
    elif q <= 335:
        month = "November"
        day = q - 305
    else:
        month = "December"
        day = q - 335

    result = f"{k} {y}, {month} {day}\nGender: {gender}"
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        id_number = request.form['id_number']
        result = process_id(id_number)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
