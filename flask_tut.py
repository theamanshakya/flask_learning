from datetime import datetime
from flask import Flask,render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy

from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '8c59cb69fb8e98bcaecafed563c3aec3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(30),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=True,default='default.jpg')
    password = db.Column(db.String(60),nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    def __repr__(self):
        return f"Users('{self.username}','{self.email}','{self.image_file}','{self.password}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"




posts = [
    {
        'author' : 'Aman Shakya',
        'title' : 'Title 1' ,
        'content' : 'Lorem ipsum content 1 for the first post' ,
        'date' : 'December 22 ,2020' 
    },
    {
        'author' : 'Varun Shakya',
        'title' : 'Title 2' ,
        'content' : 'Lorem ipsum content 2 for the first post' ,
        'date' : 'December 21 ,2020' 
    },
    {
        'author' : 'Arun Shakya',
        'title' : 'Title 3' ,
        'content' : 'Lorem ipsum content of the year for the first post' ,
        'date' : 'December 22 ,2020' 
    },
    {
        'author' : 'Aman Shakya',
        'title' : 'Title 4' ,
        'content' : 'Lorem ipsum content 3 for the first post' ,
        'date' : 'December 22 ,2020' 
    },
]
@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html',posts=posts)

@app.route('/about')
def index():
    return render_template('about.html')

@app.route('/register', methods =['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.username.data}!','success')
        return redirect(url_for('hello'))
    return render_template('register.html',title='Register Page',form=form)

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'admin':
            flash(f'Login Success for {form.email.data}...','success')
            return redirect(url_for('hello'))
        else: 
            flash(f'Failed to Login. Kindly check Email and Password','danger')


    return render_template('login.html',title='Login Page',form=form)