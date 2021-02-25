use mysql;
select host, user from user;
create user ocruser identified by 'ocr_secret';
grant all on ocr.* to ocruser@'%' identified by 'ocr_secret' with grant option;
flush privileges;