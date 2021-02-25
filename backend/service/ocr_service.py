from ocr_core.model import text_predict
from business.db_business import save_result
from PIL import Image
import numpy as np


def ocr_image(image, image_name):
    """
    识别图片中的文字并将结果存储到数据库中
    :param image:图片
    :param image_name:图片名称
    :return:识别结果
    """
    image = Image.open(image)
    image = np.array(image)
    # 对图片进行 ocr
    res = text_predict(image)
    # 解析识别结果
    res = ','.join([i["text"] for i in res])
    # 保存到数据库
    save_result(image_name, res)
    return res
