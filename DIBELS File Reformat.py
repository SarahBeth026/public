### Creates a simplified DIBELS file with one row per subtest/grade/administration based off of the original file from the vendor###
import datetime
import pandas as pd
import pandasql as psql

now = datetime.datetime.now()
print ("Start date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

##Put the location of the original DIBELS file here (must be in excel format)
input_file_location_xl = r'C:\Users\sbanks\Downloads\DataFarming_PeninsulaSchoolDistrict_K-6_2020-2022_DIBELS8thEdition_Confidential_589042640.xlsx'
##Final location of output file
output_file_location = r"C:\Users\sbanks\Downloads\DIBELS8th.csv"

input = pd.read_excel(input_file_location_xl)

print(f"DIBELS file imported " + str(len(input.index)) + " rows")

print ("Formatting Kindergarten Scores...")

LNF_K_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'LNF' AS Subtest
,'Beginning' AS Administration
,Form_LNF_K_Beginning AS Test_Form
,Date_LNF_K_Beginning AS Test_Date
,Remote_LNF_K_Beginning AS Test_Remote
,LNF_K_Beginning AS Test_Score
,Benchmark_Status_LNF_K_Beginning AS Benchmark_Status
,National_DDS_Percentile_LNF_K_Beginning AS National_DDS_Percentile
,School_Percentile_LNF_K_Beginning AS School_Percentile
,District_Percentile_LNF_K_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

PSF_K_Beginning =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'PSF' AS Subtest
,'Beginning' AS Administration
,Form_PSF_K_Beginning AS Test_Form
,Date_PSF_K_Beginning AS Test_Date
,Remote_PSF_K_Beginning AS Test_Remote
,PSF_K_Beginning AS Test_Score
,Benchmark_Status_PSF_K_Beginning as Benchmark_Status
,National_DDS_Percentile_PSF_K_Beginning AS National_DDS_Percentile
,School_Percentile_PSF_K_Beginning AS School_Percentile
,District_Percentile_PSF_K_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

NWF_CLS_K_Beginning =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'NWF-CLS' AS Subtest
,'Beginning' AS Administration
,Form_NWF_K_Beginning AS Test_Form
,Date_NWF_K_Beginning AS Test_Date
,Remote_NWF_K_Beginning AS Test_Remote
,"NWF-CLS_K_Beginning" AS Test_Score
,"Benchmark_Status_NWF-CLS_K_Beginning" as Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_K_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_K_Beginning" AS School_Percentile
,"District_Percentile_NWF-CLS_K_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

NWF_WRF_K_Beginning =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'NWF-WRF' AS Subtest
,'Beginning' AS Administration
,Form_NWF_K_Beginning AS Test_Form
,Date_NWF_K_Beginning AS Test_Date
,Remote_NWF_K_Beginning AS Test_Remote
,"NWF-WRC_K_Beginning" AS Test_Score
,"Benchmark_Status_NWF-WRC_K_Beginning" as Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_K_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_K_Beginning" AS School_Percentile
,"District_Percentile_NWF-WRC_K_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

WRF_K_Beginning =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'WRF' AS Subtest
,'Beginning' AS Administration
,Form_WRF_K_Beginning AS Test_Form
,Date_WRF_K_Beginning AS Test_Date
,Remote_WRF_K_Beginning AS Test_Remote
,WRF_K_Beginning AS Test_Score
,Benchmark_Status_WRF_K_Beginning as Benchmark_Status
,National_DDS_Percentile_WRF_K_Beginning AS National_DDS_Percentile
,School_Percentile_WRF_K_Beginning AS School_Percentile
,District_Percentile_WRF_K_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

Composite_K_Beginning =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
, Null AS Test_Form
,Date_Composite_K_Beginning AS Test_Date
, NULL AS Test_Remote
,Composite_K_Beginning AS Test_Score
,Benchmark_Status_Composite_K_Beginning as Benchmark_Status
,National_DDS_Percentile_Composite_K_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_K_Beginning AS School_Percentile
,District_Percentile_Composite_K_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

K_Beginning_Scores = pd.concat([LNF_K_Beginning,PSF_K_Beginning,NWF_CLS_K_Beginning, NWF_WRF_K_Beginning, WRF_K_Beginning, Composite_K_Beginning])

LNF_K_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'LNF' AS Subtest
,'Middle' AS Administration
,Form_LNF_K_Middle AS Test_Form
,Date_LNF_K_Middle AS Test_Date
,Remote_LNF_K_Middle AS Test_Remote
,LNF_K_Middle AS Test_Score
,Benchmark_Status_LNF_K_Middle AS Benchmark_Status
,National_DDS_Percentile_LNF_K_Middle AS National_DDS_Percentile
,School_Percentile_LNF_K_Middle AS School_Percentile
,District_Percentile_LNF_K_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

PSF_K_Middle =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'PSF' AS Subtest
,'Middle' AS Administration
,Form_PSF_K_Middle AS Test_Form
,Date_PSF_K_Middle AS Test_Date
,Remote_PSF_K_Middle AS Test_Remote
,PSF_K_Middle AS Test_Score
,Benchmark_Status_PSF_K_Middle as Benchmark_Status
,National_DDS_Percentile_PSF_K_Middle AS National_DDS_Percentile
,School_Percentile_PSF_K_Middle AS School_Percentile
,District_Percentile_PSF_K_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

NWF_CLS_K_Middle =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'NWF-CLS' AS Subtest
,'Middle' AS Administration
,Form_NWF_K_Middle AS Test_Form
,Date_NWF_K_Middle AS Test_Date
,Remote_NWF_K_Middle AS Test_Remote
,"NWF-CLS_K_Middle" AS Test_Score
,"Benchmark_Status_NWF-CLS_K_Middle" as Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_K_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_K_Middle" AS School_Percentile
,"District_Percentile_NWF-CLS_K_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

NWF_WRF_K_Middle =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'NWF-WRF' AS Subtest
,'Middle' AS Administration
,Form_NWF_K_Middle AS Test_Form
,Date_NWF_K_Middle AS Test_Date
,Remote_NWF_K_Middle AS Test_Remote
,"NWF-WRC_K_Middle" AS Test_Score
,"Benchmark_Status_NWF-WRC_K_Middle" as Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_K_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_K_Middle" AS School_Percentile
,"District_Percentile_NWF-WRC_K_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

WRF_K_Middle =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'WRF' AS Subtest
,'Middle' AS Administration
,Form_WRF_K_Middle AS Test_Form
,Date_WRF_K_Middle AS Test_Date
,Remote_WRF_K_Middle AS Test_Remote
,WRF_K_Middle AS Test_Score
,Benchmark_Status_WRF_K_Middle as Benchmark_Status
,National_DDS_Percentile_WRF_K_Middle AS National_DDS_Percentile
,School_Percentile_WRF_K_Middle AS School_Percentile
,District_Percentile_WRF_K_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

Composite_K_Middle =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
, Null AS Test_Form
,Date_Composite_K_Middle AS Test_Date
, NULL AS Test_Remote
,Composite_K_Middle AS Test_Score
,Benchmark_Status_Composite_K_Middle as Benchmark_Status
,National_DDS_Percentile_Composite_K_Middle AS National_DDS_Percentile
,School_Percentile_Composite_K_Middle AS School_Percentile
,District_Percentile_Composite_K_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

K_Middle_Scores = pd.concat([LNF_K_Middle,PSF_K_Middle,NWF_CLS_K_Middle, NWF_WRF_K_Middle, WRF_K_Middle, Composite_K_Middle])

LNF_K_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'LNF' AS Subtest
,'End' AS Administration
,Form_LNF_K_End AS Test_Form
,Date_LNF_K_End AS Test_Date
,Remote_LNF_K_End AS Test_Remote
,LNF_K_End AS Test_Score
,Benchmark_Status_LNF_K_End AS Benchmark_Status
,National_DDS_Percentile_LNF_K_End AS National_DDS_Percentile
,School_Percentile_LNF_K_End AS School_Percentile
,District_Percentile_LNF_K_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

PSF_K_End =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'PSF' AS Subtest
,'End' AS Administration
,Form_PSF_K_End AS Test_Form
,Date_PSF_K_End AS Test_Date
,Remote_PSF_K_End AS Test_Remote
,PSF_K_End AS Test_Score
,Benchmark_Status_PSF_K_End as Benchmark_Status
,National_DDS_Percentile_PSF_K_End AS National_DDS_Percentile
,School_Percentile_PSF_K_End AS School_Percentile
,District_Percentile_PSF_K_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

NWF_CLS_K_End =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'NWF-CLS' AS Subtest
,'End' AS Administration
,Form_NWF_K_End AS Test_Form
,Date_NWF_K_End AS Test_Date
,Remote_NWF_K_End AS Test_Remote
,"NWF-CLS_K_End" AS Test_Score
,"Benchmark_Status_NWF-CLS_K_End" as Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_K_End" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_K_End" AS School_Percentile
,"District_Percentile_NWF-CLS_K_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

NWF_WRF_K_End =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'NWF-WRF' AS Subtest
,'End' AS Administration
,Form_NWF_K_End AS Test_Form
,Date_NWF_K_End AS Test_Date
,Remote_NWF_K_End AS Test_Remote
,"NWF-WRC_K_End" AS Test_Score
,"Benchmark_Status_NWF-WRC_K_End" as Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_K_End" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_K_End" AS School_Percentile
,"District_Percentile_NWF-WRC_K_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

WRF_K_End =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'WRF' AS Subtest
,'End' AS Administration
,Form_WRF_K_End AS Test_Form
,Date_WRF_K_End AS Test_Date
,Remote_WRF_K_End AS Test_Remote
,WRF_K_End AS Test_Score
,Benchmark_Status_WRF_K_End as Benchmark_Status
,National_DDS_Percentile_WRF_K_End AS National_DDS_Percentile
,School_Percentile_WRF_K_End AS School_Percentile
,District_Percentile_WRF_K_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

Composite_K_End =  psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_K AS Year
,School_K AS School
,Class_K AS Class
,Secondary_Class_K AS Secondary_Class
,Teacher_K AS Teacher
,'K' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
, Null AS Test_Form
,Date_Composite_K_End AS Test_Date
, NULL AS Test_Remote
,Composite_K_End AS Test_Score
,Benchmark_Status_Composite_K_End as Benchmark_Status
,National_DDS_Percentile_Composite_K_End AS National_DDS_Percentile
,School_Percentile_Composite_K_End AS School_Percentile
,District_Percentile_Composite_K_End AS District_Percentile
,Growth_Goal_Composite_K_End AS Growth_Goal
,Growth_Goal_Type_Composite_K_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_K_End AS Growth_Goal_Met
,Growth_Percentile_Composite_K_End AS Growth_Percentile
,Months_of_Growth_Composite_K_End AS Months_of_Growth
FROM input
WHERE Year_K IS NOT NULL""")

K_End_Scores = pd.concat([LNF_K_End,PSF_K_End,NWF_CLS_K_End, NWF_WRF_K_End, WRF_K_End, Composite_K_End])

Scores_K = pd.concat([K_Beginning_Scores, K_Middle_Scores, K_End_Scores])

print ("Formatting 1st Grade Scores...")

LNF_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'LNF' AS Subtest
,'Beginning' AS Administration
,Form_LNF_1st_Beginning AS Test_Form
,Date_LNF_1st_Beginning AS Test_Date
,Remote_LNF_1st_Beginning AS Test_Remote
,LNF_1st_Beginning AS Test_Score
,Benchmark_Status_LNF_1st_Beginning AS Benchmark_Status
,National_DDS_Percentile_LNF_1st_Beginning AS National_DDS_Percentile
,School_Percentile_LNF_1st_Beginning AS School_Percentile
,District_Percentile_LNF_1st_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

PSF_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'PSF' AS Subtest
,'Beginning' AS Administration
,Form_PSF_1st_Beginning AS Test_Form
,Date_PSF_1st_Beginning AS Test_Date
,Remote_PSF_1st_Beginning AS Test_Remote
,PSF_1st_Beginning AS Test_Score
,Benchmark_Status_PSF_1st_Beginning AS Benchmark_Status
,National_DDS_Percentile_PSF_1st_Beginning AS National_DDS_Percentile
,School_Percentile_PSF_1st_Beginning AS School_Percentile
,District_Percentile_PSF_1st_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

NWF_CLS_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'NWF-CLS' AS Subtest
,'Beginning' AS Administration
,Form_NWF_1st_Beginning AS Test_Form
,Date_NWF_1st_Beginning AS Test_Date
,Remote_NWF_1st_Beginning AS Test_Remote
,"NWF-CLS_1st_Beginning" AS Test_Score
,"Benchmark_Status_NWF-CLS_1st_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_1st_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_1st_Beginning" AS School_Percentile
,"District_Percentile_NWF-CLS_1st_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

NWF_WRC_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'NWF-WRC' AS Subtest
,'Beginning' AS Administration
,Form_NWF_1st_Beginning AS Test_Form
,Date_NWF_1st_Beginning AS Test_Date
,Remote_NWF_1st_Beginning AS Test_Remote
,"NWF-WRC_1st_Beginning" AS Test_Score
,"Benchmark_Status_NWF-WRC_1st_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_1st_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_1st_Beginning" AS School_Percentile
,"District_Percentile_NWF-WRC_1st_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

WRF_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'WRF' AS Subtest
,'Beginning' AS Administration
,Form_WRF_1st_Beginning AS Test_Form
,Date_WRF_1st_Beginning AS Test_Date
,Remote_WRF_1st_Beginning AS Test_Remote
,WRF_1st_Beginning AS Test_Score
,Benchmark_Status_WRF_1st_Beginning AS Benchmark_Status
,National_DDS_Percentile_WRF_1st_Beginning AS National_DDS_Percentile
,School_Percentile_WRF_1st_Beginning AS School_Percentile
,District_Percentile_WRF_1st_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_WordsCorrect_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_1st_Beginning AS Test_Form
,Date_ORF_1st_Beginning AS Test_Date
,Remote_ORF_1st_Beginning AS Test_Remote
,"ORF-WordsCorrect_1st_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_1st_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_1st_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_1st_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_1st_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_Errors_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_1st_Beginning AS Test_Form
,Date_ORF_1st_Beginning AS Test_Date
,Remote_ORF_1st_Beginning AS Test_Remote
,"ORF-Errors_1st_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_1st_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_1st_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_Accuracy_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_1st_Beginning AS Test_Form
,Date_ORF_1st_Beginning AS Test_Date
,Remote_ORF_1st_Beginning AS Test_Remote
,"ORF-Accuracy_1st_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_1st_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_1st_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_1st_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_1st_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

Composite_1st_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_1st_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_1st_Beginning AS Test_Score
,Benchmark_Status_Composite_1st_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_1st_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_1st_Beginning AS School_Percentile
,District_Percentile_Composite_1st_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

Beginning_Scores_1st = pd.concat([LNF_1st_Beginning, PSF_1st_Beginning, NWF_CLS_1st_Beginning, NWF_WRC_1st_Beginning, WRF_1st_Beginning, ORF_WordsCorrect_1st_Beginning, ORF_Errors_1st_Beginning, ORF_Accuracy_1st_Beginning, Composite_1st_Beginning])

LNF_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'LNF' AS Subtest
,'Middle' AS Administration
,Form_LNF_1st_Middle AS Test_Form
,Date_LNF_1st_Middle AS Test_Date
,Remote_LNF_1st_Middle AS Test_Remote
,LNF_1st_Middle AS Test_Score
,Benchmark_Status_LNF_1st_Middle AS Benchmark_Status
,National_DDS_Percentile_LNF_1st_Middle AS National_DDS_Percentile
,School_Percentile_LNF_1st_Middle AS School_Percentile
,District_Percentile_LNF_1st_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

PSF_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'PSF' AS Subtest
,'Middle' AS Administration
,Form_PSF_1st_Middle AS Test_Form
,Date_PSF_1st_Middle AS Test_Date
,Remote_PSF_1st_Middle AS Test_Remote
,PSF_1st_Middle AS Test_Score
,Benchmark_Status_PSF_1st_Middle AS Benchmark_Status
,National_DDS_Percentile_PSF_1st_Middle AS National_DDS_Percentile
,School_Percentile_PSF_1st_Middle AS School_Percentile
,District_Percentile_PSF_1st_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

NWF_CLS_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'NWF-CLS' AS Subtest
,'Middle' AS Administration
,Form_NWF_1st_Middle AS Test_Form
,Date_NWF_1st_Middle AS Test_Date
,Remote_NWF_1st_Middle AS Test_Remote
,"NWF-CLS_1st_Middle" AS Test_Score
,"Benchmark_Status_NWF-CLS_1st_Middle" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_1st_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_1st_Middle" AS School_Percentile
,"District_Percentile_NWF-CLS_1st_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

NWF_WRC_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'NWF-WRC' AS Subtest
,'Middle' AS Administration
,Form_NWF_1st_Middle AS Test_Form
,Date_NWF_1st_Middle AS Test_Date
,Remote_NWF_1st_Middle AS Test_Remote
,"NWF-WRC_1st_Middle" AS Test_Score
,"Benchmark_Status_NWF-WRC_1st_Middle" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_1st_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_1st_Middle" AS School_Percentile
,"District_Percentile_NWF-WRC_1st_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

WRF_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'WRF' AS Subtest
,'Middle' AS Administration
,Form_WRF_1st_Middle AS Test_Form
,Date_WRF_1st_Middle AS Test_Date
,Remote_WRF_1st_Middle AS Test_Remote
,WRF_1st_Middle AS Test_Score
,Benchmark_Status_WRF_1st_Middle AS Benchmark_Status
,National_DDS_Percentile_WRF_1st_Middle AS National_DDS_Percentile
,School_Percentile_WRF_1st_Middle AS School_Percentile
,District_Percentile_WRF_1st_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_WordsCorrect_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_1st_Middle AS Test_Form
,Date_ORF_1st_Middle AS Test_Date
,Remote_ORF_1st_Middle AS Test_Remote
,"ORF-WordsCorrect_1st_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_1st_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_1st_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_1st_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_1st_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_Errors_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_1st_Middle AS Test_Form
,Date_ORF_1st_Middle AS Test_Date
,Remote_ORF_1st_Middle AS Test_Remote
,"ORF-Errors_1st_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_1st_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_1st_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_Accuracy_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_1st_Middle AS Test_Form
,Date_ORF_1st_Middle AS Test_Date
,Remote_ORF_1st_Middle AS Test_Remote
,"ORF-Accuracy_1st_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_1st_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_1st_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_1st_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_1st_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

Composite_1st_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_1st_Middle AS Test_Date
,Null AS Test_Remote
,Composite_1st_Middle AS Test_Score
,Benchmark_Status_Composite_1st_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_1st_Middle AS National_DDS_Percentile
,School_Percentile_Composite_1st_Middle AS School_Percentile
,District_Percentile_Composite_1st_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

Middle_Scores_1st = pd.concat([LNF_1st_Middle, PSF_1st_Middle, NWF_CLS_1st_Middle, NWF_WRC_1st_Middle, WRF_1st_Middle, ORF_WordsCorrect_1st_Middle, ORF_Errors_1st_Middle, ORF_Accuracy_1st_Middle, Composite_1st_Middle])

LNF_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'LNF' AS Subtest
,'End' AS Administration
,Form_LNF_1st_End AS Test_Form
,Date_LNF_1st_End AS Test_Date
,Remote_LNF_1st_End AS Test_Remote
,LNF_1st_End AS Test_Score
,Benchmark_Status_LNF_1st_End AS Benchmark_Status
,National_DDS_Percentile_LNF_1st_End AS National_DDS_Percentile
,School_Percentile_LNF_1st_End AS School_Percentile
,District_Percentile_LNF_1st_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

PSF_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'PSF' AS Subtest
,'End' AS Administration
,Form_PSF_1st_End AS Test_Form
,Date_PSF_1st_End AS Test_Date
,Remote_PSF_1st_End AS Test_Remote
,PSF_1st_End AS Test_Score
,Benchmark_Status_PSF_1st_End AS Benchmark_Status
,National_DDS_Percentile_PSF_1st_End AS National_DDS_Percentile
,School_Percentile_PSF_1st_End AS School_Percentile
,District_Percentile_PSF_1st_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

NWF_CLS_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'NWF-CLS' AS Subtest
,'End' AS Administration
,Form_NWF_1st_End AS Test_Form
,Date_NWF_1st_End AS Test_Date
,Remote_NWF_1st_End AS Test_Remote
,"NWF-CLS_1st_End" AS Test_Score
,"Benchmark_Status_NWF-CLS_1st_End" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_1st_End" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_1st_End" AS School_Percentile
,"District_Percentile_NWF-CLS_1st_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

NWF_WRC_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'NWF-WRC' AS Subtest
,'End' AS Administration
,Form_NWF_1st_End AS Test_Form
,Date_NWF_1st_End AS Test_Date
,Remote_NWF_1st_End AS Test_Remote
,"NWF-WRC_1st_End" AS Test_Score
,"Benchmark_Status_NWF-WRC_1st_End" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_1st_End" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_1st_End" AS School_Percentile
,"District_Percentile_NWF-WRC_1st_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

WRF_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'WRF' AS Subtest
,'End' AS Administration
,Form_WRF_1st_End AS Test_Form
,Date_WRF_1st_End AS Test_Date
,Remote_WRF_1st_End AS Test_Remote
,WRF_1st_End AS Test_Score
,Benchmark_Status_WRF_1st_End AS Benchmark_Status
,National_DDS_Percentile_WRF_1st_End AS National_DDS_Percentile
,School_Percentile_WRF_1st_End AS School_Percentile
,District_Percentile_WRF_1st_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_WordsCorrect_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_1st_End AS Test_Form
,Date_ORF_1st_End AS Test_Date
,Remote_ORF_1st_End AS Test_Remote
,"ORF-WordsCorrect_1st_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_1st_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_1st_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_1st_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_1st_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_Errors_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_1st_End AS Test_Form
,Date_ORF_1st_End AS Test_Date
,Remote_ORF_1st_End AS Test_Remote
,"ORF-Errors_1st_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_1st_End" AS School_Percentile
,"District_Percentile_ORF-Errors_1st_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

ORF_Accuracy_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_1st_End AS Test_Form
,Date_ORF_1st_End AS Test_Date
,Remote_ORF_1st_End AS Test_Remote
,"ORF-Accuracy_1st_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_1st_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_1st_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_1st_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_1st_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

Composite_1st_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_1st AS Year
,School_1st AS School
,Class_1st AS Class
,Secondary_Class_1st AS Secondary_Class
,Teacher_1st AS Teacher
,'1st' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_1st_End AS Test_Date
,Null AS Test_Remote
,Composite_1st_End AS Test_Score
,Benchmark_Status_Composite_1st_End AS Benchmark_Status
,National_DDS_Percentile_Composite_1st_End AS National_DDS_Percentile
,School_Percentile_Composite_1st_End AS School_Percentile
,District_Percentile_Composite_1st_End AS District_Percentile
,Growth_Goal_Composite_1st_End AS Growth_Goal
,Growth_Goal_Type_Composite_1st_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_1st_End AS Growth_Goal_Met
,Growth_Percentile_Composite_1st_End AS Growth_Percentile
,Months_of_Growth_Composite_1st_End AS Months_of_Growth
FROM input
WHERE Year_1st IS NOT NULL""")

