CREATE database `ocr` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE ocr;
CREATE TABLE Ocr (
                     id int primary key not null auto_increment comment 'ID',
                     image_file_name varchar(42) not null comment '用户名',
                     ocr_result varchar(500) not null comment '昵称',
                     create_time datetime DEFAULT CURRENT_TIMESTAMP

);