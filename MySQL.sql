create database saucedemodb;

use saucedemodb;

create table login(
username varchar(20),
password int
);

alter table login modify
username varchar(25) unique;
alter table login modify password varchar(25);

insert into login values ("admin","admin");
insert into login values ("standard_user", null);
insert into login (username) values ('error_user');
insert into login (username) values ('visual_user');

select * from login;

update login set password = 'secret_sauce' where username ='standard_user';
update login set password = 'secret_sauce' where username ='error_user';

delete from login where username='visual_user';

select password from login;

select password as "pwd" from login;
select password as "pwd" from login where username ='admin';

select * from login where username ='visual_user';


desc login













































