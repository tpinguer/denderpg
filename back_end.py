from flask import Flask, render_template, redirect, url_for, request
from functools import wraps
app = Flask(__name__)

# @app.route("/login")
# def login():
#     return redirect("/index", code=302)

# Route for handling the login page logic

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Thiago' or request.form['password'] != '123':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('inicio'))
    return render_template('login.html', error=error)

@app.route("/index")
def inicio():
    return render_template('index.html')


@app.route("/historia")
def historia():
    return render_template('historia.html')


@app.route("/sobre")
def sobre():
    return render_template('sobre.html')


@app.route("/livros")
def livros():
    return render_template('livros.html')


@app.route("/personagens")
def personagens():
    return render_template('personagens.html')


if __name__ == "__main__":
    app.run()