End_Scores_1st = pd.concat([LNF_1st_End, PSF_1st_End, NWF_CLS_1st_End, NWF_WRC_1st_End, WRF_1st_End, ORF_WordsCorrect_1st_End, ORF_Errors_1st_End, ORF_Accuracy_1st_End, Composite_1st_End])

Scores_1st = pd.concat([Beginning_Scores_1st, Middle_Scores_1st, End_Scores_1st])

print ("Formatting 2nd Grade Scores...")

NWF_CLS_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'NWF-CLS' AS Subtest
,'Beginning' AS Administration
,Form_NWF_2nd_Beginning AS Test_Form
,Date_NWF_2nd_Beginning AS Test_Date
,Remote_NWF_2nd_Beginning AS Test_Remote
,"NWF-CLS_2nd_Beginning" AS Test_Score
,"Benchmark_Status_NWF-CLS_2nd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_2nd_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_2nd_Beginning" AS School_Percentile
,"District_Percentile_NWF-CLS_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

NWF_WRC_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'NWF-WRC' AS Subtest
,'Beginning' AS Administration
,Form_NWF_2nd_Beginning AS Test_Form
,Date_NWF_2nd_Beginning AS Test_Date
,Remote_NWF_2nd_Beginning AS Test_Remote
,"NWF-WRC_2nd_Beginning" AS Test_Score
,"Benchmark_Status_NWF-WRC_2nd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_2nd_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_2nd_Beginning" AS School_Percentile
,"District_Percentile_NWF-WRC_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

