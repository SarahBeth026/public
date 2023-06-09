***Beezwax SQL Exercise***
--------------

Dataset: Public School Characteristics 
https://catalog.data.gov/dataset/public-school-characteristics-2020-21 

**QUESTION 1:** Filter the file to just Washington (LSTATE) State High Schools (SCHOOL_LEVEL = High) with 100 or more students (use TOTAL field for student count)

**ANSWER:** 
```
SELECT *
FROM [original file]
WHERE LSTATE = 'WA' and SCHOOL_LEVEL = 'High' and TOTAL >= 100
```
>*Notes: There should be 390 rows in the file
This tests their ability to filter and find the correct fields. We might add a filter to see if they can do a filter on whether a field contains a text string, or maybe some kind of combination of AND/OR that is more complicated.*

**QUESTION 2:** Select only the fields in the list below, and rename the TOTFRL to "STUDENTS_IN_POVERTY" and the TOTAL Column to "TOTAL STUDENTS"
Field list: LEAID, LEA_NAME, SCH_NAME, TOTFRL, G09, G10, G11, G12, G13, UG, AE, TOTAL

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
FROM [q1 dataset]
```

>*Notes: This test their ability to select specific fields and rename fields. It also calls out the fields to use for the next exercise*

**QUESTION 3:** Calculate the percent of Students in Poverty (STUDENTS_IN_POVERTY/TOTAL_STUDENTS) for each school and name it POVERTY_RATE. Ensure that schools with missing poverty numbers are interpreted as 0. 

**ANSWER:** 
```
SELECT *
, CASE WHEN TOTAL_STUDENTS>0 
THEN COALESCE(STUDENTS_IN_POVERTY, 0)/TOTAL_STUDENTS 
ELSE 0 
END AS POVERTY_RATE
FROM [q2 dataset]
```

>*Notes: This tests their ability to do calculations and accomodate missing values. The CASE statement is unnecessary because we previously filtered on schools with more than 100 students. It would be necessary only if there were rows with 0 or null in the TOTAL_STUDENTS column.  We could decide not to do the 100+ student filter in the first step to see if they avoid the division by 0. The coalesce is there to make the percentage 0 if the field is null. Ideally, they would need to add some way to account for 0 students in poverty if the field is null. Coalesce is one way, another would be another case statement. They could also list out all the fields instead of using the asterisk.*

**QUESTION 4a:** Create a file with one row per school district (LEAID), summing the columns for each grade level (G09, G10, G11, G12, G13, UG, AE) and the total number of students in poverty and total enrollment overall. Calculate the poverty rate for the district, as well as it's average school poverty rate. Name the district totals the same as the original column name, the district poverty rate as DISTRICT_POVERTY_RATE and the average school poverty rate as AVG_SCHOOL_POVERTY_RATE

**ANSWER:** 
```
SELECT
LEAID
, SUM(G09) AS G09
, SUM(G10) AS G10
, SUM(G11) AS G11
, SUM(G12) AS G12
, SUM(G13) AS G13
, SUM(UG) AS UG
, SUM(AE) AS AE
, SUM(TOTAL_STUDENTS) AS TOTAL_STUDENTS
, SUM(STUDENTS_IN_POVERTY) AS STUDENTS_IN_POVERTY
, SUM(STUDENTS_IN_POVERTY)/SUM(TOTAL_STUDENTS) AS DISTRICT_POVERTY_RATE
, AVG(POVERTY_RATE) as AVG_SCHOOL_POVERTY_RATE
FROM [q3 dataset]
GROUP BY LEAID
```
>*Notes: This tests their ability to aggregate (which would be needed sometimes for data analysis and for creating views in a data warehouse), and do calculations.*

**QUESTION 4b:** Using the file from q3, create a file with one row per LEAID, LEA_NAME, SCHOOL_NAME and grade level. Include the LEAID, LEA_NAME and SCHOOL_NAME fields in the final file, adding a GRADE_LEVEL field and an ENROLLMENT field with the number of students in each grade column (G09, G10, G11, G12, G13, UG, AE).

**ANSWER:** 
```
SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '09' AS GRADE_LEVEL
, G09 AS ENROLLMENT
FROM  [q3 dataset]

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '10' AS GRADE_LEVEL
, G10 AS ENROLLMENT
FROM  [q3 dataset]

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '11' AS GRADE_LEVEL
, G11 AS ENROLLMENT
FROM  [q3 dataset]

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, '12' AS GRADE_LEVEL
, G12 AS ENROLLMENT
FROM  [q3 dataset]

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, 'UG' AS GRADE_LEVEL
, UG AS ENROLLMENT
FROM  [q3 dataset]

UNION

SELECT
LEAID
, LEA_NAME
, SCH_NAME
, 'AE' AS GRADE_LEVEL
, AE AS ENROLLMENT
FROM  [q3 dataset]
```

>*Notes: This tests their ability to reformat files in a way that is structured differently than the original file (from columns to rows). This would be useful to prep data for analysis, or for creating views in a data warehouse. Tests their knowledge of union, their ability to create fields by manually entering a static value, their ability to combine multiple files together that are formatted similarly, and their ability to do subqueries.* 

**QUESTION 5:** Add the district poverty rate from Q4a to every row of the Q4b file for that district (LEAID). Include all columns and rows from 4a and DISTRICT_POVERTY_RATE from 4b

**ANSWER:**
```
SELECT 
q4a.*
, DISTRICT_POVERTY_RATE
FROM q4a
LEFT JOIN q4b on q4a.LEAID = q4b.LEAID
```

*Notes: This tests their ability to join datasets. We could also use an inner join or a left join in this case, or ask them to join to a subquery or common table expression (CTE) to make this more complicated and test join knowledge. They could list out all the fields or use the * with the table name listed and get the same result.*

__________________________________________________________
**OTHER DATASET IDEAS** 

Zip Code Data 
https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2020-zip-code-data-soi

Steven Seagal Movie box office numbers 
https://data.world/14thlevelcleric/caseys-money 

Global Superstore
https://data.world/2918diy/global-superstore