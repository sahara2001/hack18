-- schema.sql

drop database if exists awesome;

create database awesome;

use awesome;

/*grant select, insert, update, delete on awesome.* to 'www-data'@'localhost' identified by 'www-data';
*/
create table users (
    `id` varchar(8) not null,
    `name` varchar(50) not null,
    `loc` varchar(8) not null,
    primary key (`id`)
) engine=innodb;



create table chats (
    `id` varchar(50) not null,
    `user_id` varchar(50) not null,
    `user_name` varchar(50) not null,
    `content` mediumtext not null,
    `created_at` real not null,
    primary key (`id`)
) engine=innodb;

create table locations (
    `id` varchar(8) not null,
    `lat` DOUBLE default 0,
    `lng` DOUBLE default 0,
    primary key (`id`)
) engine=innodb;

create table REQUIREMENTS
(
    `Person` varchar(8),
    `Radius` int default 0,
    `Problem` varchar(255),
    `Time_pub` real not null

) engine=innodb;

create table HELPER
(
    `Person` varchar(8),
    `Radius` int defualt 0,
    `Solution` varchar(255),
    `Time_pub` real not null


) engine=innodb;

