use mysql;
select host, user from user;
create user ocruser identified by 'ocr_secret';
grant usage on *.* to root@localhost identified by'123456';
grant all on ocr.* to ocruser@'%' identified by 'ocr_secret' with grant option;
flush privileges;