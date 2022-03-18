from flask import flash, render_template,request,redirect,url_for,abort
from flask_login import login_required, current_user
from .. import db, photos
from app.main.forms import CreateProfile, LeaveForm
from . import main
from app.models import Profile, Leave, User
import os


# Views
@main.route('/')
def index():


    return render_template('index.html')


@main.route('/home')
def home():

    return render_template('home.html')

@main.route('/recruitment')
def recruitment():
    return render_template('recruitment.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/updatedashboard', methods=['GET','POST'])
@login_required
def dashboard():
    form= CreateProfile()
    if form.validate_on_submit():
        profile = Profile(fullname=form.fullname.data, position=form.position.data, job_id=form.job_id.data,department=form.department.data, awards = form.awards.data, experience=form.experience.data)
        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('.dashboard', profile=profile))

    flash('Profile Successfully Updated')
    profiles = Profile.query.all()
    
           
    return render_template('dashboard.html', form=form, profiles=profiles)

@main.route('/updatedashboard',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/leave')
@login_required
def leave():
    leave = Leave.query.all()
    return render_template('leave.html', leave=leave)

@main.route('/create_leave',methods=['GET','POST'])
@login_required
def new_leave():
    form =LeaveForm()
    if form.validate_on_submit():
        leave =Leave(category=form.category.data,content=form.content.data,author=current_user)
        db.session.add(leave)
        db.session.commit()
        flash("Your leave has been booked!",'success')
        return redirect(url_for('.leave'))
    return render_template('create_leave.html',form=form,legend='New Leave Request')

@main.route('/leave/<int:leave_id>/delete',methods=['POST','GET'])
@login_required
def delete_leave(leave_id): 
    leave = Leave.query.get_or_404(leave_id)
    if leave.author !=current_user:
        os.abort(403)
    db.session.delete(leave)
    db.session.commit()
    
    
    flash("You have cancelled your leave request",'success')
    return redirect(url_for('main.index'))

# @main.route('/dashboard')
# def dashboard():
#     '''supposed to query info '''
#     pass


# @main.route('/logout')
# def logout():
#     return render_template('index.html')



# @main.route('/user/<uname>')
# def dashboard(uname):
#     user = User.query.filter_by(username=uname).first()

#     if user is None:
#         abort(404)

#     return render_template('dashboard.html', user=user)


# @main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
# def update_dashboard(uname):
#     user = User.query.filter_by(username = uname).first()
#     if user is None:
#         abort(404)

#     form = UpdateExperience()

#     if form.validate_on_submit():
#         user.experience = form.experience.data
#         user.awards = form.awards.data


#         db.session.add(user)
#         db.session.commit()

#         return redirect(url_for('.dashboard',uname=user.username))

#     return render_template('updatedasboard.html',form =form)
