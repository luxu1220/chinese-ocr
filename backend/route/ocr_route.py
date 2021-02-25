from flask_restplus import Namespace
from flask_restplus import Resource
from werkzeug.datastructures import FileStorage
from service.ocr_service import ocr_image
from service.file_service import save_file
from constants import ALLOW_FILE_TYPES

ocr_app_api = Namespace('ocr', path='/ocr', description='ocr route')

ocr_post_parser = ocr_app_api.parser()

ocr_post_parser.add_argument('file',
                             type=FileStorage,
                             required=True,
                             location='files',
                             help='只支持 png、jpg 或 jpeg 格式的图片文件')


@ocr_app_api.route('')
class SendVerificationCode(Resource):
    def get(self):
        """
        测试
        :return:
        """
        return 'test_ok'

    @ocr_app_api.expect(ocr_post_parser)
    def post(self):
        """ 通过 ocr 技术识别图片中的文字并返回
        """
        args = ocr_post_parser.parse_args()
        file = args['file']
        # 判断文件类型是否符合要求
        if not file.filename.lower().endswith(ALLOW_FILE_TYPES):
            return {"success": False,
                    "reason": '图片格式错误，png 或 jpg 格式的图片文件'}, 400
        # 利用 uuid 为图片生成新文件名，并保存为文件
        filename = save_file(file)
        # 识别图片，并将识别结果存入数据库
        res = ocr_image(file, filename)
        return {"success": res}, 200
