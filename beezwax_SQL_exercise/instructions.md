***Beezwax SQL Exercise***

Dataset: Public School Characteristics 
https://catalog.data.gov/dataset/public-school-characteristics-2020-21 

**QUESTION 1:** Filter the file to just Washington (LSTATE) State High Schools (SCHOOL_LEVEL = High) with 100 or more students (use TOTAL field for student count)

**ANSWER:** 
>SELECT *
<br>FROM [original file]
<br>WHERE LSTATE = 'WA' and SCHOOL_LEVEL = 'High' and TOTAL >= 100

There should be 390 rows in the file

**QUESTION 2:** Select only the fields in the list below, and rename the TOTFRL to "STUDENTS_IN_POVERTY" and the TOTAL Column to "TOTAL STUDENTS"
Field list: LEAID, LEA_NAME, SCH_NAME, TOTFRL, G09, G10, G11, G12, G13, UG, AE, TOTAL

**ANSWER:** 
>SELECT
<br>LEAID
<br>, LEA_NAME
<br>, SCH_NAME
<br>, TOTFRL AS STUDENTS_IN_POVERTY
<br>, G09
<br>, G10
<br>, G11
<br>, G12
<br>, G13
<br>, UG
<br>, AE
<br>, TOTAL AS TOTAL_STUDENTS
<br>FROM [q1 dataset]

**QUESTION 3:** Calculate the percent of Students in Poverty (STUDENTS_IN_POVERTY/TOTAL_STUDENTS) for each school and name it POVERTY_RATE.

**ANSWER:** 
>SELECT *
<br>, CASE WHEN TOTAL_STUDENTS>0 
<br>THEN STUDENTS_IN_POVERTY/TOTAL_STUDENTS 
<br>ELSE 0 
<br>END AS POVERTY_RATE
<br>FROM [q2 dataset]

*Note: The CASE statement is unnecessary because we previously filtered on schools with more than 100 students. It would be necessary only if there were rows with 0 or null in the TOTAL_STUDENTS column.*

**QUESTION 4a:** Create a file with one row per school district (LEAID), summing the columns for each grade level (G09, G10, G11, G12, G13, UG, AE) and the total number of students in poverty and total enrollment overall. Calculate the poverty rate for the district, as well as it's average school poverty rate. Name the district totals the same as the original column name, the district poverty rate as DISTRICT_POVERTY_RATE and the average school poverty rate as AVG_SCHOOL_POVERTY_RATE

**ANSWER:** 
>SELECT
<br>LEAID
<br>, SUM(G09) AS G09
<br>, SUM(G10) AS G10
<br>, SUM(G11) AS G11
<br>, SUM(G12) AS G12
<br>, SUM(G13) AS G13
<br>, SUM(UG) AS UG
<br>, SUM(AE) AS AE
<br>, SUM(TOTAL_STUDENTS) AS TOTAL_STUDENTS
<br>, SUM(STUDENTS_IN_POVERTY) AS STUDENTS_IN_POVERTY
<br>, SUM(STUDENTS_IN_POVERTY)/SUM(TOTAL_STUDENTS) AS DISTRICT_POVERTY_RATE
<br>, AVG(POVERTY_RATE) as AVG_SCHOOL_POVERTY_RATE
<br>FROM [q3 dataset]
<br>GROUP BY LEAID


**QUESTION 4b:** Using the file from q3, create a file with one row per LEAID, LEA_NAME, SCHOOL_ID and grade level. Include the LEAID, LEA_NAME and SCHOOL_NAME fields in the final file, adding a GRADE_LEVEL field and an ENROLLMENT field with the number in each grade column (G09, G10, G11, G12, G13, UG, AE).

**ANSWER:** 
>SELECT
<br>LEA_NAME
<br>, SCH_NAME
<br>, '09' AS GRADE_LEVEL
<br>, G09 AS ENROLLMENT
<br>FROM  [q3 dataset]
<br>
<br>UNION
<br>
<br>SELECT
<br>LEA_NAME
<br>, SCH_NAME
<br>, '10' AS GRADE_LEVEL
<br>, G10 AS ENROLLMENT
<br>FROM  [q3 dataset]
<br>
<br>UNION
<br>
<br>SELECT
<br>LEA_NAME
<br>, SCH_NAME
<br>, '11' AS GRADE_LEVEL
<br>, G11 AS ENROLLMENT
<br>FROM  [q3 dataset]
<br>
<br>UNION
<br>
<br>SELECT
<br>LEA_NAME
<br>, SCH_NAME
<br>, '12' AS GRADE_LEVEL
<br>, G12 AS ENROLLMENT
<br>FROM  [q3 dataset]
<br>
<br>UNION
<br>
<br>SELECT
<br>LEA_NAME
<br>, SCH_NAME
<br>, 'UG' AS GRADE_LEVEL
<br>, UG AS ENROLLMENT
<br>FROM  [q3 dataset]
<br>
<br>UNION
<br>
<br>SELECT
<br>LEA_NAME
<br>, SCH_NAME
<br>, 'AE' AS GRADE_LEVEL
<br>, AE AS ENROLLMENT
<br>FROM  [q3 dataset]
<br><br>




__________________________________________________________
**OTHER DATASET IDEAS** 

Zip Code Data 
https://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-2020-zip-code-data-soi

Steven Seagal Movie box office numbers 
https://data.world/14thlevelcleric/caseys-money 

Global Superstore
https://data.world/2918diy/global-superstore