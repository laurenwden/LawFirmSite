from flask_nza import app, db
from flask import render_template, request, redirect, url_for
# import forms
from flask_nza.forms import UserInfoForm, CaseForm, LoginForm
#import models
from flask_nza.models import User, Case, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/cases')
@login_required
def cases():
    cases = Case.query.all()
    return render_template("cases.html",cases=cases)

#Register Route
@app.route('/register', methods=['GET','POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        # Get Information
        username = form.username.data
        password = form.password.data
        email = form.email.data
        print("\n",username,password,email)
        # Create an instance of User
        user = User(username,email,password)
        # Open and insert into database
        db.session.add(user)
        # Save info into database
        db.session.commit()
    return render_template('register.html',form = form)

#Login
@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))

    return render_template('login.html',form = form)

#Logout
@app.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('home'))



def case_delete(case_id):
    case = Case.query.get_or_404(case_id)
    db.session.delete(case)
    db.session.commit()
    return redirect(url_for('cases'))

@app.route('/cases', methods=['GET', 'POST'])
@login_required
def case():
    case = CaseForm()
    if request.method == 'POST' and post.validate():
        title = case.title.data
        note = case.note.data
        user_id = current_user.id
        print("\n", title, note)
        case = Case(title, note, user_id)
        db.session.add(case)
        db.session.commit()
        return redirect(url_for('cases'))#clears out the form fields
    return render_template('cases.html', case=case)
  
@app.route('/cases')
@login_required
def case_detail(case_id):
    #case = Case.query.filter_by(user_id=current_user.id).first()
    case = Case.query.get_or_404(case_id)
    return render_template('case_detail.html', case = case)


@app.route('/cases/update/<int:case_id>', methods = ['GET', 'POST'])
@login_required
def case_update(case_id):
    case = Case.query.get_or_404(case_id)
    update_form = CaseForm()

    if request.method == 'POST' and update_form.validate():
        title = update_form.title.data
        note = update_form.note.data
        user_id = current_user.id
        print(title,content,user_id)

        # Update will get added to the DB
        case.title = title
        case.note = note
        case.user_id = user_id

        db.session.commit()
        return redirect(url_for('case_update', case_id = case.id))
    return render_template('case_update.html', update_form = update_form)

