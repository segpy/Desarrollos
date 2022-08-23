create database reto4;
use reto4;

select * from bicicletas;
select * from proveedor;
select * from clientes;
select * from motocicletas;

alter table intenciones modify column id_intencion int not null auto_increment;

show create table intenciones;

select * from intenciones;
