# The Dundie - Take home test

**Author**: Nick Komarnicki  
A simple blog site created using Django/Python for the backend and frontend.

### Completed Functionality
+ Home page with a list view of posts

+ Detail view of a post(click to view)

+ Ability to create a new post  
   - Utilizes a simple html form. Grabs author data from db to give the users the option to choose an author.  
   - Title and description are input fields while created date will be auto-generated on creation.
   
+ Editing a post

+ Posts persist utilizing the default SQLite DB.  
   - This makes use of a Post Model and an Author model.  
   - Post model - title, description, foreignkey to author, created date.  
   - Author model - name, bio, img_url

### Shortcomings
+ Code not taking enough advantage of django options  
   - Form needs to be refactored to inherit from django forms and implemented as a class.  
   - More can be done in utilizing generic views  

+ Author view for specific author not implemented.

+ No edit property on a post to show date edited or if it has been edited.

+ Overall site design relatively simplistic.

Most difficulty developing came from not knowing the Django framework or Python. The larger learning curve was implementing the front end with python coming from a javascript background. The model system with django was simple, clear and very useful. Overall found the framework to have a lot of features to make rapid devopment easier that will get better with more study.

#### Language Versions
Python 3.8.2  
Django 3.0.5