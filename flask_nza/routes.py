from flask_nza import app, db
from flask import render_template, request, redirect, url_for
# import forms
#from flask_nza.forms import UserInfoForm, PostForm, LoginForm
#import models
#from flask_nza.models import User, Post, check_password_hash

from flask_login import login_required,login_user,current_user,logout_user


@app.route('/cases/delete/<int:case_id>', methods=['POST'])
@login_required
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
  
@app.route('/cases/<int:case_id>')
@login_required
def case_detail(case_id):
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