-- Schema

create table devices (
    ip          text not null primary key,
    hostname    text not null,
    location    text
);

create table interfaces (
    device       text not null references devices(ip)
    interface    text not null,
    ip           text,
    status       text check (status in ('up', 'down')),
);
