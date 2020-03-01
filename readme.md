# is-it-healthy BE

This is the backend part of the is-it-healthy app. The frontend can be found [here](https://github.com/kamilkulik/CornDogVsApple-FE)

is-it-healthy is a pair programming project which goal is to create a mobile app which, based on a picture, can differentiate and classify healthy and unhealthy food.

At the moment backend app has a form of a REST API developed with Python Flask-RESTPlus framework, which provides a description of an API compatible with OpenAPI Specification. The complete API documentation can be found [here](https://corn-dog-vs-apple-be.herokuapp.com/)

The main job of the backend app is to process incoming POST requests. The first step is to label the image - for vision detection, the app uses Cloud Vision API.
The next step is to integrate Natural Language Processing algorithm to classify an image as healthy or unhealthy and send back the label as a response to FE.

### Installing

To run the the containerized version of the backend app, first, you need to create .env file in the project's root directory. Base it off of .env-example file and filled it with our own authentication credentials to your application, Then run:

```js
docker-compose up
```

and navigate to http://0.0.0.0:5000/
