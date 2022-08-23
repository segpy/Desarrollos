create table proveedor (
	nombre_prov varchar(45),
    direccion varchar(45),
    telefono bigint not null,
    primary key (nombre_prov)
);

INSERT INTO proveedor (nombre_prov, direccion, telefono)
VALUES 
    ("Auteco", "calle 7 No. 45-17", 05713224459),
    ("Hitachi", "calle 19 No. 108-26", 05714223344),
    ("Bosch", "carrera 68 No. 26-45", 05715678798),
    ("Teco", "calle 77 No. 68-33", 05712213243),
    ("General Electric", "calle 29 No. 26-12", 05717239919);
    