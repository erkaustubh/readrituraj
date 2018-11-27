from flask import Flask, render_template
from flask_admin import Admin
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

admin = Admin(app, name='microblog', template_mode='bootstrap3')


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)