WRF_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'WRF' AS Subtest
,'Beginning' AS Administration
,Form_WRF_2nd_Beginning AS Test_Form
,Date_WRF_2nd_Beginning AS Test_Date
,Remote_WRF_2nd_Beginning AS Test_Remote
,WRF_2nd_Beginning AS Test_Score
,Benchmark_Status_WRF_2nd_Beginning AS Benchmark_Status
,National_DDS_Percentile_WRF_2nd_Beginning AS National_DDS_Percentile
,School_Percentile_WRF_2nd_Beginning AS School_Percentile
,District_Percentile_WRF_2nd_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_WordsCorrect_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_2nd_Beginning AS Test_Form
,Date_ORF_2nd_Beginning AS Test_Date
,Remote_ORF_2nd_Beginning AS Test_Remote
,"ORF-WordsCorrect_2nd_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_2nd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_2nd_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_2nd_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_Errors_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_2nd_Beginning AS Test_Form
,Date_ORF_2nd_Beginning AS Test_Date
,Remote_ORF_2nd_Beginning AS Test_Remote
,"ORF-Errors_2nd_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_2nd_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_Accuracy_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_2nd_Beginning AS Test_Form
,Date_ORF_2nd_Beginning AS Test_Date
,Remote_ORF_2nd_Beginning AS Test_Remote
,"ORF-Accuracy_2nd_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_2nd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_2nd_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_2nd_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Correct_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Correct' AS Subtest
,'Beginning' AS Administration
,Form_Maze_2nd_Beginning AS Test_Form
,Date_Maze_2nd_Beginning AS Test_Date
,Remote_Maze_2nd_Beginning AS Test_Remote
,"Maze-Correct_2nd_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_2nd_Beginning" AS School_Percentile
,"District_Percentile_Maze-Correct_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Incorrect_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Beginning' AS Administration
,Form_Maze_2nd_Beginning AS Test_Form
,Date_Maze_2nd_Beginning AS Test_Date
,Remote_Maze_2nd_Beginning AS Test_Remote
,"Maze-Incorrect_2nd_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_2nd_Beginning" AS School_Percentile
,"District_Percentile_Maze-Incorrect_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Adjusted_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Beginning' AS Administration
,Form_Maze_2nd_Beginning AS Test_Form
,Date_Maze_2nd_Beginning AS Test_Date
,Remote_Maze_2nd_Beginning AS Test_Remote
,"Maze-Adjusted_2nd_Beginning" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_2nd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_2nd_Beginning" AS School_Percentile
,"District_Percentile_Maze-Adjusted_2nd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

Composite_2nd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_2nd_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_2nd_Beginning AS Test_Score
,Benchmark_Status_Composite_2nd_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_2nd_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_2nd_Beginning AS School_Percentile
,District_Percentile_Composite_2nd_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

Beginning_Scores_2nd = pd.concat([NWF_CLS_2nd_Beginning, NWF_WRC_2nd_Beginning, WRF_2nd_Beginning, ORF_WordsCorrect_2nd_Beginning, ORF_Errors_2nd_Beginning, ORF_Accuracy_2nd_Beginning, MAZE_Correct_2nd_Beginning, MAZE_Incorrect_2nd_Beginning, MAZE_Adjusted_2nd_Beginning, Composite_2nd_Beginning])

NWF_CLS_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'NWF-CLS' AS Subtest
,'Middle' AS Administration
,Form_NWF_2nd_Middle AS Test_Form
,Date_NWF_2nd_Middle AS Test_Date
,Remote_NWF_2nd_Middle AS Test_Remote
,"NWF-CLS_2nd_Middle" AS Test_Score
,"Benchmark_Status_NWF-CLS_2nd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_2nd_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_2nd_Middle" AS School_Percentile
,"District_Percentile_NWF-CLS_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

NWF_WRC_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'NWF-WRC' AS Subtest
,'Middle' AS Administration
,Form_NWF_2nd_Middle AS Test_Form
,Date_NWF_2nd_Middle AS Test_Date
,Remote_NWF_2nd_Middle AS Test_Remote
,"NWF-WRC_2nd_Middle" AS Test_Score
,"Benchmark_Status_NWF-WRC_2nd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_2nd_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_2nd_Middle" AS School_Percentile
,"District_Percentile_NWF-WRC_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

WRF_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'WRF' AS Subtest
,'Middle' AS Administration
,Form_WRF_2nd_Middle AS Test_Form
,Date_WRF_2nd_Middle AS Test_Date
,Remote_WRF_2nd_Middle AS Test_Remote
,WRF_2nd_Middle AS Test_Score
,Benchmark_Status_WRF_2nd_Middle AS Benchmark_Status
,National_DDS_Percentile_WRF_2nd_Middle AS National_DDS_Percentile
,School_Percentile_WRF_2nd_Middle AS School_Percentile
,District_Percentile_WRF_2nd_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_WordsCorrect_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_2nd_Middle AS Test_Form
,Date_ORF_2nd_Middle AS Test_Date
,Remote_ORF_2nd_Middle AS Test_Remote
,"ORF-WordsCorrect_2nd_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_2nd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_2nd_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_2nd_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_Errors_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_2nd_Middle AS Test_Form
,Date_ORF_2nd_Middle AS Test_Date
,Remote_ORF_2nd_Middle AS Test_Remote
,"ORF-Errors_2nd_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_2nd_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_Accuracy_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_2nd_Middle AS Test_Form
,Date_ORF_2nd_Middle AS Test_Date
,Remote_ORF_2nd_Middle AS Test_Remote
,"ORF-Accuracy_2nd_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_2nd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_2nd_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_2nd_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Correct_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Correct' AS Subtest
,'Middle' AS Administration
,Form_Maze_2nd_Middle AS Test_Form
,Date_Maze_2nd_Middle AS Test_Date
,Remote_Maze_2nd_Middle AS Test_Remote
,"Maze-Correct_2nd_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_2nd_Middle" AS School_Percentile
,"District_Percentile_Maze-Correct_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Incorrect_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Middle' AS Administration
,Form_Maze_2nd_Middle AS Test_Form
,Date_Maze_2nd_Middle AS Test_Date
,Remote_Maze_2nd_Middle AS Test_Remote
,"Maze-Incorrect_2nd_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_2nd_Middle" AS School_Percentile
,"District_Percentile_Maze-Incorrect_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Adjusted_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Middle' AS Administration
,Form_Maze_2nd_Middle AS Test_Form
,Date_Maze_2nd_Middle AS Test_Date
,Remote_Maze_2nd_Middle AS Test_Remote
,"Maze-Adjusted_2nd_Middle" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_2nd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_2nd_Middle" AS School_Percentile
,"District_Percentile_Maze-Adjusted_2nd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

Composite_2nd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_2nd_Middle AS Test_Date
,Null AS Test_Remote
,Composite_2nd_Middle AS Test_Score
,Benchmark_Status_Composite_2nd_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_2nd_Middle AS National_DDS_Percentile
,School_Percentile_Composite_2nd_Middle AS School_Percentile
,District_Percentile_Composite_2nd_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

Middle_Scores_2nd = pd.concat([NWF_CLS_2nd_Middle, NWF_WRC_2nd_Middle, WRF_2nd_Middle, ORF_WordsCorrect_2nd_Middle, ORF_Errors_2nd_Middle, ORF_Accuracy_2nd_Middle, MAZE_Correct_2nd_Middle, MAZE_Incorrect_2nd_Middle, MAZE_Adjusted_2nd_Middle, Composite_2nd_Middle])

NWF_CLS_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'NWF-CLS' AS Subtest
,'End' AS Administration
,Form_NWF_2nd_End AS Test_Form
,Date_NWF_2nd_End AS Test_Date
,Remote_NWF_2nd_End AS Test_Remote
,"NWF-CLS_2nd_End" AS Test_Score
,"Benchmark_Status_NWF-CLS_2nd_End" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_2nd_End" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_2nd_End" AS School_Percentile
,"District_Percentile_NWF-CLS_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

NWF_WRC_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'NWF-WRC' AS Subtest
,'End' AS Administration
,Form_NWF_2nd_End AS Test_Form
,Date_NWF_2nd_End AS Test_Date
,Remote_NWF_2nd_End AS Test_Remote
,"NWF-WRC_2nd_End" AS Test_Score
,"Benchmark_Status_NWF-WRC_2nd_End" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_2nd_End" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_2nd_End" AS School_Percentile
,"District_Percentile_NWF-WRC_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

WRF_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'WRF' AS Subtest
,'End' AS Administration
,Form_WRF_2nd_End AS Test_Form
,Date_WRF_2nd_End AS Test_Date
,Remote_WRF_2nd_End AS Test_Remote
,WRF_2nd_End AS Test_Score
,Benchmark_Status_WRF_2nd_End AS Benchmark_Status
,National_DDS_Percentile_WRF_2nd_End AS National_DDS_Percentile
,School_Percentile_WRF_2nd_End AS School_Percentile
,District_Percentile_WRF_2nd_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_WordsCorrect_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_2nd_End AS Test_Form
,Date_ORF_2nd_End AS Test_Date
,Remote_ORF_2nd_End AS Test_Remote
,"ORF-WordsCorrect_2nd_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_2nd_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_2nd_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_2nd_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_Errors_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_2nd_End AS Test_Form
,Date_ORF_2nd_End AS Test_Date
,Remote_ORF_2nd_End AS Test_Remote
,"ORF-Errors_2nd_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_2nd_End" AS School_Percentile
,"District_Percentile_ORF-Errors_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

ORF_Accuracy_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_2nd_End AS Test_Form
,Date_ORF_2nd_End AS Test_Date
,Remote_ORF_2nd_End AS Test_Remote
,"ORF-Accuracy_2nd_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_2nd_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_2nd_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_2nd_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Correct_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Correct' AS Subtest
,'End' AS Administration
,Form_Maze_2nd_End AS Test_Form
,Date_Maze_2nd_End AS Test_Date
,Remote_Maze_2nd_End AS Test_Remote
,"Maze-Correct_2nd_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_2nd_End" AS School_Percentile
,"District_Percentile_Maze-Correct_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Incorrect_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Incorrect' AS Subtest
,'End' AS Administration
,Form_Maze_2nd_End AS Test_Form
,Date_Maze_2nd_End AS Test_Date
,Remote_Maze_2nd_End AS Test_Remote
,"Maze-Incorrect_2nd_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_2nd_End" AS School_Percentile
,"District_Percentile_Maze-Incorrect_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

