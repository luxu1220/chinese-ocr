import uuid
from service.ocr_service import ocr_image
import os

my_path = os.path.dirname(os.path.abspath(__file__))


def test_ocr_service():
    """测试 ocr 功能"""

    image_path = my_path + "test.jpeg"
    filename = str(uuid.uuid4()) + "jpeg"
    res = ocr_image(image_path, filename)
    assert '青少年' in res

# cd 到项目根目录下，执行 python -m pytest backend/tests
