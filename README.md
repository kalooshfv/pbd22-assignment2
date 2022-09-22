# Assignment 3: Essay Answers

Hyperlink: https://pbd22-assignment2.herokuapp.com/mywatchlist

## 1. Explain the difference between JSON, XML, and HTML!
HTML, or Hypertext Markup Language, was developed as an alternative to the then-standard and much more strict SGML (Standardized General Markup Language), which wrapped content in tags in an effort to format the content that is to-be-displayed in an application. Despite being easier to use, HTML had less structure than SGML due to having lax rules regarding the tag system. This hurt the structuring of the product, because the less rules you have, the less structure you maintain. <br>
This led to the development of XML (Extensible Markup Language), which would attempt to address this issue by directly maintaining all the strict rules of SGML, thus also maintaining the stronger structure. However, this time, XML wouldn't worry about formatting at all; that would be left to HTML. XML would be responsible for the format of sending and receiving data that is saved seperately somewhere else, while HTML would be responsible for formatting and displaying said data. <br>
Though XML is still widely-used today, a new data delivery format called JSON (JavaScript Object Notation) became the standard as it grew in popularity due to the advancement of web application development. JSON fits better in dynamic websites, which are websites that "do" stuff instead of "show" stuff, and is also based on JavaScript, which helped in interacting fluently with programming languages. <br>
Therefore, the difference between HTML and the collective of XML and JSON is that HTML is responsible for displaying and formatting data, whereas XML and JSON is responsible for sending and receiving data. The difference between XML and JSON, on the other hand, is more complicated. <br>
XML is derived from SGML, whereas JSON is based on JavaScript. This carries many other distinctions. For one, JSON works with data types such as Boolean, String, Integer, and Null, whereas XML simply uses tags that wraps around the information, which is always a string (a start tag and an end tag is mandatory). Additionally, because JSON is not a markup language, it does not have a way to display the content, while XML does. Another one would be that JSON supports the use of arrays (native to JavaScript), while XML does not. Other differences which are not that noticeable would be that XML tends to be larger file-size-wise, and JSON tends to be less secure.<br>

## 2. Explain why we need the data delivery in implementing a platform.
Most applications of the modern day regularly fetches data from a source separate from the application or device itself, and delivers it to the user based on a request the user punched in. That data is stored in a separate location because it is impractical to store a virtually endless amount of raw data in each device that runs the application; most of the time, a server is used to do that. Thus, the concept of data delivery, which is the method and formatting used to deliver data from one location to the next, is born. <br>
Conclusively, data delivery is necessary in implementing a platform because it is integral to the running of an application. It fetches data, be it a web page, statistics, graphics, or others, and delivers it to the user to be displayed in a way that that data dictates. An application would need it because the alternative is attaching the data straight onto the application itself instead of storing it somewhere else, which has many drawbacks and is simply illogical to do. <br>

## 3. Explain how you can implement the checklists above.
Creating a new app was simple enough. I ran "python manage.py startapp mywatchlist" on the command prompt, on the directory of my locally stored repository. From there, I wrote a "urls.py" file onto the app that added the mywatchlist URL path so it can be accessed through http://localhost:8000/mywatchlist. <br>
I then added a class item "WatchlistItem" in the models file of the app, with attributes: watched, title, rating, release date, and review. <br>
After that, I made a json file inside of a folder "fixtures" that contained the raw data for that webpage, which are 10 movies that I personally know of. Each movie has an entry for each attribute. That JSON file would be accompanied by an HTML file contained in a folder "templates" that dictated how the page would look. <br>
Then, to fulfill the checklist regarding implementing HTML, JSON, and XML together, I also added multiple functions in "views.py" that allowed the data to be represented via XML and JSON, both by ID and not by ID. The functions would then also be added in the 'urlpatterns' list found in "urls.py" so it can be accessed via links like http://localhost:8000/mywatchlist/xml. <br>
Finally, I edited the Procfile of the app so it would migrate the models and load the JSON file when I deployed it. Then, I pushed the local repository onto GitHub, and it automatically deployed onto Heroku.
 
## 4. Access three URLs in point 6 using Postman, take screenshots, and add them to README.md.
![Assignment 3 Postman HTML](https://user-images.githubusercontent.com/96697117/191449984-c8a696a2-7c4b-4ee6-af45-2a165abc922c.png)
![Assignment 3 Postman JSON](https://user-images.githubusercontent.com/96697117/191449922-113f02e9-e2df-4229-925c-2c29c984bafd.png)
![Assignment 3 Postman XML](https://user-images.githubusercontent.com/96697117/191449942-848e977c-0045-4147-a550-49fbbf8a2df4.png)