MAZE_Adjusted_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'MAZE-Adjusted' AS Subtest
,'End' AS Administration
,Form_Maze_2nd_End AS Test_Form
,Date_Maze_2nd_End AS Test_Date
,Remote_Maze_2nd_End AS Test_Remote
,"Maze-Adjusted_2nd_End" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_2nd_End" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_2nd_End" AS School_Percentile
,"District_Percentile_Maze-Adjusted_2nd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

Composite_2nd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_2nd AS Year
,School_2nd AS School
,Class_2nd AS Class
,Secondary_Class_2nd AS Secondary_Class
,Teacher_2nd AS Teacher
,'2nd' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_2nd_End AS Test_Date
,Null AS Test_Remote
,Composite_2nd_End AS Test_Score
,Benchmark_Status_Composite_2nd_End AS Benchmark_Status
,National_DDS_Percentile_Composite_2nd_End AS National_DDS_Percentile
,School_Percentile_Composite_2nd_End AS School_Percentile
,District_Percentile_Composite_2nd_End AS District_Percentile
,Growth_Goal_Composite_2nd_End AS Growth_Goal
,Growth_Goal_Type_Composite_2nd_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_2nd_End AS Growth_Goal_Met
,Growth_Percentile_Composite_2nd_End AS Growth_Percentile
,Months_of_Growth_Composite_2nd_End AS Months_of_Growth
FROM input
WHERE Year_2nd IS NOT NULL""")

End_Scores_2nd = pd.concat([NWF_CLS_2nd_End, NWF_WRC_2nd_End, WRF_2nd_End, ORF_WordsCorrect_2nd_End, ORF_Errors_2nd_End, ORF_Accuracy_2nd_End, MAZE_Correct_2nd_End, MAZE_Incorrect_2nd_End, MAZE_Adjusted_2nd_End, Composite_2nd_End])

Scores_2nd = pd.concat([Beginning_Scores_2nd, Middle_Scores_2nd, End_Scores_2nd])

print ("Formatting 3rd Grade Scores...")

NWF_CLS_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'NWF-CLS' AS Subtest
,'Beginning' AS Administration
,Form_NWF_3rd_Beginning AS Test_Form
,Date_NWF_3rd_Beginning AS Test_Date
,Remote_NWF_3rd_Beginning AS Test_Remote
,"NWF-CLS_3rd_Beginning" AS Test_Score
,"Benchmark_Status_NWF-CLS_3rd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_3rd_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_3rd_Beginning" AS School_Percentile
,"District_Percentile_NWF-CLS_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

NWF_WRC_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'NWF-WRC' AS Subtest
,'Beginning' AS Administration
,Form_NWF_3rd_Beginning AS Test_Form
,Date_NWF_3rd_Beginning AS Test_Date
,Remote_NWF_3rd_Beginning AS Test_Remote
,"NWF-WRC_3rd_Beginning" AS Test_Score
,"Benchmark_Status_NWF-WRC_3rd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_3rd_Beginning" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_3rd_Beginning" AS School_Percentile
,"District_Percentile_NWF-WRC_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

WRF_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'WRF' AS Subtest
,'Beginning' AS Administration
,Form_WRF_3rd_Beginning AS Test_Form
,Date_WRF_3rd_Beginning AS Test_Date
,Remote_WRF_3rd_Beginning AS Test_Remote
,WRF_3rd_Beginning AS Test_Score
,Benchmark_Status_WRF_3rd_Beginning AS Benchmark_Status
,National_DDS_Percentile_WRF_3rd_Beginning AS National_DDS_Percentile
,School_Percentile_WRF_3rd_Beginning AS School_Percentile
,District_Percentile_WRF_3rd_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_WordsCorrect_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_3rd_Beginning AS Test_Form
,Date_ORF_3rd_Beginning AS Test_Date
,Remote_ORF_3rd_Beginning AS Test_Remote
,"ORF-WordsCorrect_3rd_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_3rd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_3rd_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_3rd_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_Errors_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_3rd_Beginning AS Test_Form
,Date_ORF_3rd_Beginning AS Test_Date
,Remote_ORF_3rd_Beginning AS Test_Remote
,"ORF-Errors_3rd_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_3rd_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_Accuracy_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_3rd_Beginning AS Test_Form
,Date_ORF_3rd_Beginning AS Test_Date
,Remote_ORF_3rd_Beginning AS Test_Remote
,"ORF-Accuracy_3rd_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_3rd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_3rd_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_3rd_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Correct_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Correct' AS Subtest
,'Beginning' AS Administration
,Form_Maze_3rd_Beginning AS Test_Form
,Date_Maze_3rd_Beginning AS Test_Date
,Remote_Maze_3rd_Beginning AS Test_Remote
,"Maze-Correct_3rd_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_3rd_Beginning" AS School_Percentile
,"District_Percentile_Maze-Correct_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Incorrect_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Beginning' AS Administration
,Form_Maze_3rd_Beginning AS Test_Form
,Date_Maze_3rd_Beginning AS Test_Date
,Remote_Maze_3rd_Beginning AS Test_Remote
,"Maze-Incorrect_3rd_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_3rd_Beginning" AS School_Percentile
,"District_Percentile_Maze-Incorrect_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Adjusted_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Beginning' AS Administration
,Form_Maze_3rd_Beginning AS Test_Form
,Date_Maze_3rd_Beginning AS Test_Date
,Remote_Maze_3rd_Beginning AS Test_Remote
,"Maze-Adjusted_3rd_Beginning" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_3rd_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_3rd_Beginning" AS School_Percentile
,"District_Percentile_Maze-Adjusted_3rd_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

Composite_3rd_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_3rd_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_3rd_Beginning AS Test_Score
,Benchmark_Status_Composite_3rd_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_3rd_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_3rd_Beginning AS School_Percentile
,District_Percentile_Composite_3rd_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

Beginning_Scores_3rd = pd.concat([NWF_CLS_3rd_Beginning, NWF_WRC_3rd_Beginning, WRF_3rd_Beginning, ORF_WordsCorrect_3rd_Beginning, ORF_Errors_3rd_Beginning, ORF_Accuracy_3rd_Beginning, MAZE_Correct_3rd_Beginning, MAZE_Incorrect_3rd_Beginning, MAZE_Adjusted_3rd_Beginning, Composite_3rd_Beginning])

NWF_CLS_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'NWF-CLS' AS Subtest
,'Middle' AS Administration
,Form_NWF_3rd_Middle AS Test_Form
,Date_NWF_3rd_Middle AS Test_Date
,Remote_NWF_3rd_Middle AS Test_Remote
,"NWF-CLS_3rd_Middle" AS Test_Score
,"Benchmark_Status_NWF-CLS_3rd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_3rd_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_3rd_Middle" AS School_Percentile
,"District_Percentile_NWF-CLS_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

NWF_WRC_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'NWF-WRC' AS Subtest
,'Middle' AS Administration
,Form_NWF_3rd_Middle AS Test_Form
,Date_NWF_3rd_Middle AS Test_Date
,Remote_NWF_3rd_Middle AS Test_Remote
,"NWF-WRC_3rd_Middle" AS Test_Score
,"Benchmark_Status_NWF-WRC_3rd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_3rd_Middle" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_3rd_Middle" AS School_Percentile
,"District_Percentile_NWF-WRC_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

WRF_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'WRF' AS Subtest
,'Middle' AS Administration
,Form_WRF_3rd_Middle AS Test_Form
,Date_WRF_3rd_Middle AS Test_Date
,Remote_WRF_3rd_Middle AS Test_Remote
,WRF_3rd_Middle AS Test_Score
,Benchmark_Status_WRF_3rd_Middle AS Benchmark_Status
,National_DDS_Percentile_WRF_3rd_Middle AS National_DDS_Percentile
,School_Percentile_WRF_3rd_Middle AS School_Percentile
,District_Percentile_WRF_3rd_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_WordsCorrect_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_3rd_Middle AS Test_Form
,Date_ORF_3rd_Middle AS Test_Date
,Remote_ORF_3rd_Middle AS Test_Remote
,"ORF-WordsCorrect_3rd_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_3rd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_3rd_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_3rd_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_Errors_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_3rd_Middle AS Test_Form
,Date_ORF_3rd_Middle AS Test_Date
,Remote_ORF_3rd_Middle AS Test_Remote
,"ORF-Errors_3rd_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_3rd_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_Accuracy_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_3rd_Middle AS Test_Form
,Date_ORF_3rd_Middle AS Test_Date
,Remote_ORF_3rd_Middle AS Test_Remote
,"ORF-Accuracy_3rd_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_3rd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_3rd_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_3rd_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Correct_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Correct' AS Subtest
,'Middle' AS Administration
,Form_Maze_3rd_Middle AS Test_Form
,Date_Maze_3rd_Middle AS Test_Date
,Remote_Maze_3rd_Middle AS Test_Remote
,"Maze-Correct_3rd_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_3rd_Middle" AS School_Percentile
,"District_Percentile_Maze-Correct_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Incorrect_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Middle' AS Administration
,Form_Maze_3rd_Middle AS Test_Form
,Date_Maze_3rd_Middle AS Test_Date
,Remote_Maze_3rd_Middle AS Test_Remote
,"Maze-Incorrect_3rd_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_3rd_Middle" AS School_Percentile
,"District_Percentile_Maze-Incorrect_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Adjusted_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Middle' AS Administration
,Form_Maze_3rd_Middle AS Test_Form
,Date_Maze_3rd_Middle AS Test_Date
,Remote_Maze_3rd_Middle AS Test_Remote
,"Maze-Adjusted_3rd_Middle" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_3rd_Middle" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_3rd_Middle" AS School_Percentile
,"District_Percentile_Maze-Adjusted_3rd_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

Composite_3rd_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_3rd_Middle AS Test_Date
,Null AS Test_Remote
,Composite_3rd_Middle AS Test_Score
,Benchmark_Status_Composite_3rd_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_3rd_Middle AS National_DDS_Percentile
,School_Percentile_Composite_3rd_Middle AS School_Percentile
,District_Percentile_Composite_3rd_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

Middle_Scores_3rd = pd.concat([NWF_CLS_3rd_Middle, NWF_WRC_3rd_Middle, WRF_3rd_Middle, ORF_WordsCorrect_3rd_Middle, ORF_Errors_3rd_Middle, ORF_Accuracy_3rd_Middle, MAZE_Correct_3rd_Middle, MAZE_Incorrect_3rd_Middle, MAZE_Adjusted_3rd_Middle, Composite_3rd_Middle])

NWF_CLS_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'NWF-CLS' AS Subtest
,'End' AS Administration
,Form_NWF_3rd_End AS Test_Form
,Date_NWF_3rd_End AS Test_Date
,Remote_NWF_3rd_End AS Test_Remote
,"NWF-CLS_3rd_End" AS Test_Score
,"Benchmark_Status_NWF-CLS_3rd_End" AS Benchmark_Status
,"National_DDS_Percentile_NWF-CLS_3rd_End" AS National_DDS_Percentile
,"School_Percentile_NWF-CLS_3rd_End" AS School_Percentile
,"District_Percentile_NWF-CLS_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

NWF_WRC_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'NWF-WRC' AS Subtest
,'End' AS Administration
,Form_NWF_3rd_End AS Test_Form
,Date_NWF_3rd_End AS Test_Date
,Remote_NWF_3rd_End AS Test_Remote
,"NWF-WRC_3rd_End" AS Test_Score
,"Benchmark_Status_NWF-WRC_3rd_End" AS Benchmark_Status
,"National_DDS_Percentile_NWF-WRC_3rd_End" AS National_DDS_Percentile
,"School_Percentile_NWF-WRC_3rd_End" AS School_Percentile
,"District_Percentile_NWF-WRC_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

WRF_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'WRF' AS Subtest
,'End' AS Administration
,Form_WRF_3rd_End AS Test_Form
,Date_WRF_3rd_End AS Test_Date
,Remote_WRF_3rd_End AS Test_Remote
,WRF_3rd_End AS Test_Score
,Benchmark_Status_WRF_3rd_End AS Benchmark_Status
,National_DDS_Percentile_WRF_3rd_End AS National_DDS_Percentile
,School_Percentile_WRF_3rd_End AS School_Percentile
,District_Percentile_WRF_3rd_End AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_WordsCorrect_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_3rd_End AS Test_Form
,Date_ORF_3rd_End AS Test_Date
,Remote_ORF_3rd_End AS Test_Remote
,"ORF-WordsCorrect_3rd_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_3rd_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_3rd_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_3rd_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_Errors_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_3rd_End AS Test_Form
,Date_ORF_3rd_End AS Test_Date
,Remote_ORF_3rd_End AS Test_Remote
,"ORF-Errors_3rd_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_3rd_End" AS School_Percentile
,"District_Percentile_ORF-Errors_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

ORF_Accuracy_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_3rd_End AS Test_Form
,Date_ORF_3rd_End AS Test_Date
,Remote_ORF_3rd_End AS Test_Remote
,"ORF-Accuracy_3rd_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_3rd_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_3rd_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_3rd_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Correct_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Correct' AS Subtest
,'End' AS Administration
,Form_Maze_3rd_End AS Test_Form
,Date_Maze_3rd_End AS Test_Date
,Remote_Maze_3rd_End AS Test_Remote
,"Maze-Correct_3rd_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_3rd_End" AS School_Percentile
,"District_Percentile_Maze-Correct_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Incorrect_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Incorrect' AS Subtest
,'End' AS Administration
,Form_Maze_3rd_End AS Test_Form
,Date_Maze_3rd_End AS Test_Date
,Remote_Maze_3rd_End AS Test_Remote
,"Maze-Incorrect_3rd_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_3rd_End" AS School_Percentile
,"District_Percentile_Maze-Incorrect_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

MAZE_Adjusted_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'MAZE-Adjusted' AS Subtest
,'End' AS Administration
,Form_Maze_3rd_End AS Test_Form
,Date_Maze_3rd_End AS Test_Date
,Remote_Maze_3rd_End AS Test_Remote
,"Maze-Adjusted_3rd_End" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_3rd_End" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_3rd_End" AS School_Percentile
,"District_Percentile_Maze-Adjusted_3rd_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

Composite_3rd_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_3rd AS Year
,School_3rd AS School
,Class_3rd AS Class
,Secondary_Class_3rd AS Secondary_Class
,Teacher_3rd AS Teacher
,'3rd' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_3rd_End AS Test_Date
,Null AS Test_Remote
,Composite_3rd_End AS Test_Score
,Benchmark_Status_Composite_3rd_End AS Benchmark_Status
,National_DDS_Percentile_Composite_3rd_End AS National_DDS_Percentile
,School_Percentile_Composite_3rd_End AS School_Percentile
,District_Percentile_Composite_3rd_End AS District_Percentile
,Growth_Goal_Composite_3rd_End AS Growth_Goal
,Growth_Goal_Type_Composite_3rd_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_3rd_End AS Growth_Goal_Met
,Growth_Percentile_Composite_3rd_End AS Growth_Percentile
,Months_of_Growth_Composite_3rd_End AS Months_of_Growth
FROM input
WHERE Year_3rd IS NOT NULL""")

