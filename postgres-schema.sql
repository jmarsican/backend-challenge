create schema hackajob_global_currencies;

alter schema hackajob_global_currencies owner to postgres;

create table hackajob_global_currencies.country
(
    id            serial
        primary key,
    cca3          varchar(3),
    official_name varchar(255),
    common_name   varchar(255)
);

alter table hackajob_global_currencies.country
    owner to postgres;

create table hackajob_global_currencies.currency
(
    id   serial
        primary key,
    code varchar(3)
        constraint currency_code_uk
            unique,
    name varchar(255)
);

alter table hackajob_global_currencies.currency
    owner to postgres;

create table hackajob_global_currencies.country_currency
(
    currency_id integer not null
        constraint fkdk4atlhgo1xeki0lgs136drnb
            references hackajob_global_currencies.currency,
    country_id  integer not null
        constraint fk3sgwqmtr49xyq7hplrg2r4kqf
            references hackajob_global_currencies.country,
    primary key (currency_id, country_id)
);

alter table hackajob_global_currencies.country_currency
    owner to postgres;