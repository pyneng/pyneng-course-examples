-- Schema

create table devices (
    ip          text not null primary key,
    hostname    text not null,
    location    text
);

create table interfaces (
    device       text not null references devices(ip)
    interface    text,
    ip           text,
    status       text,
);