End_Scores_3rd = pd.concat([NWF_CLS_3rd_End, NWF_WRC_3rd_End, WRF_3rd_End, ORF_WordsCorrect_3rd_End, ORF_Errors_3rd_End, ORF_Accuracy_3rd_End, MAZE_Correct_3rd_End, MAZE_Incorrect_3rd_End, MAZE_Adjusted_3rd_End, Composite_3rd_End])

Scores_3rd = pd.concat([Beginning_Scores_3rd, Middle_Scores_3rd, End_Scores_3rd])

print ("Formatting 4th Grade Scores...")

ORF_WordsCorrect_4th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_4th_Beginning AS Test_Form
,Date_ORF_4th_Beginning AS Test_Date
,Remote_ORF_4th_Beginning AS Test_Remote
,"ORF-WordsCorrect_4th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_4th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_4th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_4th_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_4th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

ORF_Errors_4th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_4th_Beginning AS Test_Form
,Date_ORF_4th_Beginning AS Test_Date
,Remote_ORF_4th_Beginning AS Test_Remote
,"ORF-Errors_4th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_4th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_4th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

ORF_Accuracy_4th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_4th_Beginning AS Test_Form
,Date_ORF_4th_Beginning AS Test_Date
,Remote_ORF_4th_Beginning AS Test_Remote
,"ORF-Accuracy_4th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_4th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_4th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_4th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_4th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Correct_4th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Correct' AS Subtest
,'Beginning' AS Administration
,Form_Maze_4th_Beginning AS Test_Form
,Date_Maze_4th_Beginning AS Test_Date
,Remote_Maze_4th_Beginning AS Test_Remote
,"Maze-Correct_4th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_4th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Correct_4th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Incorrect_4th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Beginning' AS Administration
,Form_Maze_4th_Beginning AS Test_Form
,Date_Maze_4th_Beginning AS Test_Date
,Remote_Maze_4th_Beginning AS Test_Remote
,"Maze-Incorrect_4th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_4th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Incorrect_4th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Adjusted_4th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Beginning' AS Administration
,Form_Maze_4th_Beginning AS Test_Form
,Date_Maze_4th_Beginning AS Test_Date
,Remote_Maze_4th_Beginning AS Test_Remote
,"Maze-Adjusted_4th_Beginning" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_4th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_4th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Adjusted_4th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

Composite_4th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_4th_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_4th_Beginning AS Test_Score
,Benchmark_Status_Composite_4th_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_4th_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_4th_Beginning AS School_Percentile
,District_Percentile_Composite_4th_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

Beginning_Scores_4th = pd.concat([ORF_WordsCorrect_4th_Beginning, ORF_Errors_4th_Beginning, ORF_Accuracy_4th_Beginning, MAZE_Correct_4th_Beginning, MAZE_Incorrect_4th_Beginning, MAZE_Adjusted_4th_Beginning, Composite_4th_Beginning])

ORF_WordsCorrect_4th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_4th_Middle AS Test_Form
,Date_ORF_4th_Middle AS Test_Date
,Remote_ORF_4th_Middle AS Test_Remote
,"ORF-WordsCorrect_4th_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_4th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_4th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_4th_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_4th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

ORF_Errors_4th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_4th_Middle AS Test_Form
,Date_ORF_4th_Middle AS Test_Date
,Remote_ORF_4th_Middle AS Test_Remote
,"ORF-Errors_4th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_4th_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_4th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

ORF_Accuracy_4th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_4th_Middle AS Test_Form
,Date_ORF_4th_Middle AS Test_Date
,Remote_ORF_4th_Middle AS Test_Remote
,"ORF-Accuracy_4th_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_4th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_4th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_4th_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_4th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Correct_4th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Correct' AS Subtest
,'Middle' AS Administration
,Form_Maze_4th_Middle AS Test_Form
,Date_Maze_4th_Middle AS Test_Date
,Remote_Maze_4th_Middle AS Test_Remote
,"Maze-Correct_4th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_4th_Middle" AS School_Percentile
,"District_Percentile_Maze-Correct_4th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Incorrect_4th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Middle' AS Administration
,Form_Maze_4th_Middle AS Test_Form
,Date_Maze_4th_Middle AS Test_Date
,Remote_Maze_4th_Middle AS Test_Remote
,"Maze-Incorrect_4th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_4th_Middle" AS School_Percentile
,"District_Percentile_Maze-Incorrect_4th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Adjusted_4th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Middle' AS Administration
,Form_Maze_4th_Middle AS Test_Form
,Date_Maze_4th_Middle AS Test_Date
,Remote_Maze_4th_Middle AS Test_Remote
,"Maze-Adjusted_4th_Middle" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_4th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_4th_Middle" AS School_Percentile
,"District_Percentile_Maze-Adjusted_4th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

Composite_4th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_4th_Middle AS Test_Date
,Null AS Test_Remote
,Composite_4th_Middle AS Test_Score
,Benchmark_Status_Composite_4th_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_4th_Middle AS National_DDS_Percentile
,School_Percentile_Composite_4th_Middle AS School_Percentile
,District_Percentile_Composite_4th_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

Middle_Scores_4th = pd.concat([ORF_WordsCorrect_4th_Middle, ORF_Errors_4th_Middle, ORF_Accuracy_4th_Middle, MAZE_Correct_4th_Middle, MAZE_Incorrect_4th_Middle, MAZE_Adjusted_4th_Middle, Composite_4th_Middle])

ORF_WordsCorrect_4th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_4th_End AS Test_Form
,Date_ORF_4th_End AS Test_Date
,Remote_ORF_4th_End AS Test_Remote
,"ORF-WordsCorrect_4th_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_4th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_4th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_4th_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_4th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

ORF_Errors_4th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_4th_End AS Test_Form
,Date_ORF_4th_End AS Test_Date
,Remote_ORF_4th_End AS Test_Remote
,"ORF-Errors_4th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_4th_End" AS School_Percentile
,"District_Percentile_ORF-Errors_4th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

ORF_Accuracy_4th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_4th_End AS Test_Form
,Date_ORF_4th_End AS Test_Date
,Remote_ORF_4th_End AS Test_Remote
,"ORF-Accuracy_4th_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_4th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_4th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_4th_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_4th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Correct_4th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Correct' AS Subtest
,'End' AS Administration
,Form_Maze_4th_End AS Test_Form
,Date_Maze_4th_End AS Test_Date
,Remote_Maze_4th_End AS Test_Remote
,"Maze-Correct_4th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_4th_End" AS School_Percentile
,"District_Percentile_Maze-Correct_4th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Incorrect_4th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'End' AS Administration
,Form_Maze_4th_End AS Test_Form
,Date_Maze_4th_End AS Test_Date
,Remote_Maze_4th_End AS Test_Remote
,"Maze-Incorrect_4th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_4th_End" AS School_Percentile
,"District_Percentile_Maze-Incorrect_4th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

MAZE_Adjusted_4th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'End' AS Administration
,Form_Maze_4th_End AS Test_Form
,Date_Maze_4th_End AS Test_Date
,Remote_Maze_4th_End AS Test_Remote
,"Maze-Adjusted_4th_End" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_4th_End" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_4th_End" AS School_Percentile
,"District_Percentile_Maze-Adjusted_4th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

