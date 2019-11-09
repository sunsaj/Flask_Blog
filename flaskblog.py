from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run('0.0.0.0',5000,debug=True)
