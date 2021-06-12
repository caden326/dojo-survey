from flask import Flask, render_template, request
app = Flask(__name__)




@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users', methods=['POST'])
def create_user():
    nameform = request.form['name']
    locationform = request.form['location']
    languageform = request.form['language']
    commentform = request.form['comments']

    return render_template("show.html", name=nameform, location=locationform, language=languageform, comments=commentform)



if __name__ == "__main__":
    app.run(debug=True)

