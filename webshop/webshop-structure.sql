
drop table if exists dates;
create table dates (
    id varchar(128) unique,
    date_year integer,
    date_quarter integer,
    date_month integer,
    date_day integer,
    date_week integer
);

drop table if exists customers;
create table customers (
    id varchar(128) unique,
    name varchar(200)
);

drop table if exists products;
create table products (
    id varchar(128) unique,
    category varchar(200),
    name varchar(200)
);

drop table if exists countries;
create table countries (
    id varchar(128) unique,
    continent varchar(200),
    country varchar(200)
);

drop table if exists sales;
create table sales (
    id varchar(128) unique,
    
    date_id integer,
    customer_id integer,
    product_id integer,
    country_id integer,
    
    quantity real,
    price_total real
);

