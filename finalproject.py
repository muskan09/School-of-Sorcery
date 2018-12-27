from flask import Flask
app = Flask(__name__)

#Show all universities
@app.route('/')
@app.route('/university')
def showUniversities():
	return "This page will show all my universities"
	
#create a new university
@app.route('/university/new', methods=['GET', 'POST'])
def newUniversity():
	return "This page will be for making a new university"
	
#Edit a university
@app.route('/university/<int:university_id>/edit/', methods = ['GET', 'POST'])
def editUniversity(university_id):
	return "This page will be for editing university %s"%university_id
	
#Delete a university
@app.route('/university/<int:university_id>/delete/', methods = ['GET', 'POST'])
def deleteUniversity(university_id):
	return "This page will be for deleting university %s"%university_id
	
#Show a university's curriculum
@app.route('/university/<int:university_id>/')
@app.route('/university/<int:university_id>/curriculum/')
def showCurriculum(university_id):
	return "This page is the curriculum for university %s"%university_id
	
#Create a new course in the curriculum
@app.route('/university/<int:university_id>/curriculum/new/', methods=['GET','POST'])
def newCourse(university_id):
	return "This page is for making a new course for curriculum of university %s"%university_id
	
#Edit a course in the curriculum
@app.route('/university/<int:university_id>/curriculum/<int:curriculum_id>/edit', methods=['GET','POST'])
def editCourse(university_id, curriculum_id):
	return "This page is for editing course %s"%curriculum_id
	
#Delete a course in the curriculum
@app.route('/university/<int:university_id>/curriculum/<int:curriculum_id>/delete', methods=['GET','POST'])
def deleteCourse(university_id, curriculum_id):
	return "This page is for deleting course %s"%curriculum_id
	


if __name__ == '__main__':
	app.debug = True
	app.run(host = '0.0.0.0', port = 5000)
