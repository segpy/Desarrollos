create database miConexion;
use miConexion;

select * from users;

delete from users where usuario = 'sebas' and id;

insert into alumnos values 
		(1,'Sebas','Gomez'),
        (2,'Aura','Gomez'),
        (3,'Bibi','Gomez'),
        (4,'Alicia','Valencia'),
        (5,'Carlos','Martinez'),
        (6,'Diana','Gomez'),
        (7,'Juan','Gomez'),
        (8,'Pacho','Dussan');
        
select * from alumnos;
DELETE FROM alumnos WHERE idAlumnos>=1;

SELECT * FROM alumnos WHERE nombre = "sebas" and idAlumnos >= 1;