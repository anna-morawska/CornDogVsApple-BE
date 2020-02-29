from flask_restplus import Resource
import os
from werkzeug.utils import secure_filename
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
            image_save_path = os.path.join(app.config['IMAGE_UPLOADS'], secure_filename(uploaded_file.filename))
            uploaded_file.save(image_save_path)
            response = classify_image.classify_image(image_save_path)

            return {'data': response}, 201
        else:
             return {'message': is_image_valid[1]}, 400

