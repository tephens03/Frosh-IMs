from flask import Flask, render_template, request,redirect

app = Flask(__name__)

SPORTS = ["Basketball", "Soccer", "Hockey"]
REGISTANTS = {}

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("failure.html",error_message="Missing name")

    selected_sports = request.form.getlist("sport")
    if not selected_sports:
        return render_template("failure.html",error_message="Missing sport")
    for sport in selected_sports:
        if sport not in SPORTS:
            return render_template("failure.html",error_message="Missing sport")

    REGISTANTS[name]=selected_sports
    # return render_template("success.html", name=name, sports=selected_sports)
    return redirect("/registants")

@app.route("/registants")
def registants():
    print(REGISTANTS)
    return render_template("registants.html",registants=REGISTANTS)

if __name__ == "__main__":
    app.run(debug=True)
