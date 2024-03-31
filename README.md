URL Shortener
Description
This is a simple URL shortening application developed in Flask. It allows users to shorten URLs and redirect to the original URLs through the generated short links.

Prerequisites
Python 3.8 or higher
Redis


Makefile Targets for Flask Application

Setup
The setup target is used to set up your development environment. It creates a virtual environment, activates it, and installs the necessary dependencies specified in requirements.txt.

To use this target, run:
make setup

Test
The test target is used to run your application's test suite. It activates the virtual environment and then runs pytest to execute the tests.

To use this target, run:
make test

Run
The run target is used to run your Flask application locally. It activates the virtual environment and then starts the Flask development server using flask run.

To use this target, run:
make run
Your application will be accessible at http://localhost:5001 or the port specified.

Docker Build
The docker-build target is used to build Docker images for your application and its dependencies as defined in your docker-compose.yml file.

To use this target, run:
make docker-build

Docker Run
The docker-run target is used to start your application and its dependencies in Docker containers as defined in your docker-compose.yml file.

To use this target, run:
make docker-run

This will start your application and any services it depends on (e.g., Redis) in separate Docker containers.


Using the Shortener APIs
Shorten a URL
To shorten a URL, send a POST request to the /shorten endpoint with the URL you want to shorten.

Endpoint: /shorten
Method: POST
Request Body: url=<URL_TO_SHORTEN>

Example using curl:
curl -X POST -d "url=https://example.com" http://localhost:5001/shorten

Response:
The response will contain the shortened URL. For example:
Short URL: http://localhost:5001/abcdef

Redirect to the Original URL
To be redirected to the original URL, simply access the shortened URL in a browser or send a GET request to the shortened URL.

Endpoint: /<short_url>
Method: GET

Example using curl:
curl -L http://localhost:5001/abcdef

Response:
You will be redirected to the original URL, in this case, https://example.com.

Get Access Statistics for a Short Link
To get the number of times a short link has been accessed, send a GET request to the /stats/<short_url> endpoint with the short URL path.

Endpoint: /stats/<short_url>
Method: GET

Example using curl:
curl http://localhost:5001/stats/abcdef

Response:
If the short link exists and has been accessed, the response will contain the number of times it has been accessed. For example:
The short link abcdef has been accessed 5 times.


Notes
Make sure to replace http://localhost:5001 with the base URL of your application if it is hosted differently.
The shortened URL path (abcdef in the example) will be different for each original URL.
If you access a non-existent or expired shortened URL, you will receive a 404 response with the message "URL not found".


