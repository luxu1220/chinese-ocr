import uuid
from pathlib import Path


def save_file(file):
    """
    保存文件
    :param file:文件
    :return:新的文件名
    """
    # 利用 uuid 生成新的文件名
    filename = str(uuid.uuid4()) + Path(file.filename.lower()).suffix
    # 保存到 temp 文件夹下
    dest = Path('temp') / filename
    if not dest.parent.exists():
        dest.parent.mkdir(parents=True)
    with dest.open('wb+') as dest_f:
        dest_f.write(file.read())
    return filename
