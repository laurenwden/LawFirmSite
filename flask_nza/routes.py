from flask_nza import app, db
from flask import render_template, request, redirect, url_for
# import forms
#from flask_nza.forms import UserInfoForm, PostForm, LoginForm
#import models
#from flask_nza.models import User, Post, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user















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
    return render_template('cases.html', post=post)