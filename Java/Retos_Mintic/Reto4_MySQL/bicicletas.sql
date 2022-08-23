create table bicicletas (
	nombreF_Bici varchar(45),
    precio_U bigint not null,
    año_const int not null,
    primary key (nombreF_bici)
);

INSERT INTO bicicletas (nombreF_Bici, precio_U, año_const)
VALUES
    ("Cannondale", 1200000, 2020),
    ("Trek", 1450000, 2019),
    ("Yeti", 2000000, 2020),
    ("Fuji", 950000, 2021),
    ("Bmc", 1950000, 2018);