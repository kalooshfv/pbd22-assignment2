# Assignment 2: Essay Answers

Hyperlink: https://pbd22-assignment2.herokuapp.com/katalog/

## 1. Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the urls.py, views.py, models.py and HTML files connected each other.

REQUEST <----> URL <-----> Views <-----> Model
                                 <-----> Template
                                            
The following diagram illustrates the relations between the user and the Django framework, which applies the MVT (Model-View-Template) software pattern.

First off, MVT is a structure with 3 components, which are: <br>
  a. Models: defines the data that is stored in the database and the methods of its access <br>
  b. View: defines how models and template communicate, and is the primary logic layer of MVT <br>
  c. Template: defines how the data is served to the user and how it looks on the screen
  
Among the MVT, there is also another layer called URL (consisting of the file urls.py) that processes incoming queries from the user to the MVT structure.

The flow is as follows: <br>
  i) User inserts a request into the Django framework <br>
  ii) Request is accepted and processed by urls.py, which then directs it to views.py <br>
  iii) If the request involves acquiring from the database, views.py will call a query to models.py <br>
  iv) models.py will fetch the requested data from database and return it to views.py (return in the views function) <br>
  v) After the data-related requests are done, views.py will then redirect to the template <br>
  vi) The template will dictate how the resulted data will show up on the user's screen

## 2. Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?

Virtual environments are tools that seperates the dependencies of different projects by creating isolated environments for each project.
We use virtual environments in situations where there are multiple applications that requires different third-party installations. Without virtual environments, there is a possibility for an error to occur when one project downloads an outdated/updated version of an installation, whereas it needs an updated/outdated version.
Technically, we can still create a django web application without the use of virtual environments. But, within a practical setting where there are multiple projects inside the directory, it is always recommended to use a virtual environment.


3. Explain how did you implement the steps on point 1 to point 4 above.
