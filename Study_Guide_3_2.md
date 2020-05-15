# Unit 3, Sprint 3 Study Guide

## Introduction to SQL

### Queries

1. SELECT ... specifies the attributes to be included in the resulting dataset.

```sql
SELECT
    attribute_a,
    attribute_b,
    attribute_c
FROM table_x
```


2. FROM ... specifies the database table from which to select results (mandatory except for non-table-related selection and functions) - Select all with *

```sql
SELECT *
FROM table_x
```


3. JOIN ... https://i.stack.imgur.com/UI25E.jpg

INNER JOIN:
Returns only the results from each table that match the join condition. Records from both the original table and joined table may be excluded. Use INNER JOIN to denote an inner join. Open source DBMSs also recognize JOIN.

```sql
SELECT
  table_h.attribute_a
  ,table_h.attribute_b
  ,table_j.attribute_a
  ,table_j.attribute_x
  ,table_j.attribute_y
FROM table_h
JOIN table_j ON table_j.some_attribute = table_h.related_attribute
```

Outer Join:
Append onto the original table any results from the joined table that happen to match the join condition. Records from the original table will all be included, while some records from the joined table may be excluded. use LEFT JOIN or RIGHT JOIN to denote an outer join.

Multiple Joins:
Unlike other clauses, which may only be used once in a query, you may use a new join clause for each new table you would like to include.

```sql
SELECT
  a.attribute_d
  ,a.attribute_t
  ,b.some_awesome_attribute
  ,c.another_awesome_attribute
  ,d.the_best_attribute_ever
FROM table_b AS b
JOIN table_a AS a ON b.other_attribute = a.some_attribute
JOIN table_c AS c ON b.attribute_x = c.attribute_y
JOIN table_d AS d ON b.attribute_x = c.attribute_y
JOIN table_y AS y ON a.another_attr = y.attr2
```


4. WHERE ... optionally used to filter the set of returned results according to one or more logical conditions.

```sql
WHERE attribute_b = "some specific value" -- equal to
WHERE attribute_b <> "some specific value" -- not equal to
WHERE attribute_b > "some specific value" -- greater than, less than, etc.
WHERE attribute_b >= "some specific value" -- greater than or =, less than or =, etc.
WHERE attribute_b > "some specific value" -- greater than, less than, etc.

WHERE attribute_b LIKE "%some specific value%" -- open source dbms, string matches w/ wildcards
WHERE attribute_b LIKE "*some specific value*" -- ms access dbms, string matches w/ wildcards

WHERE attribute_b IN ("specific value 1", "specific value 2") -- inclusion in a list

WHERE attribute_b IS NULL -- lack of any value
WHERE attribute_b IS NOT NULL -- presence of any value
```


5. GROUP BY ... optionally used to specify the attributes by which other attributes may be aggregated.

```sql
SELECT
    attribute_a,
    count(attribute_x) as x_count
FROM table_z
GROUP BY attribute_m
```

When grouping by one or more attributes, each attribute in the select clause should either be included in the group by clause, or aggregate as part of an aggregate function.

```sql
SELECT
    attribute_m,
    attribute_n,
    count(attribute_x) as x_count,
    sum(attribute_y) as y_sum
FROM table_z
GROUP BY attribute_m, attribute_n
```


6. HAVING ... optionally used to filter the set of returned results according to one or more logical conditions.

```sql
SELECT
    attribute_m,
    count(attribute_x) as x_count
FROM table_z
GROUP BY attribute_m
HAVING count(attribute_x) > 100
```

The major advantage of the HAVING clause is that it executes after many of the other clauses, enabling it to recognize attribute aliases applied during execution of the select clause, including the name of aaggregated attributes.

```sql
SELECT
    attribute_m,
    count(attribute_x) as x_count
FROM table_z
GROUP BY attribute_m
HAVING x_count > 100
```


7. ORDER BY ... optionally used to specify the attributes and method for sorting the resulting data set.

