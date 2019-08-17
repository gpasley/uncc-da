-- List the following details of each employee: employee number, last name, first name, gender, and salary.

select e.emp_no, last_name, first_name, gender, salary
from employees e left outer join salaries s on e.emp_no = s.emp_no

-- List employees who were hired in 1986.

select * from employees where hire_date >= '1986-01-01' and hire_date <= '1986-12-31'

-- List the manager of each department with the following information: department number, department name, 
-- the manager's employee number, last name, first name, and start and end employment dates.

select d.dept_no, dept_name, e.emp_no, last_name, first_name, m.from_date, m.to_date 
from departments d left outer join dept_manager m on d.dept_no = m.dept_no
left outer join employees e on m.emp_no = e.emp_no


-- List the department of each employee with the following information: employee number, 
-- last name, first name, and department name.

select e.emp_no, last_name, first_name, dept_name
from employees e left outer join dept_emp de on e.emp_no=de.emp_no
left outer join departments d on de.dept_no = d.dept_no

-- List all employees whose first name is "Hercules" and last names begin with "B."

select first_name, last_name from employees
where first_name = 'Hercules' and last_name like 'B%'

-- List all employees in the Sales department, including their employee number, last name, 
-- first name, and department name.

select e.emp_no, last_name, first_name, dept_name
from employees e left outer join dept_emp de on e.emp_no=de.emp_no
left outer join departments d on de.dept_no = d.dept_no
where d.dept_no = 'd007'

-- List all employees in the Sales and Development departments, including their employee number, 
-- last name, first name, and department name.

select e.emp_no, last_name, first_name, dept_name
from employees e left outer join dept_emp de on e.emp_no=de.emp_no
left outer join departments d on de.dept_no = d.dept_no
where d.dept_no in ('d005','d007')

-- In descending order, list the frequency count of employee last names, i.e., how many employees 
-- share each last name.

select last_name, count(last_name) as total from employees group by last_name order by total desc

select * from employees where emp_no = 499942