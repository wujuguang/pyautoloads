create schema `test_db` default character set utf8 ;

create table `test_db`.`table_one` (
  `id` int not null auto_increment comment '编号',
  `name` varchar(45) not null comment '名称',
  `text` varchar(45) null comment '文本',
  `status` tinyint null default 0 comment '状态',
  primary key (`id`));

create table `test_db`.`table_two` (
  `id` int not null auto_increment comment '编号',
  `title` varchar(45) not null comment '标题',
  `text` varchar(45) null comment '文本',
  `status` tinyint null default 0 comment '状态',
  primary key (`id`));
  
  create table `test_db`.`table_user` (
  `id` int not null auto_increment comment '编号',
  `name` varchar(45) not null comment '姓名',
  `passwd` varchar(45) null comment '密码',
  primary key (`id`));