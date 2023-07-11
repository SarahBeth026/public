***Beezwax SQL Exercise***
--------------

A version of this exercise without answers that can be copied/filled in can be found here: 
https://app.noteable.io/published/32c330c7-808e-4855-93af-a03bb57de2b3/Beezwax-SQL-Exercise

Dataset: Public School Characteristics 
https://catalog.data.gov/dataset/public-school-characteristics-2020-21 


**QUESTION 1:** Using the data frame/table named "schools" (imported in the step above), filter the file to just Washington (LSTATE) State High Schools (SCHOOL_LEVEL = High) with 100 or more students (use TOTAL field for student count)

**ANSWER:** 
```
SELECT *
FROM schools
WHERE LSTATE = 'WA' and SCHOOL_LEVEL = 'High' and TOTAL >= 100
```
>*Notes: There should be 393 rows in the file
This tests their ability to filter and find the correct fields. We might add a filter to see if they can do a filter on whether a field contains a text string, or maybe some kind of combination of AND/OR that is more complicated.*

**QUESTION 2:** From the result you got in question 1 (table name is q1), select only the fields in the list below, and rename the TOTFRL to "STUDENTS_IN_POVERTY" and the TOTAL Column to "TOTAL STUDENTS". Field list: LEAID, LEA_NAME, SCH_NAME, TOTFRL, G09, G10, G11, G12, G13, UG, AE, TOTAL

**ANSWER:** 
```
SELECT
LEAID
, LEA_NAME
, SCH_NAME
, TOTFRL AS STUDENTS_IN_POVERTY
, G09
, G10
, G11
, G12
, G13
, UG
, AE
, TOTAL AS TOTAL_STUDENTS
FROM q1
```

>*Notes: This test their ability to select specific fields and rename fields. It also calls out the fields to use for the next exercise*

**QUESTION 3:**  From the result you got in question 2 (table name q2), calculate the percent of Students in Poverty (STUDENTS_IN_POVERTY/TOTAL_STUDENTS) for each school, add it to the file and name it POVERTY_RATE. Ensure that schools with missing poverty numbers are interpreted as 0.

**ANSWER:** 
```
SELECT *
, CASE WHEN TOTAL_STUDENTS>0 
THEN COALESCE(STUDENTS_IN_POVERTY, 0)/TOTAL_STUDENTS 
ELSE 0 
END AS POVERTY_RATE
FROM q2
```

>*Notes: This tests their ability to do calculations and accomodate missing values. The CASE statement is unnecessary because we previously filtered on schools with more than 100 students. It would be necessary only if there were rows with 0 or null in the TOTAL_STUDENTS column.  We could decide not to do the 100+ student filter in the first step to see if they avoid the division by 0. The coalesce is there to make the percentage 0 if the field is null. Ideally, they would need to add some way to account for 0 students in poverty if the field is null. Coalesce is one way, another would be another case statement. They could also list out all the fields instead of using the asterisk.*

**QUESTION 4a:** From the result you got in question 3 (table name q3), create a file with one row per school district (LEAID and LEA_NAME), aggregating the totals for each grade level (G09, G10, G11, G12, G13, UG, AE), the total number of students in poverty, and the total enrollment overall. Calculate the poverty rate for the district by dividing the total number of students in poverty by the total enrollment. Also calculate the average of the school poverty rates for the district. Name the district totals the same as the original column name, the district poverty rate as DISTRICT_POVERTY_RATE and the average school poverty rate as AVG_SCHOOL_POVERTY_RATE. Round both poverty rates to the third decimal place

**ANSWER:** 
```
SELECT LEAID
, LEA_NAME
, SUM(G09) AS G09
, SUM(G10) AS G10
, SUM(G11) AS G11
, SUM(G12) AS G12
, SUM(G13) AS G13
, SUM(UG) AS UG 
, SUM(AE) AS AE
, SUM(TOTAL_STUDENTS) AS TOTAL_STUDENTS 
, SUM(STUDENTS_IN_POVERTY) AS STUDENTS_IN_POVERTY
, ROUND(SUM(COALESCE(STUDENTS_IN_POVERTY,0))/SUM(TOTAL_STUDENTS), 3) AS DISTRICT_POVERTY_RATE
, ROUND(AVG(POVERTY_RATE),3) as AVG_SCHOOL_POVERTY_RATE
FROM q3
GROUP BY LEAID, LEA_NAME
```
>*Notes: This tests their ability to aggregate (which would be needed sometimes for data analysis and for creating views in a data warehouse), and do calculations.*

