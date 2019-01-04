from flask import Flask, render_template, request, redirect,jsonify, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from finaldatabase_setup import Base, University, Course

#Connect to Database and create database session
engine = create_engine('sqlite:///curriculum.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()





#JSON APIs to view university Information
@app.route('/university/<int:university_id>/course/JSON')
def curriculumJSON(university_id):
    university = session.query(University).filter_by(id = university_id).one()
    courses = session.query(Course).filter_by(university_id = university_id).all()
    return jsonify(Courses=[c.serialize for c in courses])


@app.route('/university/<int:university_id>/course/<int:course_id>/JSON')
def courseJSON(university_id, course_id):
    Course_Item = session.query(Course).filter_by(id = course_id).one()
    return jsonify(Course_Item = Course_Item.serialize)

@app.route('/university/JSON')
def universitiesJSON():
    universities = session.query(University).all()
    return jsonify(universities= [u.serialize for u in universities])






#Show all universities
@app.route('/')
@app.route('/university')
def showUniversities():
	#return "This page will show all my universities"
	universities = session.query(University).order_by(asc(University.name))
	return render_template('universities.html', universities = universities)
	
	
	
	
	
#create a new university
@app.route('/university/new', methods=['GET','POST'])
def newUniversity():
	#return "This page will be for making a new university"
	if request.method == 'POST':
		newUniversity = University(name = request.form['name'])
		session.add(newUniversity)
		flash('New University %s Successfully Created' % newUniversity.name)
		session.commit()
		return redirect(url_for('showUniversities'))
	else:
		return render_template('newUniversity.html')
		

	

	
#Edit a university
@app.route('/university/<int:university_id>/edit/', methods = ['GET', 'POST'])
def editUniversity(university_id):
	#return "This page will be for editing university %s"%university_id
	editedUniversity = session.query(University).filter_by(id = university_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedUniversity.name = request.form['name']
			flash('University Successfully Edited %s' % editedUniversity.name)
			return redirect(url_for('showUniversities'))
	else:
		return render_template('editUniversity.html', university = editedUniversity)




	
#Delete a university
@app.route('/university/<int:university_id>/delete/', methods = ['GET', 'POST'])
def deleteUniversity(university_id):
	#return "This page will be for deleting university %s"%university_id
	universityToDelete = session.query(University).filter_by(id = university_id).one()
	if request.method == 'POST':
		session.delete(universityToDelete)
		flash('%s Successfully Deleted' % universityToDelete.name)
		session.commit()
		return redirect(url_for('showUniversities', university_id = university_id))
	else:
		return render_template('deleteUniversity.html',university = universityToDelete)




	
#Show a university's curriculum
@app.route('/university/<int:university_id>/')
@app.route('/university/<int:university_id>/course/')
def showCurriculum(university_id):
	#return "This page is the curriculum for university %s"%university_id
	university = session.query(University).filter_by(id = university_id).one()
	courses = session.query(Course).filter_by(university_id = university_id).all()
	return render_template('curriculum.html', courses = courses, university = university)




	
#Create a new course in the curriculum
@app.route('/university/<int:university_id>/course/new/', methods=['GET','POST'])
def newCourse(university_id):
	#return "This page is for making a new course for curriculum of university %s"%university_id
	university = session.query(University).filter_by(id = university_id).one()
	if request.method == 'POST':
		newCourse = Course(name = request.form['name'], description = request.form['description'], professor = request.form['professor'], school = request.form['school'], university_id = university_id)
		session.add(newCourse)
		session.commit()
		flash('New Course %s Successfully Created' % (newCourse.name))
		return redirect(url_for('showCurriculum', university_id = university_id))
	else:
		return render_template('newCourse.html', university_id = university_id)




	
#Edit a course in the curriculum
@app.route('/university/<int:university_id>/course/<int:course_id>/edit', methods=['GET','POST'])
def editCourse(university_id, course_id):
	#return "This page is for editing course %s"%course_id
	editedCourse = session.query(Course).filter_by(id = course_id).one()
	university = session.query(University).filter_by(id = university_id).one()
	if request.method == 'POST':
		if request.form['name']:
			editedCourse.name = request.form['name']
		if request.form['description']:
			editedCourse.description = request.form['description']
		if request.form['professor']:
			editedCourse.professor = request.form['professor']
		if request.form['school']:
			editedCourse.school = request.form['school']
		session.add(editedCourse)
		session.commit() 
		flash('Course Successfully Edited')
		return redirect(url_for('showCurriculum', university_id = university_id))
	else:
		return render_template('editCourse.html', university= university,course = editedCourse)




	
#Delete a course in the curriculum
@app.route('/university/<int:university_id>/course/<int:course_id>/delete', methods=['GET','POST'])
def deleteCourse(university_id, course_id):
	#return "This page is for deleting course %s"%course_id
	university = session.query(University).filter_by(id = university_id).one()
	courseToDelete = session.query(Course).filter_by(id = course_id).one() 
	if request.method == 'POST':
		session.delete(courseToDelete)
		session.commit()
		flash('Course Successfully Deleted')
		return redirect(url_for('showCurriculum', university_id = university_id))
	else:
		return render_template('deleteCourse.html', course = courseToDelete)



	


if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
