from crypt import methods
import re
from flask import Flask,redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = "98342poiuhkerjtwg89pu523i4tr"





#===========================================
# Main Index
#===========================================
#* ===========================================
#? RENDER FORM - /
#* ===========================================
@app.route('/')
def index():
    if "posted" in session:
        return redirect("/reset")
    return render_template("index.html")


#t- ===========================================
#? PROCESS FORM - /process
#t- ===========================================
@app.route("/process", methods=["POST"])
def process():
    for item in request.form:
        print(item)
        print(request.form[item])
        session[item] = request.form[item]
    print(f"Request.form:  {request.form}")
    print(f"Session(submit):  {session}")
    session["posted"] = True
    return redirect("/result")



#* ===========================================
#? RENDER FORM - /result
#* ===========================================
@app.route('/result')
def result():
    if "posted" not in session:
        return redirect("/reset")
    print(f"Session(result):  {session}")
    if session:
        results_dict = session
        if results_dict["mac-pc"] == "Mac":
            result_mac_pc = "Mac"
        else:
            result_mac_pc = "PC"
    session["posted"] = True
    return render_template("result.html", results_dict=results_dict, result_mac_pc=result_mac_pc)

#t- ===========================================
#? PROCESS FORM - / go-back
#t- ===========================================
@app.route('/go-back')
def go_back():
    print(session)
    return redirect("/")


@app.route("/reset")
def rest():
    session.clear()
    return redirect("/")





#! MUST BE AT THE BOTTOM ---------------
if __name__ == "__main__":
    app.run(debug=True)