**QUESTION 4b:** Using the file from question 3 (table name q3), create a file with one row per LEAID, LEA_NAME, SCHOOL_NAME and grade level. Include the LEAID, LEA_NAME and SCHOOL_NAME fields in the final file, adding a GRADE_LEVEL field (containing the grade level name) and an ENROLLMENT field with the number of students in that grade column (G09, G10, G11, G12, G13, UG, AE).

**ANSWER:** 
```
SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '09' AS GRADE_LEVEL
, G09 AS ENROLLMENT
FROM  q3

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '10' AS GRADE_LEVEL
, G10 AS ENROLLMENT
FROM  q3

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '11' AS GRADE_LEVEL
, G11 AS ENROLLMENT
FROM  q3

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '12' AS GRADE_LEVEL
, G12 AS ENROLLMENT
FROM  q3

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, 'UG' AS GRADE_LEVEL
, UG AS ENROLLMENT
FROM  q3

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, 'AE' AS GRADE_LEVEL
, AE AS ENROLLMENT
FROM  q3
```

>*Notes: This tests their ability to reformat files in a way that is structured differently than the original file (from columns to rows). This would be useful to prep data for analysis, or for creating views in a data warehouse. Tests their knowledge of union, their ability to create fields by manually entering a static value, their ability to combine multiple files together that are formatted similarly, and their ability to do subqueries.* 

**QUESTION 5:** Add the district poverty rate from Question 4a (table name q4a) to every row of the the file from question 4b (table name q4b) for that district (linked by LEAID). Include all columns and rows from 4a and DISTRICT_POVERTY_RATE from 4b

**ANSWER:**
```
SELECT 
q4b.*
, DISTRICT_POVERTY_RATE
FROM q4b
LEFT JOIN q4a on q4a.LEAID = q4b.LEAID
```

>*Notes: This tests their ability to join datasets. We could also use an inner join or a left join in this case, or ask them to join to a subquery or common table expression (CTE) to make this more complicated and test join knowledge. They could list out all the fields or use the * with the table name listed and get the same result.*

**QUESTION 6:** Add the STATE field (LSTATE) and Zip Code field (LZIP) from the original schools table to the result from question 5 (linked by LEA_ID and SCHOOL_NAME). Include all records from the question 5 result and only those from the original file that match. Also calculate the state poverty rate, round it to 4 decimal points, and add it as a field named "STATE_POVERTY_RATE". Poverty rate is defined as the sum of the students in poverty (TOTFRL) divided by the total enrollment (TOTAL). Create a field named POVERTY_COMPARE_TO_STATE. Make the value "ABOVE" if the school has a poverty rate equal to or higher than the state and "BELOW" if the poverty rate is lower than the state. 

**ANSWER:**
```
WITH state AS 
(SELECT 
    ROUND(SUM(TOTFRL)/SUM(TOTAL) 
    , 4) as STATE_POVERTY_RATE
FROM schools
)

SELECT q5.*
, schools.LSTATE
, schools.LZIP
, state.STATE_POVERTY_RATE
, CASE WHEN DISTRICT_POVERTY_RATE>= STATE_POVERTY_RATE THEN 'ABOVE'
    WHEN DISTRICT_POVERTY_RATE < STATE_POVERTY_RATE THEN 'BELOW'
    END AS POVERTY_COMPARE_TO_STATE
FROM q5
LEFT JOIN schools on q5.LEAID = schools.LEAID and q5.SCH_NAME = schools.SCH_NAME 
JOIN state on 1=1 
```
>*Notes: This tests their ability to join datasets using multiple criteria, it also tests their ability to use a subquery, and their ability to join when they do not have primary key. It also tests their ability to do a calculation and use a case statement, in case they have not chosen to use that earlier in the exercise*


**QUESTION 7:** Create a query that tells me the count of schools (name the field COUNT) from the result of question 6 (table name q6) that have a poverty rate equal to or higher than the state poverty rate. Note that school names are not unique, so a unique identifier would be a combination of the SCH_NAME and LEAID. 

**ANSWER:**
```
SELECT 
COUNT(DISTINCT (LEAID||SCH_NAME)) AS COUNT
FROM q6
WHERE POVERTY_COMPARE_TO_STATE = 'ABOVE'
```

>*Notes: I just added this one as a quick way to see if they got the same answer I did. There should be 196 schools with >100 enrollment and a district poverty rate higher than the state*