```sql
SELECT *
FROM my_table
ORDER BY attribute_a -- sort in ascending order (ASC) by default
ORDER BY attribute_a DESC -- sort in descending order
```


8. UNION ... (not covered)

### Functions

1. Casting

```sql
SELECT
    cast('2016-11-06' AS DATETIME) AS scheduled_at,
    cast('2016-11-06' AS DATE) AS scheduled_on
```

2. String

```sql
SELECT concat('Hello', ' ', 'world!') AS my_message
```

3. Date

```sql
SELECT
    now() AS datetime_right_now,
    curdate() AS date_right_now,
    curtime() AS time_right_now,
    date_format(curdate(), '%b') AS this_month_abbrev,
    date_format(curdate(), '%Y-%b') AS this_year_and_month
```

4. Conditional

```sql
SELECT
    courses.registration_name,
    IF(courses.registration_name LIKE "%ISTM%", "Information Systems Department", "Other Department") AS department_classification,
    CASE
        WHEN courses.registration_name LIKE '%ISTM%' THEN 'Information Systems Department'
        WHEN courses.registration_name LIKE '%BADM%' THEN 'Business Administration Department'
        WHEN courses.registration_name LIKE '%MKTG%' THEN 'Marketing Department'
        ELSE 'Other Department'
    END department_name
FROM(
    SELECT "MKTG-1414-10" AS registration_name
) courses
```

```sql
SELECT
    NULL, -- evaluates to NULL
    coalesce(NULL,0) -- evaluates to 0
```

### Database Management

#### Databases

1. Create Database

```sql
CREATE DATABASE my_db;
```

2. Remove Database

```sql
DROP DATABASE my_db;
```
```sql
DROP DATABASE IF EXISTS my_db;
```

3. Show Database
```sql
-- mysql:
SHOW DATABASES;

-- sqlite:
.databases

-- postgresql:
\list
```


#### Tables

1. Create Table

```sql
CREATE TABLE my_table; -- only some dbms let you create an undefined table structure like this
```

```sql
CREATE TABLE IF EXISTS my_table; -- conditionally create a table
```

```sql
CREATE TABLE my_well_defined_table (
    name VARCHAR(20),
    owner VARCHAR(20),
    species VARCHAR(20),
    sex CHAR(1),
    birth DATE,
    death DATE
);
```

```sql
CREATE TABLE my_table_copy AS (
    SELECT * FROM my_table
);
```

2. Remove Table

```sql
DROP TABLE my_table;
```

```sql
DROP TABLE IF EXISTS my_table;
```

3. Show Tables

```sql
-- mysql:
SHOW DATABASES;

-- sqlite:
.tables

-- postgresql:
\connect db_name
\dt
```

#### Index Attributes

1. Create Indices

Create a normal index.
```sql
-- mysql:
ALTER TABLE my_table ADD INDEX(my_index_attribute);

-- postgresql:
CREATE INDEX my_index ON my_table (my_index_attribute);

-- sqlite:
CREATE INDEX 'my_index' ON 'my_table' ('my_index_attribute' ASC);
```

Create a primary key.
```sql
-- mysql:
ALTER TABLE my_table ADD PRIMARY KEY(my_primary_key_attribute);

-- sqlite:
CREATE UNIQUE INDEX 'my_pk_index' ON 'my_table' ('my_primary_key_attribute' ASC);
```

Create a composite primary key.
```sql
-- mysql:
ALTER TABLE my_db.my_table ADD PRIMARY KEY(first_composite_key_attribute, second_composite_key_attribute, another_composite_key_attribute);

-- sqlite:
CREATE UNIQUE INDEX `my_ck_index` ON `my_table` (`first_compisite_key_attribute`, `second_compisite_key_attribute`, `another_compisite_key_attribute` ASC);
```

2. Remove Indices

```sql
-- mysql:
DROP INDEX my_index_attribute ON my_table;

-- sqlite:
DROP INDEX my_index;
```

