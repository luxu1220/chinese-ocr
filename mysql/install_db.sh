mysql -uroot -p$MYSQL_ROOT_PASSWORD << EOF
source $WORK_PATH/init_database_table.sql
source $WORK_PATH/init_user.sql