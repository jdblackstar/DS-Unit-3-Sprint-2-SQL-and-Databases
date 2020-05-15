# Unit 3, Sprint 3 Study Guide

## Introduction to SQL

### Queries
1. SELECT ... specifies the attributes to be included in the resulting dataset.

SELECT
    attribute_a,
    attribute_b,
    attribute_c
FROM table_x

2. FROM ... specifies the database table from which to select results (mandatory except for non-table-related selection and functions) - Select all with *

SELECT *
FROM table_x

3. JOIN ... 

4. WHERE ... optionally used to filter the set of returned results according to one or more logical conditions.

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


5. GROUP BY ... optionally used to specify the attributes by which other attributes may be aggregated.

SELECT
    attribute_a,
    count(attribute_x) as x_count
FROM table_z
GROUP BY attribute_m

When grouping by one or more attributes, each attribute in the select clause should either be included in the group by clause, or aggregate as part of an aggregate function.

SELECT
    attribute_m,
    attribute_n,
    count(attribute_x) as x_count,
    sum(attribute_y) as y_sum
FROM table_z
GROUP BY attribute_m, attribute_n

6. HAVING ... optionally used to filter the set of returned results according to one or more logical conditions.

SELECT
    attribute_m,
    count(attribute_x) as x_count
FROM table_z
GROUP BY attribute_m
HAVING count(attribute_x) > 100

The major advantage of the HAVING clause is that it executes after many of the other clauses, enabling it to recognize attribute aliases applied during execution of the select clause, including the name of aaggregated attributes.

SELECT
    attribute_m,
    count(attribute_x) as x_count
FROM table_z
GROUP BY attribute_m
HAVING x_count > 100

7. ORDER BY ... optionally used to specify the attributes and method for sorting the resulting data set.

SELECT *
FROM my_table
ORDER BY attribute_a -- sort in ascending order (ASC) by default
ORDER BY attribute_a DESC -- sort in descending order

8. UNION ... (not covered)

### Functions
1. Casting

SELECT
    cast('2016-11-06' AS DATETIME) AS scheduled_at,
    cast('2016-11-06' AS DATE) AS scheduled_on

2. String

SELECT concat('Hello', ' ', 'world!') AS my_message

3. Date

SELECT
    now() AS datetime_right_now,
    curdate() AS date_right_now,
    curtime() AS time_right_now,
    date_format(curdate(), '%b') AS this_month_abbrev,
    date_format(curdate(), '%Y-%b') AS this_year_and_month

4. Conditional

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

SELECT
    NULL, -- evaluates to NULL
    coalesce(NULL,0) -- evaluates to 0

### Other Considerations
1. Distinct

SELECT DISTINCT attribute_a -- returns only unique values of attribute_a
FROM table_z

SELECT
    DISTINCT
        attribute_a,
        attribute_b,
        attribute_c -- returns only unique value combinations of the set of all selected attributes
FROM table_z

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