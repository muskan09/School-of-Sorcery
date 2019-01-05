from flask import Flask, render_template, request
from flask import redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from finaldatabase_setup import Base, University, Course, User
from flask import session as login_session
import random
import string
import urllib
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(open("client_secrets.json", "r").read())["web"][
    "client_id"
]
APPLICATION_NAME = "University Curriculum App"

# Connect to Database and create database session
engine = create_engine("sqlite:///curriculum.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# JSON APIs to view university Information
@app.route("/university/<int:university_id>/course/JSON")
def curriculumJSON(university_id):
    university = session.query(University).filter_by(id=university_id).one()
    courses = (
        session.query(Course).filter_by(university_id=university_id).all()
    )
    return jsonify(Courses=[c.serialize for c in courses])


@app.route("/university/<int:university_id>/course/<int:course_id>/JSON")
def courseJSON(university_id, course_id):
    Course_Item = session.query(Course).filter_by(id=course_id).one()
    return jsonify(Course_Item=Course_Item.serialize)


@app.route("/university/JSON")
def universitiesJSON():
    universities = session.query(University).all()
    return jsonify(universities=[u.serialize for u in universities])


# Show all universities
@app.route("/")
@app.route("/university")
def showUniversities():
    # return "This page will show all my universities"
    universities = session.query(University).order_by(asc(University.name))
    if "username" not in login_session:
        return render_template(
            "public_universities.html", universities=universities
        )
    else:
        return render_template("universities.html", universities=universities)


# create a new university
@app.route("/university/new", methods=["GET", "POST"])
def newUniversity():
    # return "This page will be for making a new university"
    if "username" not in login_session:
        return redirect("/login")
    if request.method == "POST":
        newUniversity = University(
            name=request.form["name"], user_id=login_session["user_id"]
        )
        session.add(newUniversity)
        flash("New University %s Successfully Created" % newUniversity.name)
        session.commit()
        return redirect(url_for("showUniversities"))
    else:
        return render_template("newUniversity.html")


# Edit a university
@app.route("/university/<int:university_id>/edit/", methods=["GET", "POST"])
def editUniversity(university_id):
    # return "This page will be for editing university %s"%university_id
    if "username" not in login_session:
        return redirect("/login")
    editedUniversity = (
        session.query(University).filter_by(id=university_id).one()
    )
    if request.method == "POST":
        if request.form["name"]:
            editedUniversity.name = request.form["name"]
            flash("University Successfully Edited %s" % editedUniversity.name)
            return redirect(url_for("showUniversities"))
    else:
        return render_template(
            "editUniversity.html", university=editedUniversity
        )


# Delete a university
@app.route("/university/<int:university_id>/delete/", methods=["GET", "POST"])
def deleteUniversity(university_id):
    # return "This page will be for deleting university %s"%university_id
    if "username" not in login_session:
        return redirect("/login")
    universityToDelete = (
        session.query(University).filter_by(id=university_id).one()
    )
    if request.method == "POST":
        session.delete(universityToDelete)
        flash("%s Successfully Deleted" % universityToDelete.name)
        session.commit()
        return redirect(
            url_for("showUniversities", university_id=university_id)
        )
    else:
        return render_template(
            "deleteUniversity.html", university=universityToDelete
        )


# Show a university's curriculum
@app.route("/university/<int:university_id>/")
@app.route("/university/<int:university_id>/course/")
def showCurriculum(university_id):
    # return "This page is the curriculum for university %s"%university_id
    university = session.query(University).filter_by(id=university_id).one()
    courses = (
        session.query(Course).filter_by(university_id=university_id).all()
    )
    creator = getUserInfo(university.user_id)
    if "username" not in login_session:
        return render_template(
            "public_courses.html",
            categories=categories,
            items=items,
            quantity=quantity,
        )
    else:
        return render_template(
            "curriculum.html",
            courses=courses,
            university=university,
            creator=creator,
        )


# Create a new course in the curriculum
@app.route(
    "/university/<int:university_id>/course/new/", methods=["GET", "POST"]
)
def newCourse(university_id):
    if "username" not in login_session:
        return redirect("/login")
    university = session.query(University).filter_by(id=university_id).one()
    if request.method == "POST":
        newCourse = Course(
            name=request.form["name"],
            description=request.form["description"],
            professor=request.form["professor"],
            school=request.form["school"],
            university_id=university_id,
            user_id=university.user_id,
        )
        session.add(newCourse)
        session.commit()
        flash("New Course %s Successfully Created" % (newCourse.name))
        return redirect(url_for("showCurriculum", university_id=university_id))
    else:
        return render_template("newCourse.html", university_id=university_id)


# Edit a course in the curriculum
@app.route(
    "/university/<int:university_id>/course/<int:course_id>/edit",
    methods=["GET", "POST"],
)
def editCourse(university_id, course_id):
    # return "This page is for editing course %s"%course_id
    if "username" not in login_session:
        return redirect("/login")
    editedCourse = session.query(Course).filter_by(id=course_id).one()
    university = session.query(University).filter_by(id=university_id).one()
    if request.method == "POST":
        if request.form["name"]:
            editedCourse.name = request.form["name"]
        if request.form["description"]:
            editedCourse.description = request.form["description"]
        if request.form["professor"]:
            editedCourse.professor = request.form["professor"]
        if request.form["school"]:
            editedCourse.school = request.form["school"]
        session.add(editedCourse)
        session.commit()
        flash("Course Successfully Edited")
        return redirect(url_for("showCurriculum", university_id=university_id))
    else:
        return render_template(
            "editCourse.html", university=university, course=editedCourse
        )


# Delete a course in the curriculum
@app.route(
    "/university/<int:university_id>/course/<int:course_id>/delete",
    methods=["GET", "POST"],
)
def deleteCourse(university_id, course_id):
    # return "This page is for deleting course %s"%course_id
    if "username" not in login_session:
        return redirect("/login")
    university = session.query(University).filter_by(id=university_id).one()
    courseToDelete = session.query(Course).filter_by(id=course_id).one()
    if request.method == "POST":
        session.delete(courseToDelete)
        session.commit()
        flash("Course Successfully Deleted")
        return redirect(url_for("showCurriculum", university_id=university_id))
    else:
        return render_template("deleteCourse.html", course=courseToDelete)


# Create a state token to prevent request forgery
# Store it in session for later validation
# --------------------------------------
# Login Handling
# --------------------------------------
@app.route("/login")
def showLogin():
    state = "".join(
        random.choice(string.ascii_uppercase + string.digits)
        for x in range(32)
    )
    login_session["state"] = state
    return render_template("login.html", STATE=state)


# CONNECT - Google login get token
@app.route("/gconnect", methods=["POST"])
def gconnect():
    # Validate state token
    if request.args.get("state") != login_session["state"]:
        response = make_response(json.dumps("Invalid state parameter."), 401)
        response.headers["Content-Type"] = "application/json"
        return response
    # Obtain authorization code
    code = request.data
    # print(code)
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets("client_secrets.json", scope="")
        oauth_flow.redirect_uri = "postmessage"
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps("Failed to upgrade the authorization code."), 401
        )
        response.headers["Content-Type"] = "application/json"
        return response
    # Check that the access token is valid.
    access_token = credentials.access_token
    url = (
        "https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s"
        % access_token
    )
    h = httplib2.Http()
    result = json.loads(h.request(url, "GET")[1])
    print(result)
    # If there was an error in the access token info, abort.
    if result.get("error") is not None:
        response = make_response(json.dumps(result.get("error")), 500)
        response.headers["Content-Type"] = "application/json"
        return response
    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token["sub"]
    if result["user_id"] != gplus_id:
        st = "Token's user ID doesn't match given user ID."
        response = make_response(json.dumps(st), 401)
        response.headers["Content-Type"] = "application/json"
        return response
    # Verify that the access token is valid for this app.
    if result["issued_to"] != CLIENT_ID:
        stt = "Token's client ID does not match app's."
        response = make_response(json.dumps(stt), 401)
        print("Token's client ID does not match app's.")
        response.headers["Content-Type"] = "application/json"
        return response
    stored_credentials = login_session.get("credentials")
    stored_gplus_id = login_session.get("gplus_id")
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        sttt = "Current user is already connected."
        response = make_response(json.dumps(sttt), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    # Store the access token in the session for later use.
    login_session["access_token"] = credentials.access_token
    login_session["gplus_id"] = gplus_id
    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {"access_token": credentials.access_token, "alt": "json"}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()
    login_session["provider"] = "google"
    login_session["username"] = data["name"]
    login_session["picture"] = data["picture"]
    login_session["email"] = data["email"]
    # see if user exists, if not create new user
    user_id = getUserID(login_session["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session["user_id"] = user_id
    output = ""
    output += "<h1>Welcome, "
    output += login_session["username"]
    output += "!</h1>"
    output += '<img src="'
    output += login_session["picture"]
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '  # noqa
    flash("you are now logged in as %s" % login_session["username"], "success")
    print("done!")
    return output


# User helper functions


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def createUser(login_session):
    newUser = User(
        name=login_session["username"],
        email=login_session["email"],
        picture=login_session["picture"],
    )
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session["email"]).one()
    return user.id


# Func to Logout


@app.route("/gdisconnect")
def gdisconnect():
    access_token = login_session.get("access_token")
    if access_token is None:
        print "Access Token is None"
        sts = "Current user not connected."
        response = make_response(json.dumps(sts), 401)
        response.headers["Content-Type"] = "application/json"
        return response
    print "In gdisconnect access token is %s" % access_token
    print "User name is: "
    print login_session["username"]
    url = "https://accounts.google.com/o/oauth2/revoke?token=%s" % access_token
    print url
    h = httplib2.Http()
    result = h.request(url, "GET")[0]
    print "result is ", result
    if result["status"] == "200":
        del login_session["access_token"]
        del login_session["gplus_id"]
        del login_session["username"]
        del login_session["email"]
        del login_session["picture"]
        response = make_response(json.dumps("Successfully disconnected."), 200)
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        stss = "Failed to revoke token for given user."
        response = make_response(json.dumps(stss, 400))
        response.headers["Content-Type"] = "application/json"
        return response


if __name__ == "__main__":
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host="0.0.0.0", port=5000)