Composite_4th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_4th AS Year
,School_4th AS School
,Class_4th AS Class
,Secondary_Class_4th AS Secondary_Class
,Teacher_4th AS Teacher
,'4th' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_4th_End AS Test_Date
,Null AS Test_Remote
,Composite_4th_End AS Test_Score
,Benchmark_Status_Composite_4th_End AS Benchmark_Status
,National_DDS_Percentile_Composite_4th_End AS National_DDS_Percentile
,School_Percentile_Composite_4th_End AS School_Percentile
,District_Percentile_Composite_4th_End AS District_Percentile
,Growth_Goal_Composite_4th_End AS Growth_Goal
,Growth_Goal_Type_Composite_4th_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_4th_End AS Growth_Goal_Met
,Growth_Percentile_Composite_4th_End AS Growth_Percentile
,Months_of_Growth_Composite_4th_End AS Months_of_Growth
FROM input
WHERE Year_4th IS NOT NULL""")

End_Scores_4th = pd.concat([ORF_WordsCorrect_4th_End, ORF_Errors_4th_End, ORF_Accuracy_4th_End, MAZE_Correct_4th_End, MAZE_Incorrect_4th_End, MAZE_Adjusted_4th_End, Composite_4th_End])

Scores_4th = pd.concat([Beginning_Scores_4th, Middle_Scores_4th, End_Scores_4th])

print ("Formatting 5th Grade Scores...")

ORF_WordsCorrect_5th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_5th_Beginning AS Test_Form
,Date_ORF_5th_Beginning AS Test_Date
,Remote_ORF_5th_Beginning AS Test_Remote
,"ORF-WordsCorrect_5th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_5th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_5th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_5th_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_5th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

ORF_Errors_5th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_5th_Beginning AS Test_Form
,Date_ORF_5th_Beginning AS Test_Date
,Remote_ORF_5th_Beginning AS Test_Remote
,"ORF-Errors_5th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_5th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_5th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

ORF_Accuracy_5th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_5th_Beginning AS Test_Form
,Date_ORF_5th_Beginning AS Test_Date
,Remote_ORF_5th_Beginning AS Test_Remote
,"ORF-Accuracy_5th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_5th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_5th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_5th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_5th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Correct_5th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Correct' AS Subtest
,'Beginning' AS Administration
,Form_Maze_5th_Beginning AS Test_Form
,Date_Maze_5th_Beginning AS Test_Date
,Remote_Maze_5th_Beginning AS Test_Remote
,"Maze-Correct_5th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_5th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Correct_5th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Incorrect_5th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Beginning' AS Administration
,Form_Maze_5th_Beginning AS Test_Form
,Date_Maze_5th_Beginning AS Test_Date
,Remote_Maze_5th_Beginning AS Test_Remote
,"Maze-Incorrect_5th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_5th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Incorrect_5th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Adjusted_5th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Beginning' AS Administration
,Form_Maze_5th_Beginning AS Test_Form
,Date_Maze_5th_Beginning AS Test_Date
,Remote_Maze_5th_Beginning AS Test_Remote
,"Maze-Adjusted_5th_Beginning" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_5th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_5th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Adjusted_5th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

Composite_5th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_5th_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_5th_Beginning AS Test_Score
,Benchmark_Status_Composite_5th_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_5th_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_5th_Beginning AS School_Percentile
,District_Percentile_Composite_5th_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

Beginning_Scores_5th = pd.concat([ORF_WordsCorrect_5th_Beginning, ORF_Errors_5th_Beginning, ORF_Accuracy_5th_Beginning, MAZE_Correct_5th_Beginning, MAZE_Incorrect_5th_Beginning, MAZE_Adjusted_5th_Beginning, Composite_5th_Beginning])

ORF_WordsCorrect_5th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_5th_Middle AS Test_Form
,Date_ORF_5th_Middle AS Test_Date
,Remote_ORF_5th_Middle AS Test_Remote
,"ORF-WordsCorrect_5th_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_5th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_5th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_5th_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_5th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

ORF_Errors_5th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_5th_Middle AS Test_Form
,Date_ORF_5th_Middle AS Test_Date
,Remote_ORF_5th_Middle AS Test_Remote
,"ORF-Errors_5th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_5th_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_5th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

ORF_Accuracy_5th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_5th_Middle AS Test_Form
,Date_ORF_5th_Middle AS Test_Date
,Remote_ORF_5th_Middle AS Test_Remote
,"ORF-Accuracy_5th_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_5th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_5th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_5th_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_5th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Correct_5th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Correct' AS Subtest
,'Middle' AS Administration
,Form_Maze_5th_Middle AS Test_Form
,Date_Maze_5th_Middle AS Test_Date
,Remote_Maze_5th_Middle AS Test_Remote
,"Maze-Correct_5th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_5th_Middle" AS School_Percentile
,"District_Percentile_Maze-Correct_5th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Incorrect_5th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Middle' AS Administration
,Form_Maze_5th_Middle AS Test_Form
,Date_Maze_5th_Middle AS Test_Date
,Remote_Maze_5th_Middle AS Test_Remote
,"Maze-Incorrect_5th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_5th_Middle" AS School_Percentile
,"District_Percentile_Maze-Incorrect_5th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Adjusted_5th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Middle' AS Administration
,Form_Maze_5th_Middle AS Test_Form
,Date_Maze_5th_Middle AS Test_Date
,Remote_Maze_5th_Middle AS Test_Remote
,"Maze-Adjusted_5th_Middle" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_5th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_5th_Middle" AS School_Percentile
,"District_Percentile_Maze-Adjusted_5th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

Composite_5th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_5th_Middle AS Test_Date
,Null AS Test_Remote
,Composite_5th_Middle AS Test_Score
,Benchmark_Status_Composite_5th_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_5th_Middle AS National_DDS_Percentile
,School_Percentile_Composite_5th_Middle AS School_Percentile
,District_Percentile_Composite_5th_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

Middle_Scores_5th = pd.concat([ORF_WordsCorrect_5th_Middle, ORF_Errors_5th_Middle, ORF_Accuracy_5th_Middle, MAZE_Correct_5th_Middle, MAZE_Incorrect_5th_Middle, MAZE_Adjusted_5th_Middle, Composite_5th_Middle])

ORF_WordsCorrect_5th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_5th_End AS Test_Form
,Date_ORF_5th_End AS Test_Date
,Remote_ORF_5th_End AS Test_Remote
,"ORF-WordsCorrect_5th_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_5th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_5th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_5th_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_5th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

ORF_Errors_5th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_5th_End AS Test_Form
,Date_ORF_5th_End AS Test_Date
,Remote_ORF_5th_End AS Test_Remote
,"ORF-Errors_5th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_5th_End" AS School_Percentile
,"District_Percentile_ORF-Errors_5th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

ORF_Accuracy_5th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_5th_End AS Test_Form
,Date_ORF_5th_End AS Test_Date
,Remote_ORF_5th_End AS Test_Remote
,"ORF-Accuracy_5th_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_5th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_5th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_5th_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_5th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Correct_5th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Correct' AS Subtest
,'End' AS Administration
,Form_Maze_5th_End AS Test_Form
,Date_Maze_5th_End AS Test_Date
,Remote_Maze_5th_End AS Test_Remote
,"Maze-Correct_5th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_5th_End" AS School_Percentile
,"District_Percentile_Maze-Correct_5th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Incorrect_5th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'End' AS Administration
,Form_Maze_5th_End AS Test_Form
,Date_Maze_5th_End AS Test_Date
,Remote_Maze_5th_End AS Test_Remote
,"Maze-Incorrect_5th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_5th_End" AS School_Percentile
,"District_Percentile_Maze-Incorrect_5th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

MAZE_Adjusted_5th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'End' AS Administration
,Form_Maze_5th_End AS Test_Form
,Date_Maze_5th_End AS Test_Date
,Remote_Maze_5th_End AS Test_Remote
,"Maze-Adjusted_5th_End" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_5th_End" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_5th_End" AS School_Percentile
,"District_Percentile_Maze-Adjusted_5th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

Composite_5th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_5th AS Year
,School_5th AS School
,Class_5th AS Class
,Secondary_Class_5th AS Secondary_Class
,Teacher_5th AS Teacher
,'5th' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_5th_End AS Test_Date
,Null AS Test_Remote
,Composite_5th_End AS Test_Score
,Benchmark_Status_Composite_5th_End AS Benchmark_Status
,National_DDS_Percentile_Composite_5th_End AS National_DDS_Percentile
,School_Percentile_Composite_5th_End AS School_Percentile
,District_Percentile_Composite_5th_End AS District_Percentile
,Growth_Goal_Composite_5th_End AS Growth_Goal
,Growth_Goal_Type_Composite_5th_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_5th_End AS Growth_Goal_Met
,Growth_Percentile_Composite_5th_End AS Growth_Percentile
,Months_of_Growth_Composite_5th_End AS Months_of_Growth
FROM input
WHERE Year_5th IS NOT NULL""")

End_Scores_5th = pd.concat([ORF_WordsCorrect_5th_End, ORF_Errors_5th_End, ORF_Accuracy_5th_End, MAZE_Correct_5th_End, MAZE_Incorrect_5th_End, MAZE_Adjusted_5th_End, Composite_5th_End])

Scores_5th = pd.concat([Beginning_Scores_5th, Middle_Scores_5th, End_Scores_5th])

print ("Formatting 6th Grade Scores...")

ORF_WordsCorrect_6th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_6th_Beginning AS Test_Form
,Date_ORF_6th_Beginning AS Test_Date
,Remote_ORF_6th_Beginning AS Test_Remote
,"ORF-WordsCorrect_6th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_6th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_6th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_6th_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_6th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

ORF_Errors_6th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_6th_Beginning AS Test_Form
,Date_ORF_6th_Beginning AS Test_Date
,Remote_ORF_6th_Beginning AS Test_Remote
,"ORF-Errors_6th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_6th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_6th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

ORF_Accuracy_6th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_6th_Beginning AS Test_Form
,Date_ORF_6th_Beginning AS Test_Date
,Remote_ORF_6th_Beginning AS Test_Remote
,"ORF-Accuracy_6th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_6th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_6th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_6th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_6th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Correct_6th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Correct' AS Subtest
,'Beginning' AS Administration
,Form_Maze_6th_Beginning AS Test_Form
,Date_Maze_6th_Beginning AS Test_Date
,Remote_Maze_6th_Beginning AS Test_Remote
,"Maze-Correct_6th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_6th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Correct_6th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Incorrect_6th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Beginning' AS Administration
,Form_Maze_6th_Beginning AS Test_Form
,Date_Maze_6th_Beginning AS Test_Date
,Remote_Maze_6th_Beginning AS Test_Remote
,"Maze-Incorrect_6th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_6th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Incorrect_6th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Adjusted_6th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Beginning' AS Administration
,Form_Maze_6th_Beginning AS Test_Form
,Date_Maze_6th_Beginning AS Test_Date
,Remote_Maze_6th_Beginning AS Test_Remote
,"Maze-Adjusted_6th_Beginning" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_6th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_6th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Adjusted_6th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

Composite_6th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_6th_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_6th_Beginning AS Test_Score
,Benchmark_Status_Composite_6th_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_6th_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_6th_Beginning AS School_Percentile
,District_Percentile_Composite_6th_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

Beginning_Scores_6th = pd.concat([ORF_WordsCorrect_6th_Beginning, ORF_Errors_6th_Beginning, ORF_Accuracy_6th_Beginning, MAZE_Correct_6th_Beginning, MAZE_Incorrect_6th_Beginning, MAZE_Adjusted_6th_Beginning, Composite_6th_Beginning])

ORF_WordsCorrect_6th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_6th_Middle AS Test_Form
,Date_ORF_6th_Middle AS Test_Date
,Remote_ORF_6th_Middle AS Test_Remote
,"ORF-WordsCorrect_6th_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_6th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_6th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_6th_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_6th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

ORF_Errors_6th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_6th_Middle AS Test_Form
,Date_ORF_6th_Middle AS Test_Date
,Remote_ORF_6th_Middle AS Test_Remote
,"ORF-Errors_6th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_6th_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_6th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

ORF_Accuracy_6th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_6th_Middle AS Test_Form
,Date_ORF_6th_Middle AS Test_Date
,Remote_ORF_6th_Middle AS Test_Remote
,"ORF-Accuracy_6th_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_6th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_6th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_6th_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_6th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Correct_6th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Correct' AS Subtest
,'Middle' AS Administration
,Form_Maze_6th_Middle AS Test_Form
,Date_Maze_6th_Middle AS Test_Date
,Remote_Maze_6th_Middle AS Test_Remote
,"Maze-Correct_6th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_6th_Middle" AS School_Percentile
,"District_Percentile_Maze-Correct_6th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Incorrect_6th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Middle' AS Administration
,Form_Maze_6th_Middle AS Test_Form
,Date_Maze_6th_Middle AS Test_Date
,Remote_Maze_6th_Middle AS Test_Remote
,"Maze-Incorrect_6th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_6th_Middle" AS School_Percentile
,"District_Percentile_Maze-Incorrect_6th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Adjusted_6th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Middle' AS Administration
,Form_Maze_6th_Middle AS Test_Form
,Date_Maze_6th_Middle AS Test_Date
,Remote_Maze_6th_Middle AS Test_Remote
,"Maze-Adjusted_6th_Middle" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_6th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_6th_Middle" AS School_Percentile
,"District_Percentile_Maze-Adjusted_6th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

