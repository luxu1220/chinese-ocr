from flask_restplus import Api
from .ocr_route import ocr_app_api

api = Api(
    title='简单的中文 OCR API',
    version='1.0',
    description='识别并返回图片(支持jpg, jpeg, png格式)中的文本',
)

api.add_namespace(ocr_app_api)