3. Show Indices
```sql
-- mysql:
SHOW INDEX FROM my_table;

-- sqlite:
.indices
```

#### Data

1. Create Records

```sql
INSERT INTO my_well_defined_table
VALUES ('Fluffy','George Washington','dog','m','1956-10-28', NULL);
```

```sql
INSERT INTO my_well_defined_table
VALUES
  ('Fluffy','George Washington','dog','m','1756-10-28', NULL),
  ('Ruffles','George Washington','dog','f','1766-09-01', NULL)
;
```

Load records from a text file.

```sql
LOAD DATA LOCAL INFILE '~/Desktop/some_file.txt'
INTO TABLE my_well_defined_table
FIELDS
  TERMINATED BY ','
  ENCLOSED BY '"'
LINES TERMINATED BY '\r\n' -- windows-style line breaks
-- LINES TERMINATED BY '\n' -- mac-style line breaks
IGNORE 1 LINES
;
/*
data importation references:
  + https://dev.mysql.com/doc/refman/5.0/en/loading-tables.html
  + https://dev.mysql.com/doc/refman/5.0/en/insert.html
  + https://dev.mysql.com/doc/refman/5.0/en/load-data.html
  + csv/txt line break characters:
    + windows: '\r\n'
    + mac: either '\n' (OS-X), or '\r' (OS-9 and earlier)
*/
```

2. Remove Records

```sql
DELETE FROM my_table; -- removes all records
```

```sql
DELETE FROM my_table
WHERE attribute_a = "some value"; -- removes all records matching a given condition (see data analysis lecture notes for more info on the where clause...)
```

### Other Considerations

1. Distinct

```sql
SELECT DISTINCT attribute_a -- returns only unique values of attribute_a
FROM table_z
```

```sql
SELECT
    DISTINCT
        attribute_a,
        attribute_b,
        attribute_c -- returns only unique value combinations of the set of all selected attributes
FROM table_z
```

### Best Practices

#### Know the schema
Endeavor to learn, understand, and even memorize table names, attribute names, and table relationships. Print or draw a schema diagram, table diagram or ERD, and keep it with you for reference as you query. This will improve schema familiarity and query productivity.

#### Count rows
Notice, and place a high importance on the number of rows returned by each query. Anticipate and predict the number of rows you expect will be returned by each query. This will help remediate unexpected results and SQL misunderstandings that might otherwise not be revealed by DBMS error messages.

#### Start small
Don't try to write the final query in one attempt. Start by writing basic queries and execute each successfully before iteratively adding complexity to arrive at your final attempt. This will help you diagnose/avoid bugs and syntax errors.

#### Work backwards
Think about the end result of the query you are trying to write before you start writing. What are the attributes and characteristics of your desired dataset? Describe and/or draw your desired dataset before you start writing SQL. By keeping in mind your final objective, you will be better able to devise a proper query strategy, and you might save time by avoiding unproductive/improper strategies and attempts.

#### Document your work
Document your manual and programmatic tasks alike. Literally write down what you did and how you did it, and keep that information close beside your actual work product. Use comments in your code to help explain your intentions and methodology. This will improve the ability of yourself and others to repeat your work in the future, and will help you in efforts to diagnose/verify/justify analytical findings.

#### Use consistent style
Adopt the writing style of community members or develop your own, but be consistent. This will help you communicate/share your queries with others, and avoid syntax errors.

## SQL for Analysis

### NOSQL

### Elephant SQL

#### Browser

### PostgreSQL




## NOSQL and Document Oriented Databases

### Important to know what a computer cluster is

## Acid and Database Scalability Tradeoffs


## Types of Databases
### NoSQL

### MongoDB
- Really easy to put data into, doesn't really 

### Vertica (Columnar)
### Amazon RedShift (Columnar)


## Sprint Challenge Format

### Create data base
### Insert data into it

### If provided a data base and asked business questions, write queries for it