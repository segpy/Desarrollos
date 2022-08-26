--!CONSULTAS
--Formas de hacer un select

--? Alterando primer atributo del select
--*SELECT * ...
--*SELECT campo ...;
--*SELECT campo1, campo2 ...;    

DISTINCT: muestra solo los valores distintos/sin repetir
--*SELECT distinct campo ...;
    --Muestra la combinacion de los campos(combinados) sin repetir
--*SELECT distinct campo1, campo2 ...; 


AS: asigna un nombre a un campo
--*SELECT campo AS nombre ...;
--*SELECT campo1 AS nombre1, campo2 AS nombre2 ...;
    CONCAT
    --*SELECT CONCAT(campo1,,' ',campo2) AS nombre ...;
--*SELECT count(*) AS nombre ...;
--*SELECT ... from tabla as nombre ...;

COUNT: cuenta los valores, salida entera                    <-------------->        funcion agregada: NECESITA GROUP BY para separar los valores
--*SELECT count(campo) ...;
--*SELECT count(*) ...;
    DISTINCT
    --*SELECT count(distinct campo) ...;
    --*SELECT count(distinct *) ...;


SUM: suma los valores de un campo, salida entera            <-------------->        funcion agregada: NECESITA GROUP BY para separar los valores
--*SELECT sum(campo) ...;


AVG: promedio de los valores de un campo, salida entera     <-------------->        funcion agregada: NECESITA GROUP BY para separar los valores
--*SELECT avg(campo) ...;

MIN: minimo de los valores de un campo                      <-------------->        funcion agregada: NECESITA GROUP BY para separar los valoress
--*SELECT min(campo) ...;

MAX: maximo de los valores de un campo                      <-------------->        funcion agregada: NECESITA GROUP BY para separar los valores
--*SELECT max(campo) ...;


TOP: muestra las primeras(#) filas de una tabla --SQLServer, MS Access
--*SELECT TOP # * ...;
--*SELECT TOP # campo ...;
LIMIT: muestra las primeras(#) filas de una tabla --MySQL, PostgreSQL
--*SELECT * from ... LIMIT #;
--*SELECT * from ... LIMIT #,#;
    OFFSET: muestra las filas que estan despues de la fila #
    --*SELECT * from ... LIMIT # OFFSET #;


CASE: se usa para hacer una condicion
/*
SELECT OrderID, Quantity,
CASE
    WHEN Quantity > 30 THEN 'The quantity is greater than 30'
    WHEN Quantity = 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS QuantityText
FROM OrderDetails;
*/
/*
SELECT CustomerName, City, Country
FROM Customers
ORDER BY
(CASE
    WHEN City IS NULL THEN Country
    ELSE City
END);
*/

--? Alterando segundo atributo del select
--*SELECT ... FROM tabla ...;



--? Alterando tercer atributo del select
INNER JOIN: uniendo dos tablas
--*INNER JOIN tabla2 ON tabla1.campo = tabla2.campo;
    WHERE
    --*INNER JOIN tabla2 ON tabla1.campo = tabla2.campo WHERE ...;
    GROUP BY
    --*INNER JOIN tabla2 ON tabla1.campo = tabla2.campo GROUP BY ...;
    ORDER BY
    --*INNER JOIN tabla2 ON tabla1.campo = tabla2.campo ORDER BY ...;


WHERE: filtra los valores de un campo             
--*WHERE campo = valor;
                 valor pueder ser:
        -subquery: 'select min(age) from tabla'
        -int:       1
        -string:   'USA'
        -float:     1.5
        -date:      '2019-01-01'
        -datetime:  '2019-01-01 00:00:00'
        -time:      '00:00:00'
        -bool:       true
        
    AND, OR, NOT, IN
    --*WHERE campo1 = valor1 AND campo2 = valor2;
    --*WHERE campo1 = valor1 OR campo2 = valor2;
    --*WHERE NOT campo = valor;
    --*WHERE campo IN (valor1, valor2);
    --*WHERE valor IN (campo);
    --*WHERE campo IN (select campo from tabla);
OPERATOR: =, <, >, <=, >=, <>
    --*WHERE campo1 OPERATOR valor; 
    BETWEEN: valor1 AND valor2
    --*WHERE campo BETWEEN valor1 AND valor2;
    --*WHERE campo NOT BETWEEN valor1 AND valor2;
    IS NULL: campo es nulo
    --*WHERE campo IS NULL;
    IS NOT NULL: campo no es nulo
    --*WHERE campo IS NOT NULL;
        COUNT, cuenta los NULL o NOT NULL
    --*SELECT count(*) FROM tabla WHERE campo IS NOT NULL;
    EXISTS
    --*WHERE EXISTS (SELECT * FROM tabla2 WHERE campo = campo2);
    LIKE: se usa con string 
    --*WHERE campo LIKE 'string';
    ANY: campo contiene alguno de los valores
    --*WHERE campo OPERATOR ANY (valor1);
    ALL: campo contiene todos los valores
    --*WHERE campo OPERATOR ALL (subquery);
    GROUP BY: agrupa los valores de un campo
    --*WHERE campo ... GROUP BY campo ...;
    ORDER BY:
    --*WHERE campo1 ... ORDER BY campo2 ...;
    UNION:
    --*WHERE campo1 ... UNION SELECT campo2 FROM tabla2;


GROUP BY: agrupa los valores unicos de un campo
--*GROUP BY campo;
    HAVING: filtra los valores de un campo
    --*GROUP BY campo HAVING campo = valor;
    HAVING COUNT: cuenta los valores de un campo
    --*GROUP BY campo HAVING count(*) > #;
    HAVING SUM: suma los valores de un campo
    --*GROUP BY campo HAVING sum(campo) > #;
    HAVING AVG: promedio de los valores de un campo
    --*GROUP BY campo HAVING avg(campo) > #;
    HAVING MIN: minimo de los valores de un campo
    --*GROUP BY campo HAVING min(campo) > #;
    HAVING MAX: maximo de los valores de un campo
    --*GROUP BY campo HAVING max(campo) > #;


ORDER BY: ordena los valores de un campo
--*ORDER BY campo;
    ASC: ascendente
    --*ORDER BY campo ASC;
    DESC: descendente
    --*ORDER BY campo DESC;

UNION: unir dos tablas exactamente iguales
--*UNION SELECT * FROM tabla2;
    ALL: unir todas las filas de las tablas
    --*UNION ALL SELECT * FROM tabla2;