Composite_6th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_6th_Middle AS Test_Date
,Null AS Test_Remote
,Composite_6th_Middle AS Test_Score
,Benchmark_Status_Composite_6th_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_6th_Middle AS National_DDS_Percentile
,School_Percentile_Composite_6th_Middle AS School_Percentile
,District_Percentile_Composite_6th_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

Middle_Scores_6th = pd.concat([ORF_WordsCorrect_6th_Middle, ORF_Errors_6th_Middle, ORF_Accuracy_6th_Middle, MAZE_Correct_6th_Middle, MAZE_Incorrect_6th_Middle, MAZE_Adjusted_6th_Middle, Composite_6th_Middle])

ORF_WordsCorrect_6th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_6th_End AS Test_Form
,Date_ORF_6th_End AS Test_Date
,Remote_ORF_6th_End AS Test_Remote
,"ORF-WordsCorrect_6th_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_6th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_6th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_6th_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_6th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

ORF_Errors_6th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_6th_End AS Test_Form
,Date_ORF_6th_End AS Test_Date
,Remote_ORF_6th_End AS Test_Remote
,"ORF-Errors_6th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_6th_End" AS School_Percentile
,"District_Percentile_ORF-Errors_6th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

ORF_Accuracy_6th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_6th_End AS Test_Form
,Date_ORF_6th_End AS Test_Date
,Remote_ORF_6th_End AS Test_Remote
,"ORF-Accuracy_6th_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_6th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_6th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_6th_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_6th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Correct_6th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Correct' AS Subtest
,'End' AS Administration
,Form_Maze_6th_End AS Test_Form
,Date_Maze_6th_End AS Test_Date
,Remote_Maze_6th_End AS Test_Remote
,"Maze-Correct_6th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_6th_End" AS School_Percentile
,"District_Percentile_Maze-Correct_6th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Incorrect_6th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'End' AS Administration
,Form_Maze_6th_End AS Test_Form
,Date_Maze_6th_End AS Test_Date
,Remote_Maze_6th_End AS Test_Remote
,"Maze-Incorrect_6th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_6th_End" AS School_Percentile
,"District_Percentile_Maze-Incorrect_6th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

MAZE_Adjusted_6th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'End' AS Administration
,Form_Maze_6th_End AS Test_Form
,Date_Maze_6th_End AS Test_Date
,Remote_Maze_6th_End AS Test_Remote
,"Maze-Adjusted_6th_End" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_6th_End" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_6th_End" AS School_Percentile
,"District_Percentile_Maze-Adjusted_6th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

Composite_6th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_6th AS Year
,School_6th AS School
,Class_6th AS Class
,Secondary_Class_6th AS Secondary_Class
,Teacher_6th AS Teacher
,'6th' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_6th_End AS Test_Date
,Null AS Test_Remote
,Composite_6th_End AS Test_Score
,Benchmark_Status_Composite_6th_End AS Benchmark_Status
,National_DDS_Percentile_Composite_6th_End AS National_DDS_Percentile
,School_Percentile_Composite_6th_End AS School_Percentile
,District_Percentile_Composite_6th_End AS District_Percentile
,Growth_Goal_Composite_6th_End AS Growth_Goal
,Growth_Goal_Type_Composite_6th_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_6th_End AS Growth_Goal_Met
,Growth_Percentile_Composite_6th_End AS Growth_Percentile
,Months_of_Growth_Composite_6th_End AS Months_of_Growth
FROM input
WHERE Year_6th IS NOT NULL""")

End_Scores_6th = pd.concat([ORF_WordsCorrect_6th_End, ORF_Errors_6th_End, ORF_Accuracy_6th_End, MAZE_Correct_6th_End, MAZE_Incorrect_6th_End, MAZE_Adjusted_6th_End, Composite_6th_End])

Scores_6th = pd.concat([Beginning_Scores_6th, Middle_Scores_6th, End_Scores_6th])

print ("Formatting 7th Grade Scores...")

ORF_WordsCorrect_7th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_7th_Beginning AS Test_Form
,Date_ORF_7th_Beginning AS Test_Date
,Remote_ORF_7th_Beginning AS Test_Remote
,"ORF-WordsCorrect_7th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_7th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_7th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_7th_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_7th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

ORF_Errors_7th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_7th_Beginning AS Test_Form
,Date_ORF_7th_Beginning AS Test_Date
,Remote_ORF_7th_Beginning AS Test_Remote
,"ORF-Errors_7th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_7th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_7th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

ORF_Accuracy_7th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_7th_Beginning AS Test_Form
,Date_ORF_7th_Beginning AS Test_Date
,Remote_ORF_7th_Beginning AS Test_Remote
,"ORF-Accuracy_7th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_7th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_7th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_7th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_7th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Correct_7th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Correct' AS Subtest
,'Beginning' AS Administration
,Form_Maze_7th_Beginning AS Test_Form
,Date_Maze_7th_Beginning AS Test_Date
,Remote_Maze_7th_Beginning AS Test_Remote
,"Maze-Correct_7th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_7th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Correct_7th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Incorrect_7th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Beginning' AS Administration
,Form_Maze_7th_Beginning AS Test_Form
,Date_Maze_7th_Beginning AS Test_Date
,Remote_Maze_7th_Beginning AS Test_Remote
,"Maze-Incorrect_7th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_7th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Incorrect_7th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Adjusted_7th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Beginning' AS Administration
,Form_Maze_7th_Beginning AS Test_Form
,Date_Maze_7th_Beginning AS Test_Date
,Remote_Maze_7th_Beginning AS Test_Remote
,"Maze-Adjusted_7th_Beginning" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_7th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_7th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Adjusted_7th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

Composite_7th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_7th_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_7th_Beginning AS Test_Score
,Benchmark_Status_Composite_7th_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_7th_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_7th_Beginning AS School_Percentile
,District_Percentile_Composite_7th_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

Beginning_Scores_7th = pd.concat([ORF_WordsCorrect_7th_Beginning, ORF_Errors_7th_Beginning, ORF_Accuracy_7th_Beginning, MAZE_Correct_7th_Beginning, MAZE_Incorrect_7th_Beginning, MAZE_Adjusted_7th_Beginning, Composite_7th_Beginning])

ORF_WordsCorrect_7th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_7th_Middle AS Test_Form
,Date_ORF_7th_Middle AS Test_Date
,Remote_ORF_7th_Middle AS Test_Remote
,"ORF-WordsCorrect_7th_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_7th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_7th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_7th_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_7th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

ORF_Errors_7th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_7th_Middle AS Test_Form
,Date_ORF_7th_Middle AS Test_Date
,Remote_ORF_7th_Middle AS Test_Remote
,"ORF-Errors_7th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_7th_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_7th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

ORF_Accuracy_7th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_7th_Middle AS Test_Form
,Date_ORF_7th_Middle AS Test_Date
,Remote_ORF_7th_Middle AS Test_Remote
,"ORF-Accuracy_7th_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_7th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_7th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_7th_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_7th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Correct_7th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Correct' AS Subtest
,'Middle' AS Administration
,Form_Maze_7th_Middle AS Test_Form
,Date_Maze_7th_Middle AS Test_Date
,Remote_Maze_7th_Middle AS Test_Remote
,"Maze-Correct_7th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_7th_Middle" AS School_Percentile
,"District_Percentile_Maze-Correct_7th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Incorrect_7th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Middle' AS Administration
,Form_Maze_7th_Middle AS Test_Form
,Date_Maze_7th_Middle AS Test_Date
,Remote_Maze_7th_Middle AS Test_Remote
,"Maze-Incorrect_7th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_7th_Middle" AS School_Percentile
,"District_Percentile_Maze-Incorrect_7th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Adjusted_7th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Middle' AS Administration
,Form_Maze_7th_Middle AS Test_Form
,Date_Maze_7th_Middle AS Test_Date
,Remote_Maze_7th_Middle AS Test_Remote
,"Maze-Adjusted_7th_Middle" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_7th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_7th_Middle" AS School_Percentile
,"District_Percentile_Maze-Adjusted_7th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

Composite_7th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_7th_Middle AS Test_Date
,Null AS Test_Remote
,Composite_7th_Middle AS Test_Score
,Benchmark_Status_Composite_7th_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_7th_Middle AS National_DDS_Percentile
,School_Percentile_Composite_7th_Middle AS School_Percentile
,District_Percentile_Composite_7th_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

Middle_Scores_7th = pd.concat([ORF_WordsCorrect_7th_Middle, ORF_Errors_7th_Middle, ORF_Accuracy_7th_Middle, MAZE_Correct_7th_Middle, MAZE_Incorrect_7th_Middle, MAZE_Adjusted_7th_Middle, Composite_7th_Middle])

ORF_WordsCorrect_7th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_7th_End AS Test_Form
,Date_ORF_7th_End AS Test_Date
,Remote_ORF_7th_End AS Test_Remote
,"ORF-WordsCorrect_7th_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_7th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_7th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_7th_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_7th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

ORF_Errors_7th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_7th_End AS Test_Form
,Date_ORF_7th_End AS Test_Date
,Remote_ORF_7th_End AS Test_Remote
,"ORF-Errors_7th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_7th_End" AS School_Percentile
,"District_Percentile_ORF-Errors_7th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

ORF_Accuracy_7th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_7th_End AS Test_Form
,Date_ORF_7th_End AS Test_Date
,Remote_ORF_7th_End AS Test_Remote
,"ORF-Accuracy_7th_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_7th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_7th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_7th_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_7th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Correct_7th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Correct' AS Subtest
,'End' AS Administration
,Form_Maze_7th_End AS Test_Form
,Date_Maze_7th_End AS Test_Date
,Remote_Maze_7th_End AS Test_Remote
,"Maze-Correct_7th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_7th_End" AS School_Percentile
,"District_Percentile_Maze-Correct_7th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Incorrect_7th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'End' AS Administration
,Form_Maze_7th_End AS Test_Form
,Date_Maze_7th_End AS Test_Date
,Remote_Maze_7th_End AS Test_Remote
,"Maze-Incorrect_7th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_7th_End" AS School_Percentile
,"District_Percentile_Maze-Incorrect_7th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

MAZE_Adjusted_7th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'End' AS Administration
,Form_Maze_7th_End AS Test_Form
,Date_Maze_7th_End AS Test_Date
,Remote_Maze_7th_End AS Test_Remote
,"Maze-Adjusted_7th_End" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_7th_End" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_7th_End" AS School_Percentile
,"District_Percentile_Maze-Adjusted_7th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

Composite_7th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_7th AS Year
,School_7th AS School
,Class_7th AS Class
,Secondary_Class_7th AS Secondary_Class
,Teacher_7th AS Teacher
,'7th' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_7th_End AS Test_Date
,Null AS Test_Remote
,Composite_7th_End AS Test_Score
,Benchmark_Status_Composite_7th_End AS Benchmark_Status
,National_DDS_Percentile_Composite_7th_End AS National_DDS_Percentile
,School_Percentile_Composite_7th_End AS School_Percentile
,District_Percentile_Composite_7th_End AS District_Percentile
,Growth_Goal_Composite_7th_End AS Growth_Goal
,Growth_Goal_Type_Composite_7th_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_7th_End AS Growth_Goal_Met
,Growth_Percentile_Composite_7th_End AS Growth_Percentile
,Months_of_Growth_Composite_7th_End AS Months_of_Growth
FROM input
WHERE Year_7th IS NOT NULL""")

End_Scores_7th = pd.concat([ORF_WordsCorrect_7th_End, ORF_Errors_7th_End, ORF_Accuracy_7th_End, MAZE_Correct_7th_End, MAZE_Incorrect_7th_End, MAZE_Adjusted_7th_End, Composite_7th_End])

Scores_7th = pd.concat([Beginning_Scores_7th, Middle_Scores_7th, End_Scores_7th])

print ("Formatting 8th Grade Scores...")

