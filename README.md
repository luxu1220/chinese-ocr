# 项目背景
本项目构建了一个简单 Flask 应用，提供中文 OCR 功能， 并将识别结果存储在 Mysql 数据库中，仅做展示使用。

# 安装
1. clone 项目  `git clone https://github.com/WestonLu/chinese-ocr.git`
2. build 后端镜像，在 chinese-ocr/backend 文件夹内执行 `docker build -t luxu1220/docker-backend .`
3. build mysql镜像，在 chinese-ocr/mysql 文件夹内执行 `docker build -t luxu1220/mysql .`
4. 使用 docker-compose 启动服务， 在 chinese-ocr 文件夹内执行 `docker-compose up -d`

如果 build 镜像时使用了其他 tag，请自行修改 docker-compose.yaml 中的镜像名。

# 使用
浏览器访问 http://127.0.0.1:5005/ 可查看 API。

![](https://ftp.bmp.ovh/imgs/2021/02/060a05f7a38ed1c1.png)


测试图像及识别结果见下图。

![](https://ftp.bmp.ovh/imgs/2021/02/1279ec9f5cf638ca.png)

![](https://ftp.bmp.ovh/imgs/2021/02/d7250a0eabbd6849.png)

# 相关项目
ocr 部分来自 https://github.com/DayBreak-u/chineseocr_lite



