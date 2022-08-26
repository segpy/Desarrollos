create table users ( 
	id int not null auto_increment,
    usuario varchar(45),
    clave varchar(45),
    primary key (id)
);
insert into users values 
		(1,'sebas','clave');


insert into users values 
		(1,'sebas','clave'),
        (2,'aura','clave');
        
insert into users values (1,'sebas','clave');