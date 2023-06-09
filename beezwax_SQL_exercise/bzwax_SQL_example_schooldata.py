import pandas as pd
import pandasql as psql

#put file location here## 
github_file_folder = r'C:\Users\sbanks\OneDrive - World Vision US\Documents\GitHub\public\beezwax_SQL_exercise'
import_file_location = f'{github_file_folder}\\Public_School_Characteristics_2020-21.csv'

schools = pd.read_csv(import_file_location, low_memory = False)

print(f"File imported: " + str(len(schools.index)) + " rows")

###QUESTION 1: Filter the file to just Washington (LSTATE) State High Schools (SCHOOL_LEVEL = High) with 100 or more students (use TOTAL field for student count)# 

###ANSWER: in between triple quotations below.

q1 = psql.sqldf("""
SELECT * 
FROM schools 
WHERE LSTATE = 'WA' and SCHOOL_LEVEL = 'High' and TOTAL >= 100
""")

print(f"There are " + str(len(q1.index)) + " High Schools in Washington with more than 100 students")

q1_save_location = f'{github_file_folder}\q1.csv'
q1.to_csv(q1_save_location, index=False)
print(f"Q1 Result saved to " + q1_save_location)

###QUESTION 2: Select only the following fields and rename the TOTFRL to "STUDENTS_IN_POVERTY" and the TOTAL Column to "TOTAL STUDENTS"
#LEAID, LEA_NAME, SCH_NAME, TOTFRL, G09, G10, G11, G12, G13, UG, AE, TOTAL

###ANSWER: in between triple quotations below.
q2 = psql.sqldf("""
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
""")

q2_save_location = f'{github_file_folder}\q2.csv'
q2.to_csv(q2_save_location, index=False)
print(f"Q2 Result saved to " + q2_save_location)

###QUESTION 3: Calculate the percent of Students in Poverty (STUDENTS_IN_POVERTY/TOTAL_STUDENTS) for each school and name it POVERTY_RATE. 

###ANSWER: in between triple quotations below.
q3 = psql.sqldf("""
SELECT *
, CASE WHEN TOTAL_STUDENTS>0 THEN COALESCE(STUDENTS_IN_POVERTY, 0)/TOTAL_STUDENTS ELSE 0 END AS POVERTY_RATE
FROM q2
""")
### Note - ideally the case statement would be there, but since we already filtered to schools with >100 total students, the division without the case statement would be fine##
#Ideally, they would need to add some way to account for 0 students in poverty if the field is blank. Coalesce is one way, another would be a case statement. 

q3_save_location = f'{github_file_folder}\q3.csv'
q3.to_csv(q3_save_location, index=False)
print(f"Q3 Result saved to " + q3_save_location)

###QUESTION 4a: Create a file with one row per school district (LEAID and LEA_NAME), summing the columns for each grade level (G09, G10, G11, G12, G13, UG, AE) and the total number of students in poverty and total enrollment overall. 
#Calculate the poverty rate for the district, as well as it's average school poverty rate. Name the district totals the same as the original column name, the district poverty rate as DISTRICT_POVERTY_RATE and the average school poverty rate as AVG_SCHOOL_POVERTY_RATE.
#ROUND both poverty rates to the third decimal place

###ANSWER: in between triple quotations below.
q4a = psql.sqldf("""
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
""")

q4a_save_location = f'{github_file_folder}\q4a.csv'
q4a.to_csv(q4a_save_location, index=False)
print(f"Q4a Result saved to " + q4a_save_location)

###QUESTION 4b: Using the file from q3, create a file with one row per LEAID, LEA_NAME, SCHOOL_ID and grade level. Include the LEAID, LEA_NAME and SCHOOL_NAME fields in the final file, adding a GRADE_LEVEL field and an ENROLLMENT field with the number in each grade column (G09, G10, G11, G12, G13, UG, AE).

###ANSWER: in between triple quotations below.
q4b = psql.sqldf("""
SELECT 
LEAID
, LEA_NAME
, SCH_NAME
, '09' AS GRADE_LEVEL
, G09 AS ENROLLMENT 
FROM q3

UNION 

SELECT 
LEAID
, LEA_NAME
, SCH_NAME
, '10' AS GRADE_LEVEL
, G10 AS ENROLLMENT 
FROM q3

UNION 

SELECT 
LEAID
, LEA_NAME
, SCH_NAME
, '11' AS GRADE_LEVEL
, G11 AS ENROLLMENT 
FROM q3

UNION 

SELECT 
LEAID
, LEA_NAME
, SCH_NAME
, '12' AS GRADE_LEVEL
, G12 AS ENROLLMENT 
FROM q3

UNION 

SELECT 
LEAID
, LEA_NAME
, SCH_NAME
, 'UG' AS GRADE_LEVEL
, UG AS ENROLLMENT 
FROM q3

UNION 

SELECT 
LEAID
, LEA_NAME
, SCH_NAME
, 'AE' AS GRADE_LEVEL
, AE AS ENROLLMENT 
FROM q3
""")

q4b_save_location = f'{github_file_folder}\q4b.csv'
q4b.to_csv(q4b_save_location, index=False)
print(f"Q4b Result saved to " + q4b_save_location)

###QUESTION 5: Add the district poverty rate from Q4a to every row of the Q4b file for that district (LEAID). Include all columns and rows from 4b and DISTRICT_POVERTY_RATE from 4a

###ANSWER: in between triple quotations below.

q5 = psql.sqldf("""
SELECT q4b.*
, DISTRICT_POVERTY_RATE
FROM q4b
LEFT JOIN q4a on q4a.LEAID = q4b.LEAID
""")

q5_save_location = f'{github_file_folder}\q5.csv'
q5.to_csv(q5_save_location, index=False)
print(f"Q5 Result saved to " + q5_save_location)

#Note: could use an inner join or a left join in this case. We could make this more complicated to test join knowledge.
#Note: could list out all the fields or use the * with the table name listed.   