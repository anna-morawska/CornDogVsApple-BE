import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask 
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app)

a_contributor = api.model('contributor', {'name' : fields.String('contributor name')})

contributors = []
authors = [{'name' : 'Anna Morawska'}, {'name' : 'Kamil Kulik'}]
contributors.extend(authors)

@api.route('/contributor')
class Contributor(Resource):
    def get(self):
        return contributors

    @api.expect(a_contributor)
    def post(self):
        contributors.append(api.payload)
        return {'result' : 'Contributor added'}, 201 

if __name__ == '__main__':
    app.run(debug=True)