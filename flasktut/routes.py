from flask import render_template,url_for,flash,redirect
from flasktut import app
from flasktut.models import User ,Post
from flasktut.forms import RegistrationForm, LoginForm

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