# plusminus
Simple Flask-based Python web server for testing different hosting options ...

plusminus.py imports both the pprint and flask modules and creates a Flask instance (i.e. a web server) named app.  In the last lines of the script, app is configured to run on the host machine’s internal IP address using TCP port 1234 when the script is executed.  app accepts input as either parameters embedded in the URL of a HTTP GET or JSON included in a HTTP POST.  The method handling the GET adds and subtracts 3 to the base number passed in the URL and returns both numbers.  The method handling the POST adds and subtracts a number received as a parameter in the POST and performs the same addition and subtraction of that number to the base number also passed in the same JSON payload - and returns the results in JSON format.

plusminusClienty.py is a simple client to pass parameters as JSON in a HTTP POST to the server.
