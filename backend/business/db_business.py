from .db_connect import Session
from entity.ocr import Ocr


def save_result(image_file_name, ocr_result):
    """
    保存识别的结果到数据库中
    :param image_file_name: 图片文件名
    :param ocr_result:识别结果
    :return:None
    """
    # 创建 session
    session = Session()
    # 执行ORM操作
    obj1 = Ocr(image_file_name=image_file_name,
               ocr_result=ocr_result)
    session.add(obj1)
    # 提交事务
    session.commit()
    # 关闭session
    session.close()
