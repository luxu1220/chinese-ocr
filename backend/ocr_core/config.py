import os

filt_path = os.path.abspath(__file__)
father_path = os.path.abspath(os.path.dirname(filt_path) + os.path.sep + ".")

GPU_ID = "cpu"

dbnet_short_size = 960
det_model_type = "dbnet"
pse_scale = 1
model_path = os.path.join(father_path, "models/dbnet.onnx")

# crnn相关
nh = 256
crnn_vertical_model_path = os.path.join(father_path,
                                        "models/crnn_dw_lstm_vertical.pth")
LSTMFLAG = False
crnn_model_path = os.path.join(father_path, "models/crnn_lite_dense_dw.pth")

# angle_class相关
lable_map_dict = {0: "hengdao", 1: "hengzhen", 2: "shudao",
                  3: "shuzhen"}  # hengdao: 文本行横向倒立 其他类似
rotae_map_dict = {"hengdao": 180, "hengzhen": 0, "shudao": 180,
                  "shuzhen": 0}  # 文本行需要旋转的角度
angle_type = "shufflenetv2_05"
angle_model_path = os.path.join(father_path, "models/{}.pth".format(angle_type))

TIMEOUT = 30

version = 'api/v1'
