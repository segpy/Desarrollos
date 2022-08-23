CREATE TABLE intenciones (
	id_intencion int not null auto_increment,
    user varchar(45) not null,
    busqueda varchar(45) not null,
    fecha date not null,
    hora time not null,
    primary key (id_intencion),
    foreign key (user) references clientes(username)
);

INSERT INTO intenciones (user, busqueda,fecha, hora)
VALUES
    ("lucky", "Cannondale", '2017-10-25', '20:00:00'),
    ("lucky", "Trek", '2019-03-15', '18:30:00'),
    ("lucky", "Starker", '2019-05-20', '20:30:00'),
    ("malopez", "Cannondale", '2018-05-20', '20:30:00'),
    ("malopez", "Starker", '2020-01-20', '20:30:00'),
    ("diva", "Yeti", '2019-05-20', '20:30:00'),
    ("diva", "Fuji", '2018-06-22', '21:30:00'),
    ("diva", "Lucky Lion", '2020-03-17', '15:30:20'),
    ("dreamer", "Lucky Lion", '2020-03-17', '15:30:20'),
    ("dreamer", "Be Electric", '2020-04-10', '18:30:20'),
    ("ninja", "Aima", '2020-02-17', '20:30:20'),
    ("ninja", "Starker", '2020-02-20', '16:30:20'),
    ("ninja", "Mec de Colombia", '2020-03-27', '18:30:20'),
    ("rose", "Atom Electric", '2020-03-20', '21:30:20'),
    ("green", "Yeti", '2020-01-10', '17:30:20'),
    ("green", "Trek", '2020-02-15', '20:30:20'),
    ("green", "Bmc", '2020-03-17', '18:30:20');