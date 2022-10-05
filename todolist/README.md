# Assignment 4 Essay

https://pbd22-assignment2.herokuapp.com/todolist <br>

## What is the difference between Inline, Internal, and External CSS? What are the advantages and disadvantages of each style?
Inline, Internal, and External CSS are three methods of applying CSS, categorized based on the location of the CSS code. Inline CSS is located inside an HTML tag. Internal CSS is located in the HTML file itself, in the HTML head using the style tag. External CSS utilizes a separate CSS file that is referenced in the HTML file's head. 
<br>
Inline CSS is by far the most specific method among the three, as you will add a style attribute straight in the element you're modifying without using selectors. Inline CSS is generally not used as much as the other two alternatives, but can be useful when we don't have access to external CSS files or only want to apply a style to one specific element. It is also very quick in the sense that quick fixes are generally done using inline CSS. But, it still stands that inline CSS is extremely tedious and repetitive when done solely on its own in a page.
<br>
Internal CSS is useful when the aim is to stylize one single HTML page. However, using this style when modifying multiple pages gets time-consuming very fast. Other than that, in Internal CSS, you can use class and ID selectors. Furthermore, you won't need to upload multiple files since the CSS code is embedded in the HTML file. This is a double-edged sword though, as having the CSS integrated in the HTML file will make that specific page load longer.<br>
External CSS is useful when organizing a multi-paged application; one CSS file is used by multiple pages, which reduces repetition. Other than that, the absence of CSS code in HTML files will keep the HTML code clean and structured. Despite that, external CSS also poses some cons. Relying on an external CSS file will go awry when that file is not rendered/loaded correctly, which leaves the HTML bare in the application. Also, uploading or linking multiple CSS files increases your site's overall download time (as opposed to one specific page).
<br>

## Describe the HTML5 tags that you know.
A few general HTML tags: <ol>
<li>head: section of HTML file to insert references to other files</li>
<li>title: title of page visible on the application window</li>
<li>body: main content of the HTML page</li>
<li>hyperlink: clickable reference to other pages</li>
<li>paragraph: plain and modifiable text</li>
<li>bold: to make selected text bold</li>
<li>italic: to make selected text italic</li>
<li>underline: to underline selected text</li>
<li>heading: larger text meant for headers</li>
<li>line break: break to a new line</li>
<li>image: insert images with a source</li>
<li>table: a modifiable table</li>
<li>input: asks user for input of various kinds</li>
<li>ordered list: list that has logical ordering</li>
<li>unordered list: list without logical ordering</li>
<li>form: used to collect user input and pass into other applications</li>
<li>div: divide the page into highly malleable sections</li>
</ol>

## Describe the types of CSS selectors you know.
A few general CSS selectors: <ol>
<li> star: targets every single element on the page
<li> hash: targets elements by id
<li> class: targets elements by class name
<li> type: targets elements by its HTML tag type
<li> descendant: targets the tags that belong to another tag
<li> attribute: targets elements that have the defined attribute
</ol>

## Explain how you would implement the checklist above.
Firstly, I integrated Boostrap into my todolist application by editing my base.html file's head. I did this by including multiple bootstrap links using the script tag. <br>
Then, I searched for inspiration on the Internet as to how I would style my application pages. After I found one example that stuck with me, I inspected it using a feature built in Google Chrome, and wrote that code into my login, register, create_task, and homepage. <br>
After modifying the base style to my tastes, I included a navbar by implementing a class in Bootstrap into my base.html file. I also added code that made the navbar change depending on if the user is authenticated or not. <br>
Moving on, I modified the homepage by deleting the table I used in the previous assignment and replacing it with Bootstrap Cards. Said cards have a header containing the task's date, a body containing the task's title, description, and status. It would also have 2 buttons: one that let the status be updated and another that let the task be deleted on the card's footer. <br>
Finally, I used media queries to implement responsiveness onto my application. By using the @media rule, I experimented using the inspect feature to find notable borders (width and height) of devices, and modified the page so that attributes could either fit into those borders, or would be deemed uneccessary enough to be removed. <br>
