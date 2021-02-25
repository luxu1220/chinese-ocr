# 基础镜像
FROM mysql:5.7
# 暴露端口
EXPOSE 3306
#设置免密登录
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
CMD service mysql start && tail -F /var/log/mysql/error.log