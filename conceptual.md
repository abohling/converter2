### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

	### The biggest differences are that javascript is for used for things on screen and python is for data to be passed.
	-
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
	### value using dict.item()
	### get the key by using list comprehension- loop til you hit the key
	 
	-
- What is a unit test?

	### A unit test tests the smallest testable part of the application

	-
- What is an integration test?

	### test in which different parts are tested combined

	-
- What is the role of web application framework, like Flask?

	### Flask provides tools, libraries and technologies to build a web app. It allows you to keep adding third party libraries to provide functionality
	
	-
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
  ### depending on the the size of information needed to passasd. But if you want to follow api design path params are used to identify a specific source  while the query parameters are use to sort/filter

	-
- How do you collect data from a URL placeholder parameter using Flask?

	### app.route('/urlsomething/<dataid>')
	
	-
- How do you collect data from the query string using Flask?

	### set the ids and = request.args['ids'] to get the information
	
	-

- How do you collect data from the body of the request using Flask?

	### data = request.form.get('something')

	-
- What is a cookie and what kinds of things are they commonly used for?

	### cookies is data that is stored, it is information that is passed from the user to the server and back.
	
	-
- What is the session object in Flask?

	### is used to track session data which is stored as a dictionary object. The dictionary contains key value pairs of the session variables.
	
	-
- What does Flask's `jsonify()` do?

	### it converts a json(js object notation) output into a response ojbect with json type