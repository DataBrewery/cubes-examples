
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
    id varchar(200) unique,
    name varchar(200)
);

drop table if exists products;
create table products (
    id varchar(200) unique,
    category_id varchar(200),
    category_label varchar(200),
    product_id varchar(200),
    product_label varchar(200)
);

drop table if exists countries;
create table countries (
    id varchar(200) unique,
    continent_id varchar(200),
    continent_label varchar(200),
    country_id varchar(200),
    country_label varchar(200)
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

drop table if exists webvisits;
create table webvisits (
    id varchar(128) unique,
    
    date_id integer,
    country_id integer,
    
    browser varchar(200),
    newsletter varchar(200),
    source_id varchar(200),
    source_label varchar(200),
    
    pageviews integer
);
