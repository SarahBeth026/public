##***Beezwax SQL Exercise***

Dataset: Public School Characteristics 
https://catalog.data.gov/dataset/public-school-characteristics-2020-21 

**QUESTION 1:** Filter the file to just Washington (LSTATE) State High Schools (SCHOOL_LEVEL = High) with 100 or more students (use TOTAL field for student count)

**ANSWER:** 
```
SELECT *
FROM [original file]
WHERE LSTATE = 'WA' and SCHOOL_LEVEL = 'High' and TOTAL >= 100
```
There should be 390 rows in the file

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

**QUESTION 3:** Calculate the percent of Students in Poverty (STUDENTS_IN_POVERTY/TOTAL_STUDENTS) for each school and name it POVERTY_RATE.

**ANSWER:** 
```
SELECT *
, CASE WHEN TOTAL_STUDENTS>0 
THEN COALESCE(STUDENTS_IN_POVERTY, 0)/TOTAL_STUDENTS 
ELSE 0 
END AS POVERTY_RATE
FROM [q2 dataset]
```

*Note: The CASE statement is unnecessary because we previously filtered on schools with more than 100 students. It would be necessary only if there were rows with 0 or null in the TOTAL_STUDENTS column. The coalesce is there to make the percentage 0 if the field is null. Ideally, they would need to add some way to account for 0 students in poverty if the field is null. Coalesce is one way, another would be a case statement.*

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

**QUESTION 4b:** Using the file from q3, create a file with one row per LEAID, LEA_NAME, SCHOOL_ID and grade level. Include the LEAID, LEA_NAME and SCHOOL_NAME fields in the final file, adding a GRADE_LEVEL field and an ENROLLMENT field with the number in each grade column (G09, G10, G11, G12, G13, UG, AE).

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

**QUESTION 5:** Add the district poverty rate from Q4a to every row of the Q4b file for that district (LEAID). Include all columns and rows from 4a and DISTRICT_POVERTY_RATE from 4b

**ANSWER:**
```
SELECT 
q4a.*
, DISTRICT_POVERTY_RATE
FROM q4a
LEFT JOIN q4b on q4a.LEAID = q4b.LEAID
```

*Note: could list out all the fields or use the * with the table name listed.Could also use an inner join or a left join in this case. We could make this more complicated to test join knowledge.*

__________________________________________________________
**OTHER DATASET IDEAS** 

Zip Code Data 
https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2020-zip-code-data-soi

Steven Seagal Movie box office numbers 
https://data.world/14thlevelcleric/caseys-money 

Global Superstore
https://data.world/2918diy/global-superstore