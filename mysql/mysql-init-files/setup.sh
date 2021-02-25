#!/bin/bash
echo `service mysql status`
echo '1 Service Start.....'
service mysql start
sleep 3
echo `service mysql status`
echo '2.Create table'
mysql< /mysql/schema.sql
sleep 3
echo '3. Create user'
mysql< /mysql/changeUser.sql
sleep 3
echo `service mysql status`
echo '4 ok'