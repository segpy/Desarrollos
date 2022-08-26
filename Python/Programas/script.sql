/*Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
*/
SELECT DISTINCT city FROM station WHERE id % 2 = 0;

/*Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
*/
SELECT COUNT(city) - COUNT(DISTINCT city) FROM station;

/*Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
*/
SELECT city, length(city) from station where length(city) = (SELECT MIN(length(city)) FROM station) ORDER BY city ASC LIMIT 1;
SELECT city, length(city) from station where length(city) = (SELECT MAX(length(city)) FROM station) ORDER BY city ASC LIMIT 1;

/*Write a query to print IDs of the campanies that have more than 10000 employees, in ascending order of ID.
*/
SELECT id FROM company WHERE employees > 10000 ORDER BY id ASC;

/*se tienen tres tablas tipo_doc, personal y documentos, hacer una solicitud que traiga el identificador de personal y nombre de la persona de todo el personal que tenga exactamente 3 documentos registrados
*/
SELECT personal.id, personal.nombre FROM personal INNER JOIN documentos ON personal.id = documentos.id_personal group by personal.id having count(documentos.id_personal) = 3;