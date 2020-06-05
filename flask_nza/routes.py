from flask_nza import app, db
from flask import render_template, request, redirect, url_for
# import forms
#from flask_nza.forms import UserInfoForm, PostForm, LoginForm
#import models
#from flask_nza.models import User, Post, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user

@app.route('/cases/delete/<int:post_id>', methods=['POST'])
@login_required
def case_delete(case_id):
    case = Case.query.get_or_404(case_id)
    db.session.delete(case)
    db.session.commit()
    return redirect(url_for('cases'))