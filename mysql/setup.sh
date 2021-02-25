#!/bin/bash
echo `service mysql status`
echo '1 Service Start.....'
mkdir /home/mysql
chmod 755 /home/mysql
service mysql start
sleep 3
echo `service mysql status`
echo '2.Create table'
mysql< /Data/schema.sql
sleep 3
echo '3. Create user'
mysql< /Data/changeUser.sql
echo '4 stop service.....'
sleep 3
service mysql stop
sleep 3
echo `service mysql status`
echo '5 ok'