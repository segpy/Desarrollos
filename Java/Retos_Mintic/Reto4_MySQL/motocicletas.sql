CREATE TABLE motocicletas (
	nombreF_Moto varchar(45) not null,
    precio_U int not null,
    duracion_bat varchar(45) not null,
    proveedor_mot varchar(45) not null,
    primary key (nombreF_Moto),
    foreign key (proveedor_mot) references proveedor(nombre_prov)
);

INSERT INTO motocicletas (nombreF_Moto, precio_U, duracion_bat, proveedor_mot)
VALUES
    ("Starker", 4200000, "18 horas", "Auteco"),
    ("Lucky Lion", 5600000, "14 horas", "Hitachi"),
    ("Be Electric", 4600000, "26 horas", "Auteco"),
    ("Aima", 8000000, "36 horas", "Bosch"),
    ("Mec de Colombia", 5900000, "20 horas", "Teco"),
    ("Atom Electric", 4500000, "12 horas", "General Electric");