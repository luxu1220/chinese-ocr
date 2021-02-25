# 基础镜像
FROM mysql:5.7
#设置免密登录
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
#将所需文件放到容器中
COPY setup.sh /Data/setup.sh
COPY schema.sql /Data/schema.sql
COPY changeUser.sql /Data/changeUser.sql
#初始化数据库
RUN sh /Data/setup.sh
#设置容器启动时执行的命令
CMD service mysql start && tail -F /var/log/mysql/error.log