create database employeedb;

use employeedb;

create table employee(
eid int primary key,
ename varchar(25) not null,
salary numeric(10,2),
bonus numeric(7,2)
);

desc employee;