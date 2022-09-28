# Assignment 4 Essay

https://pbd22-assignment2.herokuapp.com/todolist <br>

## What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element? 
A CSRF (Cross-Site Request Forgery) token is a tag that Django has implemented to prevent a CSRF attack, which is when an attacker induces users to perform actions that they do not intend to perform. This happens when the user is in a session in a certain Web application, and by doing something unaware (e.g. clicking a malicious URL), a request gets crafted and sent into the Web application without the user's consent. Since the application cannot differentiate if the request is actually made by the user or otherwise, the unauthorized request gets executed.  <br>
The tag solves this issue by generating a token on the server side when rendering a page, and cross-checks this token for any requests that come back in. If a request doesn't contain the generated token, then the request does not get executed. <br>
Without this code snippet or tag, then our application would be vulnurable to CSRF attacks, and might be liable for a breach of personal data, unsanctioned transactions, or other unsavory events. <br>
  
## Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.
It is possible to generate a form manually. The generator {{ form.as_table }} uses a python file that contains a form object as reference to display onto an HTML file, but it is also possible to directly create a form on the HTML file itself. <br>
You would generally use the form tag, followed by an attribute "method" which has a value of between "POST" and "GET". The main difference between the two is that GET carries request parameter appended in URL string while POST carries request parameter in message body. Then, you would use the input tag, along with its various attributes to give a slot where the user can input their data into the form. Additionally, you could use the label tag to specify what is expected on each input. A few frequently used examples of input types would be: radio, checkbox, text, button, date, email, file, and URL. <br>

## Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.

## Explain how you implement the checklist above.
