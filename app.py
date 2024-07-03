from flask import Flask, render_template, request, redirect, url_for, Response
import pandas as pd
from main import helloworld
from main2 import  helloworld2
from main3 import helloworld3
from main4 import helloworld4
app = Flask(__name__)
import os




# Load configuration based on environment
environment = os.getenv('FLASK_ENV', 'development')
if environment == 'development':
    app.config.from_object('config.development')
elif environment == 'testing':
    app.config.from_object('config.testing')
elif environment == 'production':
    app.config.from_object('config.production')



@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        call = request.form["schema"]
        if call == "employee":
            return redirect(url_for("employee"))
        elif call == "invoice":
            return redirect(url_for("invoice"))
        elif call == "cardb":
            return redirect(url_for("car"))
        elif call == "school":
            return redirect(url_for("school"))
        
    else:
        return render_template("index.html")



@app.route("/employee", methods = ["GET", "POST"])
def employee():
    if request.method == "POST":
        number = request.form["Number1"]
        params = request.form.getlist("Attribute")
        params2 = request.form.getlist("Attribute_user")
        params3 = request.form.getlist("min_salary")
        params4 = request.form.getlist("max_salary")
        params5 = request.form.getlist("start_date")
        params6 = request.form.getlist("end_date")
        helloworld(int(number), params=params, names=params2, min_salary=params3, max_salary=params4, min_date=params5, max_date=params6)

        return redirect(url_for("display_csv"))
    else:
        return render_template("dropdown35.html")

@app.route("/invoice", methods = ["GET", "POST"])
def invoice():
    if request.method == "POST":
        number = request.form["Number1"]
        params = request.form.getlist("Attribute")
        params2 = request.form.getlist("Attribute_user")

        helloworld2(int(number), params=params, names=params2)

        return redirect(url_for("display_csv"))
    else:
        return render_template("dropdown2.html")


@app.route("/car", methods = ["GET", "POST"])
def car():
    if request.method == "POST":
        number = request.form["Number1"]
        params = request.form.getlist("Attribute")
        params2 = request.form.getlist("Attribute_user")

        helloworld4(int(number), params=params, names=params2)

        return redirect(url_for("display_csv"))
    else:
        return render_template("dropdown1.html")

@app.route("/school", methods = ["GET", "POST"])
def school():
    if request.method == "POST":
        number = request.form["Number1"]
        params = request.form.getlist("Attribute")
        params2 = request.form.getlist("Attribute_user")

        helloworld3(int(number), params=params, names=params2)

        return redirect(url_for("display_csv"))
    else:
        return render_template("dropdown4.html")




@app.route("/csv", methods = ["GET", "POST"])
def display_csv():
    if request.method == "POST":
        return redirect(url_for("download"))
    else:
        df = pd.read_csv("try.csv")
        df.index = range(1,len(df)+1)
        
        df = df.head(10)

        table_html = df.to_html(classes="table table-stripped")

        return render_template('index2.html', table_html=table_html)
    

@app.route("/download")
def download():
    df = pd.read_csv("try.csv")
    # df = df.to_parquet(index=False)
    df = df.to_csv(index=False)

    # response = Response(df, mimetype='text/parquet')
    # response.headers['Content-Disposition'] = 'attachment; filename=data.parquet'


    response = Response(df, mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'

    return response

if __name__ == "__main__":
    app.run(port=8081, debug=True)