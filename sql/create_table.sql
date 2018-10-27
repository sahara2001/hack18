delimiter $
/*This file create tables for hackohio18 app*/

create table if not exists LOCATIONS
(
    Loc_id varchar(8),
    Lat DOUBLE DEFAULT 0,
    Lng DOUBLE DEFAULT 0,
    primary key (Loc_id)
)engine = innodb;

create table if not exists USERS
(
    `Id` varchar(8) AUTOINCREMENT,
    `User_name` varchar(40),
    `Location_id` varchar(8)
    ON UPDATE CASCADE
    ON DELETE SET NULL,
    primary key (`Id`),
    foreign key (`Location_id`) REFERENCES LOCATIONS(`Loc_id`)
    ON UPDATE CASCADE)

create table REQUIREMENTS
(
    Person varchar(8),
    Radius int default 0,
    Problem varchar(255),
    Time_pub DATETIME default CURRENT_TIMESTAMP,
    foreign key (Person) REFERENCES USERS(Id)
)engine=innodb;

create table HELPER
(
    Person varchar(8),
    Radius int defualt 0,
    Solution varchar(255),
    Time_pub DATETIME default CURRENT_TIMESTAMP,
    foreign key (Person) REFERENCES USERS(Id)
) 

$;