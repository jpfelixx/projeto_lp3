from flask import Flask , render_template
app2 = Flask("My application2")

@app2.route("/termos-de-uso")
def termosdeuso(): 
    return render_template("termosdeuso.html")

app2.run()