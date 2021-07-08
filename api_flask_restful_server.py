from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

class CustomerAPI(Resource):
    def get(self):
        pass



@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,LOCK,UNLOCK')
  return response
  
if __name__ == '__main__':
    #server1 = pywsgi.WSGIServer(('0.0.0.0', 81), app)
    #server1.serve_forever()
    pass
