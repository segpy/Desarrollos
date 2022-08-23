create table clientes (
	username varchar(45),
	nombres varchar(45),
    apellidos varchar(45),
    email varchar(45),
    celular bigint not null,
    pasword int not null,
    nacimiento date not null,
    primary key (username)
);

INSERT INTO clientes (username, nombres, apellidos, email, celular, pasword, nacimiento)
VALUES 
    ("lucky", "Pedro", "Perez", "tunometecabra@gmail.com", 3108539152, 12345678, '2000-05-12'),
    ("malopez", "Maria", "Lopez", "malopes@gmail.com", 3175410050, 87654321, '1989-08-24'),
    ("diva", "Ana", "Diaz", "diva@gmail.com", 3223142231, 21425353, '2001-04-29'),
    ("dreamer", "Luis", "Rojas", "dreamer@gmail.com", 3013512235,  43526342, '2004-12-04'),
    ("ninja", "Andres", "Cruz", "ninja@gmail.com", 3223654785, 23154789, '2004-10-19'),
    ("neon", "Nelson", "Ruiz", "neon@gmail.com", 3152556494, 54332987, '1993-05-15'),
    ("rose", "Claudia", "Mendez", "rose@gmail.com", 3005478124, 96432543, '2002-01-26'),
    ("green", "Jorge", "Rodriguez", "green@gmial.com", 3184562745, 65467124, '2000-11-17');