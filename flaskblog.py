from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'af2673b2f2f6c7adbc5bde2455bcdb94'

posts = [
    {
        'author':'Corey',
        'title':'Blog 1',
        'content':'Post content for Blog 1',
        'date_posted': 'April 21, 2018'
    },
    {
        'author':'Saj',
        'title':'Blog 2',
        'content':'Post content for Blog 2',
        'date_posted': 'April 22, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts = posts)


@app.route("/about")
def about():
    return render_template('about.html',title = 'About')


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='Register', form = form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'Password':
            flash('You have been logged in!','success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html',title='Login', form = form)

if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)
