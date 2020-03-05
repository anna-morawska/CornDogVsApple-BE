from flask_restplus import Resource
import os
from werkzeug.datastructures import FileStorage
from app import api, app, classify_image, my_utils

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)


@api.route('/upload-image/')
@api.expect(upload_parser)
class Upload(Resource):
    @my_utils.limit_content_length(4 * 1024 * 1024)
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']
        is_image_valid = my_utils.validate_image(uploaded_file)

        if is_image_valid[0]:
            response = classify_image.classify_image(uploaded_file.read())
            return {'data': response}, 201
        else:
             return {'message': is_image_valid[1]}, 400

