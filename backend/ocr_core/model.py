import copy

import numpy as np
from PIL import Image

from .angle_class import AangleClassHandle, shufflenet_v2_x0_5
from .config import *
from .crnn import LiteCrnn, CRNNHandle
from .crnn.keys import alphabetChinese as alphabet
from .dbnet.dbnet_infer import DBNET
from .utils import crop_rect, sorted_boxes, get_rotate_crop_image

text_handle = DBNET(model_path)
crnn_net = LiteCrnn(32, 1, len(alphabet) + 1, nh, n_rnn=2, leakyRelu=False,
                    lstmFlag=LSTMFLAG)

crnn_handle = CRNNHandle(crnn_model_path, crnn_net, gpu_id=GPU_ID)

crnn_vertical_net = LiteCrnn(32, 1, len(alphabet) + 1, nh, n_rnn=2,
                             leakyRelu=False, lstmFlag=True)
crnn_vertical_handle = CRNNHandle(crnn_vertical_model_path,
                                  crnn_vertical_net, gpu_id=GPU_ID)

angle_net = shufflenet_v2_x0_5(num_classes=len(lable_map_dict),
                               pretrained=False)

angle_handle = AangleClassHandle(angle_model_path, angle_net, gpu_id=GPU_ID)


def crnnRec(im, rects_re, f=1.0):
    """
    crnn模型，ocr识别
    @@model,
    @@converter,
    @@im:Array
    @@text_recs:text box
    @@ifIm:是否输出box对应的img
    """
    results = []
    im = Image.fromarray(im)
    for index, rect in enumerate(rects_re):
        degree, w, h, cx, cy = rect
        partImg = crop_rect(im, ((cx, cy), (h, w), degree))
        newW, newH = partImg.size
        partImg_array = np.uint8(partImg)
        if newH > 1.5 * newW:
            partImg_array = np.rot90(partImg_array, 1)
        angel_index = angle_handle.predict(partImg_array)
        angel_class = lable_map_dict[angel_index]
        rotate_angle = rotae_map_dict[angel_class]
        if rotate_angle != 0:
            partImg_array = np.rot90(partImg_array, rotate_angle // 90)
        partImg = Image.fromarray(partImg_array).convert("RGB")
        partImg_ = partImg.convert('L')
        try:
            if crnn_vertical_handle is not None and angel_class in ["shudao",
                                                                    "shuzhen"]:
                simPred = crnn_vertical_handle.predict(partImg_)
            else:
                simPred = crnn_handle.predict(partImg_)  ##识别的文本
        except:
            continue

        if simPred.strip() != u'':
            results.append(
                {'cx': cx * f, 'cy': cy * f, 'text': simPred, 'w': newW * f,
                 'h': newH * f,
                 'degree': degree})
    return results


def crnnRecWithBox(im, boxes_list):
    """
    crnn模型，ocr识别
    @@model,
    @@converter,
    @@im:Array
    @@text_recs:text box
    @@ifIm:是否输出box对应的img
    """
    results = []
    boxes_list = sorted_boxes(np.array(boxes_list))
    for index, box in enumerate(boxes_list):
        tmp_box = copy.deepcopy(box)
        partImg_array = get_rotate_crop_image(im, tmp_box.astype(np.float32))
        angel_index = angle_handle.predict(partImg_array)

        angel_class = lable_map_dict[angel_index]
        rotate_angle = rotae_map_dict[angel_class]

        if rotate_angle != 0:
            partImg_array = np.rot90(partImg_array, rotate_angle // 90)

        partImg = Image.fromarray(partImg_array).convert("RGB")
        partImg_ = partImg.convert('L')
        newW, newH = partImg.size
        try:

            if crnn_vertical_handle is not None and angel_class in ["shudao",
                                                                    "shuzhen"]:
                simPred = crnn_vertical_handle.predict(partImg_)
            else:
                simPred = crnn_handle.predict(partImg_)  ##识别的文本
        except:
            continue

        if simPred.strip() != u'':
            results.append(
                {'cx': 0, 'cy': 0, 'text': simPred, 'w': newW, 'h': newH,
                 'degree': 0})
    return results


def text_predict(img):
    boxes_list, score_list = text_handle.process(img)
    result = crnnRecWithBox(np.array(img), boxes_list)
    return result


if __name__ == '__main__':
    img = Image.open("./test.jpeg")
    img = np.array(img)
    res = text_predict(img)
    print(res)
