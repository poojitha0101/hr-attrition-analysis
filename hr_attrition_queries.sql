create database HR_Attrition;
use HR_Attrition;
select * from HR_Attrition;
--Find the total number of employees in each department.
select count(*) from HR_Attrition;
--Find how many employees left the company (Attrition = 'Yes') and how many stayed (Attrition = 'No').
select Attrition, count(*) from HR_Attrition group by Attrition;
--Find the average monthly income of employees who left vs employees who stayed.
select Attrition, Avg(MonthlyIncome)as monthly_income_emplyees_counting from HR_Attrition group by Attrition;
--Find how many employees left the company who were also doing OverTime.
select Attrition, count(OverTime)as counting_employees_who_left from HR_Attrition group by Attrition;
--Find the number of employees who left, grouped by department.
select Department,count(Attrition)as employees_who_left from HR_Attrition where Attrition=1 group by Department;

select * from HR_Attrition;
--Show all column names and data types.
exec sp_help 'HR_Attrition';
-- Min, Max, Avg age of employees who left
select min(Age)as minimum_Age,Max(Age)as Maximun_Age, avg(Age)as Average_Age from HR_Attrition where Attrition=1;
--Attrition by Job Role:
select JobRole,count(*)as counting_Attrition from HR_Attrition group by JobRole order by counting_Attrition desc;
--Attrition rate by Department:
select department, count(*) as total_employees,sum(cast(Attrition as int))as left_count,
round(sum(cast(Attrition as int))*100/count(*),2)as attriton_rate from HR_Attrition group by Department;
-- Departments where attrition > 50:
select Department,count(*) from HR_Attrition group by Department having count(*)>50;