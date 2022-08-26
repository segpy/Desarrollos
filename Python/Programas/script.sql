--MySQL Functions:
--String Functions: ASCII, CHAR, CONCAT, CONCAT_WS, ELT, EXPORT_SET, FIELD, FIND_IN_SET, INSERT, INSTR, LCASE, LEFT, LENGTH, LOCATE, LOWER, LPAD, LTRIM, MID, OCTET_LENGTH, POSITION, REPEAT, REPLACE, REVERSE, RIGHT, RPAD, RTRIM, SOUNDEX, SPACE, SUBSTRING, SUBSTRING_INDEX, UCASE, UPPER, VERSION,
--Numeric Functions: ABS, CEIL, CEILING, EXP, FLOOR, LN, LOG, LOG2, LOG10, MOD, POWER, RADIANS, RAND, RANDOM, ROUND, SIGN, SQRT, TRUNCATE,
--Date Functions: CURDATE, CURTIME, DATE, DATEDIFF, DAY, DAYNAME, DAYOFMONTH, DAYOFWEEK, DAYOFYEAR, HOUR, MINUTE, MONTH, MONTHNAME, NOW, QUARTER, SECOND, TIMESTAMP, TIMESTAMPADD, TIMESTAMPDIFF, WEEK, WEEKDAY, WEEKOFYEAR, YEAR, YEARWEEK,


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

/*se tienen tres tablas tipo_doc, personal y documentos, hacer una solicitud que traiga el identificador de personal y nombre de la persona de todo el personal que tenga exactamente 3 documentos registrados sin usar count.
*/
SELECT personal.id, personal.nombre FROM personal INNER JOIN documentos ON personal.id = documentos.id_personal group by personal.id having count(documentos.id_personal) = 3;

/*Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
*/
SELECT DISTINCT city FROM station WHERE city LIKE 'a%' OR city LIKE 'e%' OR city LIKE 'i%' OR city LIKE 'o%' OR city LIKE 'u%';

/*Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.
*/
SELECT DISTINCT city FROM station WHERE city LIKE '%a' OR city LIKE '%e' OR city LIKE '%i' OR city LIKE '%o' OR city LIKE '%u';

/*Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters.
*/
select distinct city from station where (city like 'a%' or city like 'e%' or city like 'i%' or city like 'o%' or city like 'u%') and (city like '%a' or city like '%e' or city like '%i' or city like '%o' or city like '%u');
--Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters using MySQL's functions (i.e., RIGHT, LEFT, LENGTH, SUBSTRING, etc.).
SELECT DISTINCT city FROM station WHERE RIGHT(city, 1) IN ('a', 'e', 'i', 'o', 'u') AND LEFT(city, 1) IN ('a', 'e', 'i', 'o', 'u');

--Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates using MySQL's functions (i.e., RIGHT, LEFT, LENGTH, SUBSTRING, etc.).
SELECT DISTINCT city FROM station WHERE RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

--Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates. using MySQL string functions
SELECT DISTINCT city FROM station WHERE LEFT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u') OR RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

--Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates. using MySQL string functions
SELECT DISTINCT city FROM station WHERE LEFT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u') AND RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

/*Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID. Use string functions.
*/
SELECT nombre FROM students WHERE marks > 75 ORDER BY right(nombre, 3) ASC, id ASC;
SELECT nombre FROM students WHERE marks > 75 ORDER BY SUBSTRING(nombre, -3), id ASC;


/*Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
*/
SELECT SUM(population) FROM city INNER JOIN country ON city.CountryCode = country.Code WHERE continent = 'Asia';

/*Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
*/
SELECT city.Name FROM city INNER JOIN country ON city.CountryCode = country.Code WHERE continent = 'Africa';
select city.name from city where countrycode in (select country.code from country where continent = 'Africa');