
# STEP 1: Create the raw data list

raw_data = [
    1121, "Jackie Grainger", 22.22,
    1122, "Jignesh Thrakkar", 25.25,
    1127, "Dion Green", 28.75, False,
    24.32, 1132, "Jacob Gerber",
    "Sarah Sanderson", 23.45, 1137, True,
    "Brandon Heck", 1138, 25.84, True,
    1152, "David Toma", 22.65,
    23.75, 1157, "Charles King", False,
    "Jackie Grainger", 1121, 22.22, False,
    22.65, 1152, "David Toma"
]

# STEP 2: Sort information into a list of dictionary items

employee_list = []
emp_id = None
emp_name = None
emp_wage = None

for item in raw_data:
    # ignore boolean values (noone knows what they are)
    # IMPORTANT: Check bool BEFORE int because bool is a subclass of int
    if isinstance(item, bool):
        continue
    elif isinstance(item, int):
        emp_id = item
    elif isinstance(item, str):
        emp_name = item
    elif isinstance(item, float):
        emp_wage = item

    # Build the employee dictionary with all three pieces of info
    if emp_id is not None and emp_name is not None and emp_wage is not None:
        employee_dict = {
            "employee_id": emp_id,
            "employee_name": emp_name,
            "hourly_wage": emp_wage
        }
        employee_list.append(employee_dict)
        # Reset for the next employee
        emp_id = None
        emp_name = None
        emp_wage = None

# STEP 3: Remove duplicate employees (keep first occurrence)

unique_employee_list = []
seen_ids = set()

for emp in employee_list:
    if emp["employee_id"] not in seen_ids:
        unique_employee_list.append(emp)
        seen_ids.add(emp["employee_id"])

# STEP 4: Calculate total hourly rate (wage * 1.3 for benefits)

for emp in unique_employee_list:
    emp["total_hourly_rate"] = round(emp["hourly_wage"] * 1.3, 2)
    
# STEP 5: Identify underpaid employees (total rate between 28.15 and 30.65)

underpaid_salaries = []

for emp in unique_employee_list:
    if 28.15 <= emp["total_hourly_rate"] <= 30.65:
        underpaid_salaries.append(emp)
        
     
# STEP 6: Calculate raises based on hourly wage 

company_raises = []

for emp in unique_employee_list:
    wage = emp["hourly_wage"]

    if 22 <= wage < 24:
        raise_pct = 0.05      # 5% raise
    elif 24 <= wage < 26:
        raise_pct = 0.04      # 4% raise
    elif 26 <= wage < 28:
        raise_pct = 0.03      # 3% raise
    else:
        raise_pct = 0.02      # 2% standard raise

    raise_amount = round(wage * raise_pct, 2)

    company_raises.append({
        "employee_name": emp["employee_name"],
        "raise_amount": raise_amount
    })
    
# STEP 7: Print all three lists

print("=" * 60)
print("EMPLOYEE DATABASE")
print("=" * 60)
for emp in unique_employee_list:
    print(emp)

print("\n" + "=" * 60)
print("UNDERPAID EMPLOYEES")
print("=" * 60)
for emp in underpaid_salaries:
    print(emp)

print("\n" + "=" * 60)
print("COMPANY RAISES")
print("=" * 60)
for raise_info in company_raises:
    print(raise_info)
    