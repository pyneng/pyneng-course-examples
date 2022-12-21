-- Schema

create table if not exists devices (
    ip          text not null primary key,
    hostname    text not null,
    location    text
);

create table interfaces (
    device       text not null,
    interface    text not null,
    ip           text,
    status       text check (status in ('up', 'down'))
);
