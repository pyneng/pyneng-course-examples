select nexthop, count(network) from rib group by nexthop;
select nexthop, count(network) from rib group by nexthop order by count(network);
select distinct netmask from rib order by cast(netmask as integer);
