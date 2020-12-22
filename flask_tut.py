from flask import Flask,render_template,url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '8c59cb69fb8e98bcaecafed563c3aec3'

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

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Login Page',form=form)