ORF_WordsCorrect_8th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Beginning' AS Administration
,Form_ORF_8th_Beginning AS Test_Form
,Date_ORF_8th_Beginning AS Test_Date
,Remote_ORF_8th_Beginning AS Test_Remote
,"ORF-WordsCorrect_8th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_8th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_8th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_8th_Beginning" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_8th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

ORF_Errors_8th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-Errors' AS Subtest
,'Beginning' AS Administration
,Form_ORF_8th_Beginning AS Test_Form
,Date_ORF_8th_Beginning AS Test_Date
,Remote_ORF_8th_Beginning AS Test_Remote
,"ORF-Errors_8th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_8th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Errors_8th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

ORF_Accuracy_8th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Beginning' AS Administration
,Form_ORF_8th_Beginning AS Test_Form
,Date_ORF_8th_Beginning AS Test_Date
,Remote_ORF_8th_Beginning AS Test_Remote
,"ORF-Accuracy_8th_Beginning" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_8th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_8th_Beginning" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_8th_Beginning" AS School_Percentile
,"District_Percentile_ORF-Accuracy_8th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Correct_8th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Correct' AS Subtest
,'Beginning' AS Administration
,Form_Maze_8th_Beginning AS Test_Form
,Date_Maze_8th_Beginning AS Test_Date
,Remote_Maze_8th_Beginning AS Test_Remote
,"Maze-Correct_8th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_8th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Correct_8th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Incorrect_8th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Beginning' AS Administration
,Form_Maze_8th_Beginning AS Test_Form
,Date_Maze_8th_Beginning AS Test_Date
,Remote_Maze_8th_Beginning AS Test_Remote
,"Maze-Incorrect_8th_Beginning" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_8th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Incorrect_8th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Adjusted_8th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Beginning' AS Administration
,Form_Maze_8th_Beginning AS Test_Form
,Date_Maze_8th_Beginning AS Test_Date
,Remote_Maze_8th_Beginning AS Test_Remote
,"Maze-Adjusted_8th_Beginning" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_8th_Beginning" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_8th_Beginning" AS School_Percentile
,"District_Percentile_Maze-Adjusted_8th_Beginning" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

Composite_8th_Beginning = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'Composite' AS Subtest
,'Beginning' AS Administration
,Null AS Test_Form
,Date_Composite_8th_Beginning AS Test_Date
,Null AS Test_Remote
,Composite_8th_Beginning AS Test_Score
,Benchmark_Status_Composite_8th_Beginning AS Benchmark_Status
,National_DDS_Percentile_Composite_8th_Beginning AS National_DDS_Percentile
,School_Percentile_Composite_8th_Beginning AS School_Percentile
,District_Percentile_Composite_8th_Beginning AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

Beginning_Scores_8th = pd.concat([ORF_WordsCorrect_8th_Beginning, ORF_Errors_8th_Beginning, ORF_Accuracy_8th_Beginning, MAZE_Correct_8th_Beginning, MAZE_Incorrect_8th_Beginning, MAZE_Adjusted_8th_Beginning, Composite_8th_Beginning])

ORF_WordsCorrect_8th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'Middle' AS Administration
,Form_ORF_8th_Middle AS Test_Form
,Date_ORF_8th_Middle AS Test_Date
,Remote_ORF_8th_Middle AS Test_Remote
,"ORF-WordsCorrect_8th_Middle" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_8th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_8th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_8th_Middle" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_8th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

ORF_Errors_8th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-Errors' AS Subtest
,'Middle' AS Administration
,Form_ORF_8th_Middle AS Test_Form
,Date_ORF_8th_Middle AS Test_Date
,Remote_ORF_8th_Middle AS Test_Remote
,"ORF-Errors_8th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_8th_Middle" AS School_Percentile
,"District_Percentile_ORF-Errors_8th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

ORF_Accuracy_8th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-Accuracy' AS Subtest
,'Middle' AS Administration
,Form_ORF_8th_Middle AS Test_Form
,Date_ORF_8th_Middle AS Test_Date
,Remote_ORF_8th_Middle AS Test_Remote
,"ORF-Accuracy_8th_Middle" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_8th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_8th_Middle" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_8th_Middle" AS School_Percentile
,"District_Percentile_ORF-Accuracy_8th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Correct_8th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Correct' AS Subtest
,'Middle' AS Administration
,Form_Maze_8th_Middle AS Test_Form
,Date_Maze_8th_Middle AS Test_Date
,Remote_Maze_8th_Middle AS Test_Remote
,"Maze-Correct_8th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_8th_Middle" AS School_Percentile
,"District_Percentile_Maze-Correct_8th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Incorrect_8th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'Middle' AS Administration
,Form_Maze_8th_Middle AS Test_Form
,Date_Maze_8th_Middle AS Test_Date
,Remote_Maze_8th_Middle AS Test_Remote
,"Maze-Incorrect_8th_Middle" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_8th_Middle" AS School_Percentile
,"District_Percentile_Maze-Incorrect_8th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Adjusted_8th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'Middle' AS Administration
,Form_Maze_8th_Middle AS Test_Form
,Date_Maze_8th_Middle AS Test_Date
,Remote_Maze_8th_Middle AS Test_Remote
,"Maze-Adjusted_8th_Middle" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_8th_Middle" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_8th_Middle" AS School_Percentile
,"District_Percentile_Maze-Adjusted_8th_Middle" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

Composite_8th_Middle = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'Composite' AS Subtest
,'Middle' AS Administration
,Null AS Test_Form
,Date_Composite_8th_Middle AS Test_Date
,Null AS Test_Remote
,Composite_8th_Middle AS Test_Score
,Benchmark_Status_Composite_8th_Middle AS Benchmark_Status
,National_DDS_Percentile_Composite_8th_Middle AS National_DDS_Percentile
,School_Percentile_Composite_8th_Middle AS School_Percentile
,District_Percentile_Composite_8th_Middle AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

Middle_Scores_8th = pd.concat([ORF_WordsCorrect_8th_Middle, ORF_Errors_8th_Middle, ORF_Accuracy_8th_Middle, MAZE_Correct_8th_Middle, MAZE_Incorrect_8th_Middle, MAZE_Adjusted_8th_Middle, Composite_8th_Middle])

ORF_WordsCorrect_8th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-WordsCorrect' AS Subtest
,'End' AS Administration
,Form_ORF_8th_End AS Test_Form
,Date_ORF_8th_End AS Test_Date
,Remote_ORF_8th_End AS Test_Remote
,"ORF-WordsCorrect_8th_End" AS Test_Score
,"Benchmark_Status_ORF-WordsCorrect_8th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-WordsCorrect_8th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-WordsCorrect_8th_End" AS School_Percentile
,"District_Percentile_ORF-WordsCorrect_8th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

ORF_Errors_8th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-Errors' AS Subtest
,'End' AS Administration
,Form_ORF_8th_End AS Test_Form
,Date_ORF_8th_End AS Test_Date
,Remote_ORF_8th_End AS Test_Remote
,"ORF-Errors_8th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_ORF-Errors_8th_End" AS School_Percentile
,"District_Percentile_ORF-Errors_8th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

ORF_Accuracy_8th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'ORF-Accuracy' AS Subtest
,'End' AS Administration
,Form_ORF_8th_End AS Test_Form
,Date_ORF_8th_End AS Test_Date
,Remote_ORF_8th_End AS Test_Remote
,"ORF-Accuracy_8th_End" AS Test_Score
,"Benchmark_Status_ORF-Accuracy_8th_End" AS Benchmark_Status
,"National_DDS_Percentile_ORF-Accuracy_8th_End" AS National_DDS_Percentile
,"School_Percentile_ORF-Accuracy_8th_End" AS School_Percentile
,"District_Percentile_ORF-Accuracy_8th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Correct_8th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Correct' AS Subtest
,'End' AS Administration
,Form_Maze_8th_End AS Test_Form
,Date_Maze_8th_End AS Test_Date
,Remote_Maze_8th_End AS Test_Remote
,"Maze-Correct_8th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Correct_8th_End" AS School_Percentile
,"District_Percentile_Maze-Correct_8th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Incorrect_8th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Incorrect' AS Subtest
,'End' AS Administration
,Form_Maze_8th_End AS Test_Form
,Date_Maze_8th_End AS Test_Date
,Remote_Maze_8th_End AS Test_Remote
,"Maze-Incorrect_8th_End" AS Test_Score
,Null AS Benchmark_Status
,Null AS National_DDS_Percentile
,"School_Percentile_Maze-Incorrect_8th_End" AS School_Percentile
,"District_Percentile_Maze-Incorrect_8th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

MAZE_Adjusted_8th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'MAZE-Adjusted' AS Subtest
,'End' AS Administration
,Form_Maze_8th_End AS Test_Form
,Date_Maze_8th_End AS Test_Date
,Remote_Maze_8th_End AS Test_Remote
,"Maze-Adjusted_8th_End" AS Test_Score
,"Benchmark_Status_Maze-Adjusted_8th_End" AS Benchmark_Status
,"National_DDS_Percentile_Maze" AS National_DDS_Percentile
,"School_Percentile_Maze-Adjusted_8th_End" AS School_Percentile
,"District_Percentile_Maze-Adjusted_8th_End" AS District_Percentile
,Null AS Growth_Goal
,Null AS Growth_Goal_Type
,Null AS Growth_Goal_Met
,Null AS Growth_Percentile
,Null AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

Composite_8th_End = psql.sqldf("""
SELECT 
District_Name
,District_Institutional_ID
,Last
,First
,Student_ID
,Secondary_ID
,Birth_Date
,Race_Ethnicity
,Gender
,Free_Reduced_Lunch
,Special_Education
,Disability_Status_Spec_Ed_Category_Services_Provided
,Additional_Codes
,DIBELS_Approved_Accommodations
,Year_8th AS Year
,School_8th AS School
,Class_8th AS Class
,Secondary_Class_8th AS Secondary_Class
,Teacher_8th AS Teacher
,'8th' AS Grade
,'Composite' AS Subtest
,'End' AS Administration
,Null AS Test_Form
,Date_Composite_8th_End AS Test_Date
,Null AS Test_Remote
,Composite_8th_End AS Test_Score
,Benchmark_Status_Composite_8th_End AS Benchmark_Status
,National_DDS_Percentile_Composite_8th_End AS National_DDS_Percentile
,School_Percentile_Composite_8th_End AS School_Percentile
,District_Percentile_Composite_8th_End AS District_Percentile
,Growth_Goal_Composite_8th_End AS Growth_Goal
,Growth_Goal_Type_Composite_8th_End AS Growth_Goal_Type
,Growth_Goal_Met_Composite_8th_End AS Growth_Goal_Met
,Growth_Percentile_Composite_8th_End AS Growth_Percentile
,Months_of_Growth_Composite_8th_End AS Months_of_Growth
FROM input
WHERE Year_8th IS NOT NULL""")

End_Scores_8th = pd.concat([ORF_WordsCorrect_8th_End, ORF_Errors_8th_End, ORF_Accuracy_8th_End, MAZE_Correct_8th_End, MAZE_Incorrect_8th_End, MAZE_Adjusted_8th_End, Composite_8th_End])

Scores_8th = pd.concat([Beginning_Scores_8th, Middle_Scores_8th, End_Scores_8th])

print("Combining data...")

all_scores = pd.concat([Scores_K, Scores_1st, Scores_2nd, Scores_3rd, Scores_4th, Scores_5th, Scores_6th, Scores_7th, Scores_8th])

print(f"All scores file created " + str(len(all_scores.index)) + " rows")

#Eliminate empty rows#
output = psql.sqldf("""SELECT *
FROM all_scores
WHERE Test_Date is not null or Test_score is not null""")

print(f"Simplified DIBELS file created " + str(len(output.index)) + " rows")

#Export to csv
output.to_csv (output_file_location, index=False)

now = datetime.datetime.now()
print ("End date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))