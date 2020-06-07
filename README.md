# NZA Lawfirm WebApp
This is the first project by *The Bob Marley's* using FLASK.

The original requirenments can be found [here](https://classroom.google.com/c/OTQ5OTQ1MDk1MDNa/a/MTA5MTk0MDk4MDMw/details).

## PreWork
* Brainstormed on the approach
* Agreed on 55%-55% approach (__because we gave it 110%__) join programming v. individual programming
* Schedule breaks, meals, debugging time expectations
* Created file structure together, including Procfile
* Divided tasks fairly [here](https://docs.google.com/spreadsheets/d/1FA5QScZEDUsldNLGAP9XTDDBjh1gaPlfBu0SfVeUSec/edit#gid=1414651411)
* Forked originator's repo, made local clones
* Created Heroku collaborators project the night before, as well as a shared drive folder

## Environment 
* First did a pull from the original originator's github repo
* Then: 
```
virtualenv flask_nza_env
cd Scripts 
activate
../..
pip install flask
pip install Flask-WTF
pip install Flask-SQLAlchemy
pip install Flask-Migrate
pip install Flask-Login
pip freeze
```
* After, requirenments.txt from a pip freeze
* After forks + clones, everyone had to:
```
pip install -r requirenments.txt
```

## Features
### Common Elements
Jointly created models.py, routes.py, IlovePie.py, base.html, nav.html, footer.html.

### Register/LogIn/Logout
*By Celeste B.*

Backend: `@app.route('/register', methods=['GET','POST'])` and `@app.route('/login', methods = ['GET','POST'])`
Frontend: register.html and login.html.

### Create Case
*By Lauren W.*

Backend: `@app.route('/createcases', methods=['GET', 'POST'])`
Backend: Created forms.py

### Existing Cases
*By Jack N.*

Backend: `@app.route('/existingcases')`
Frontend: existingcases.html

### Update Case Note / Case Detail
*By Jackie H.*

Backend: `@app.route('/case_detail/<int:case_id>')`, `@app.route('/cases/update/<int:case_id>', methods = ['GET', 'POST'])` and `@app.route('/logout')`
Frontend: case_detail.html and case_update.html

### Delete Case Note
*By Aaron A.*

Backend: `@app.route('/cases/delete/<int:case_id>', methods=['POST'])`
Frontend: Delete Button, Delete Button Modal

## Database
Created database and linked it to our backend with:
```
flask db init
flask db migrate -m "first migration"
flaks db upgrade
```

## Deployment
- First we installed the following programs:
```
pip install pillow pycopg2 gunicorn
```
- Then, connected github repo to Heroku and [deployed](https://www.youtube.com/watch?v=wx-F8Y0JXiU)

Deployed version can be found [here](https://nza-lawfirm.herokuapp.com/)