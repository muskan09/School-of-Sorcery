# UNIVERSITY CURRICULUM CATALOGUE
----
## ABOUT
> An application that provides a list of universities within a variety of courses as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.

### Prerequisite knowledge:

  * [Python](https://www.python.org/)

  * [SQL](https://www.postgresql.org/)
  
  * [HTML](https://www.w3schools.com/html/)

  * [CSS](https://www.w3schools.com/css/)
   
  * [JS](https://www.w3schools.com/js/)
  
### Additional Tools used:

  * [Vagrant](https://www.vagrantup.com/)

  * [VirtualBox](https://www.virtualbox.org/)

  * [Git commands](https://in.udacity.com/course/how-to-use-git-and-github--ud775-india)

  * [PEP 8](https://www.python.org/dev/peps/pep-0008/)

  * [OAUTH](https://console.developers.google.com/apis)
  
  * [FLASK](http://flask.pocoo.org/)

  * [REQUESTS](http://docs.python-requests.org/en/master/)

## SETUP
> Install virtual machine
> Install vagrant
> Clone the [fullstack-nanodegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)

> Clone the [university app](https://github.com/muskan09/UniversityApp) and add it to the vagrant dir.

## STEPS TO RUN THE APPLICATION
> Launch the Vagrant VM from inside the vagrant folder with: 
`vagrant up`

> Then access the shell with:       
`vagrant ssh`

> Then move inside the universityapp directory:
`cd /vagrant/UniversityApp`

> Then run the application(note, this uses python2):
`python finalproject.py`

> After the last command you are able to browse the application at this URL:        
`http://localhost:5000/`

> Optional Steps-:
    
> to run the finaldatabase_setup.py
`python3 finaldatabase_setup.py`

> to populate the database  
Clone the [lotsofcourses.py file](https://github.com/muskan09/LotsOfCourses)
then run 
`python3 finallotsofcourses.py`

## SOFTWARE DEVELOPMENT LIFE CYCLE
###### Agile methodlogy was followed in this project.
### ITERATIONS:-
#### 1: MOCKUPS
> Mockups and routes decided.

#### 2: ROUTING
> finalproject.py created and routes added and tested.

#### 3: TEMPLATES & FORMS
> All html added in /templates dir and necessary code added to finalproject.py and all html pages are tested.

#### 4: DATABASE CREATION & POPULATION
> finaldatabase_setup.py created and populated with [finallotsofcourses.py](https://github.com/muskan09/LotsOfCourses).
 
> Checked curriculum.db using sqlitebrowser.

#### 5: CRUD FUNCTIONALITY
> All the functions for creating, reading, updating,deleting university and courses added. And then finalproject.py is tested with all the functionalities.

####  6: API ENDPOINTS
> Then all the JSON routes were created and app was tested.

#### 7: STYLING & MESSAGE FLASHING
> Then message flashing was added in finalproject.py and all html pages in /templates dir.

> Css was added in the /static dir.


#### 8. AUTHENTICATION AND AUTHORIZATION
> Oauth was integrated with the app and tested and necessary changes were made to the code.

##### NOTE: all the pictures of the app are available in the pictures directory.

----
## CONCEPTS LEARNT

> how to develop a RESTful web application using the Python framework Flask along with implementing third-party OAuth authentication. 

> How to properly use the various HTTP methods available to you and how these methods relate to CRUD (create, read, update and delete) operations.

> Efficiently interacting with data which is the backbone upon which performant web applications are built

> Properly implementing authentication mechanisms and appropriately mapping HTTP methods to CRUD operations are core features of a properly secured web application

----
### LICENSE
 MIT ©2019 Muskan Kalsi
