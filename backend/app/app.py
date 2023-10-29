# IMPORTS

from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from models.db import db
from models.owner import db as owner_db
from models.school import db as school_db
from models.educator import db as educator_db
from models.student import db as student_db
from models.room import db as room_db
from models.assessment import db as assessment_db
from models.resource import db as resource_db
from models.drive import db as drive_db
from models.note import db as note_db
from config import Config
from werkzeug.security import generate_password_hash, check_password_hash

#Init

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


# ROUTES


@app.route('/')
def index():
    return render_template('index.html')

## AUTHENTICATION
### Login

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the user exists in Owners, Educators, or Students table
        owner = Owner.query.filter_by(username=username).first()
        educator = Educator.query.filter_by(username=username).first()
        student = Student.query.filter_by(username=username).first()
        
        if owner and check_password_hash(owner.password, password):
            session['user_id'] = owner.id
            return redirect(url_for('owner_dashboard'))  # Redirect to owner's dashboard
        elif educator and check_password_hash(educator.password, password):
            session['user_id'] = educator.id
            return redirect(url_for('educator_dashboard'))  # Redirect to educator's dashboard
        elif student and check_password_hash(student.password, password):
            session['user_id'] = student.id
            return redirect(url_for('student_dashboard'))  # Redirect to student's dashboard
        else:
            return 'Invalid username or password. Please try again.'

    return render_template('login.html')


### Registration
@app.route('/register/owner', methods=['GET', 'POST'])
def register_owner():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Create and add owner to the database
        new_owner = Owner(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('owner_registration.html')

@app.route('/register/educator', methods=['GET', 'POST'])
def register_educator():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Create and add educator to the database (not active until approved)
        new_educator = Educator(username=username, password=generate_password_hash(password, method='sha256'), is_active=False)
        db.session.add(new_educator)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('educator_registration.html')

@app.route('/register/student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Create and add student to the database (not active until approved)
        new_student = Student(username=username, password=generate_password_hash(password, method='sha256'), is_active=False)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('student_registration.html')

### Routes for owner to approve educator and student accounts


@app.route('/approve/educator/<int:educator_id>')
def approve_educator(educator_id):
    educator = Educator.query.get(educator_id)
    educator.is_active = True
    db.session.commit()
    return redirect(url_for('owner_dashboard'))

@app.route('/approve/student/<int:student_id>')
def approve_student(student_id):
    student = Student.query.get(student_id)
    student.is_active = True
    db.session.commit()
    return redirect(url_for('owner_dashboard'))
@app.route('/owners/create', methods=['GET', 'POST'])
def create_owner():
    if request.method == 'POST':
        # Process form data and create a new owner in the database
        return redirect(url_for('owner_list'))
    return render_template('owner_form.html')


## CRUD
#### Owners:

@app.route('/owners')
def owner_list():
    owners = Owner.query.all()
    return render_template('owner_list.html', owners=owners)

#### Educators:

@app.route('/educators')
def educator_list():
    educators = Educator.query.all()
    return render_template('educator_list.html', educators=educators)


#### Students:

@app.route('/students')
def student_list():
    students = Student.query.all()
    return render_template('student_list.html', students=students)


#### Schools:

@app.route('/schools')
def school_list():
    schools = School.query.all()
    return render_template('school_list.html', schools=schools)

@app.route('/schools/create', methods=['GET', 'POST'])
def create_school():
    if request.method == 'POST':
        # Process form data and create a new school in the database
        return redirect(url_for('school_list'))
    return render_template('school_form.html')


#### Classes:

@app.route('/room')
def room_list():
    room = room.query.all()
    return render_template('room_list.html', room=room)

@app.route('/room/create', methods=['GET', 'POST'])
def create_room():
    if request.method == 'POST':
        # Process form data and create a new room in the database
        return redirect(url_for('room_list'))
    return render_template('room_form.html')


#### Assessments:

@app.route('/assessments')
def assessment_list():
    assessments = Assessment.query.all()
    return render_template('assessment_list.html', assessments=assessments)

@app.route('/assessments/create', methods=['GET', 'POST'])
def create_assessment():
    if request.method == 'POST':
        # Process form data and create a new assessment in the database
        return redirect(url_for('assessment_list'))
    return render_template('assessment_form.html')

#### Resources:

@app.route('/resources')
def resource_list():
    resources = Resource.query.all()
    return render_template('resource_list.html', resources=resources)

@app.route('/resources/create', methods=['GET', 'POST'])
def create_resource():
    if request.method == 'POST':
        # Process form data and create a new resource in the database
        return redirect(url_for('resource_list'))
    return render_template('resource_form.html')


#### Drives:

@app.route('/drives')
def drive_list():
    drives = Drive.query.all()
    return render_template('drive_list.html', drives=drives)

@app.route('/drives/create', methods=['GET', 'POST'])
def create_drive():
    if request.method == 'POST':
        # Process form data and create a new drive in the database
        return redirect(url_for('drive_list'))
    return render_template('drive_form.html')

#### Notes:

@app.route('/notes')
def note_list():
    notes = Note.query.all()
    return render_template('note_list.html', notes=notes)

@app.route('/notes/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        # Process form data and create a new note in the database
        return redirect(url_for('note_list'))
    return render_template('note_form.html')



if __name__ == '__main__':
    app.run(debug=True)
