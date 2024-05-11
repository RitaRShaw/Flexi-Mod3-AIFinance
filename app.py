from flask import Flask, render_template,request

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))


@app.route("/main",methods=["GET","POST"])
def main():
    r=request.form.get("q")
    return(render_template("main.html",r=r))
    ## the r=r one from the back end r and another from front end the html

@app.route("/prediction",methods=["GET","POST"])
def prediction():
    return(render_template("prediction.html"))

@app.route("/dbs_price",methods=["GET","POST"])
def dbs_price():
    q=float(request.form.get("q"))
    return(render_template("dbs_price.html",r=(q*-50.6)+90.2))

if __name__=="__main__":
    app.run()

## == magic reserved for some only
