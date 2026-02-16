

# VALIDATION FUNCTIONS
# Each one checks a specific field and returns True/False.
# Keeps the main loop clean instead of nesting a ton of if/else logic.


def validate_employee_id(emp_id):
    """Checks that Employee ID is not empty, all digits, and 7 or fewer characters."""
    if emp_id.strip() == '':
        print("  >> Employee ID is required. Try again.")
        return False
    if not emp_id.strip().isdigit():
        print("  >> Employee ID must be numbers only. Try again.")
        return False
    if len(emp_id.strip()) > 7:
        print("  >> Employee ID can't be more than 7 digits. Try again.")
        return False
    return True


def validate_employee_name(name):
    """Checks that name is not empty and only contains letters, spaces, apostrophes, or hyphens."""
    if name.strip() == '':
        print("  >> Employee Name is required. Try again.")
        return False
    # Loop through each character - only allow letters, spaces, ' and -
    for char in name.strip():
        if not (char.isalpha() or char in " '-"):
            print(f"  >> '{char}' isn't allowed in a name. Letters, spaces, apostrophes, and hyphens only.")
            return False
    return True


def validate_employee_email(email):
    """Checks that email is not empty and doesn't contain any of the disallowed characters."""
    # These characters are specifically banned per the assignment
    disallowed_email = set('!"\'#$%^&*()=+,<>/?;:[]{}\\')

    if email.strip() == '':
        print("  >> Employee Email is required. Try again.")
        return False
    # Check every character against the banned set
    for char in email.strip():
        if char in disallowed_email:
            print(f"  >> '{char}' isn't allowed in an email address. Try again.")
            return False
    return True


def validate_employee_address(address):
    """Address is optional. If provided, checks it doesn't contain banned characters."""
    # Different banned set than email - @ is banned here, but not in email
    disallowed_address = set('!"\'@$%^&*_=+<>?;:[]{}')

    # Empty is fine - address isn't required
    if address.strip() == '':
        return True
    # If they typed something, make sure it's clean
    for char in address.strip():
        if char in disallowed_address:
            print(f"  >> '{char}' isn't allowed in an address. Try again.")
            return False
    return True


def validate_employee_salary(salary_input):
    """Checks that salary is not empty, is a valid number, and falls between 18 and 27."""
    if salary_input.strip() == '':
        print("  >> Employee Salary is required. Try again.")
        return False
    # try/except catches anything that isn't a real number
    try:
        salary = float(salary_input.strip())
    except ValueError:
        print("  >> That's not a valid number. Try again.")
        return False
    # Must be in the 18-27 range per assignment rules
    if salary < 18 or salary > 27:
        print("  >> Salary has to be between 18.00 and 27.00. Try again.")
        return False
    return True



# MAIN PROGRAM - DATA COLLECTION
# Outer while loop keeps gathering employees until user says stop.
# Inner while loops handle re-prompting when validation fails.
# True / break pattern from Chapter 13.


# Master list - each employee will be a dictionary appended here
employee_list = []
employee_count = 0

print("=" * 55)
print("       EMPLOYEE INFORMATION GATHERING SYSTEM")
print("=" * 55)

# Keep collecting employees until user says no
while True:
    employee_count += 1
    print(f"\n--- Employee #{employee_count} ---")

    # Get Employee ID - loops until valid input
    while True:
        emp_id = input("Enter Employee ID (up to 7 digits): ")
        if validate_employee_id(emp_id):
            emp_id = emp_id.strip()
            break  # Good input - move on

    # Get Employee Name - loops until valid input
    while True:
        emp_name = input("Enter Employee Name: ")
        if validate_employee_name(emp_name):
            emp_name = emp_name.strip()
            break

    # Get Employee Email - loops until valid input
    while True:
        emp_email = input("Enter Employee Email: ")
        if validate_employee_email(emp_email):
            emp_email = emp_email.strip()
            break

    # Get Employee Address - optional, but still validated if provided
    while True:
        emp_address = input("Enter Employee Address (optional - press Enter to skip): ")
        if validate_employee_address(emp_address):
            emp_address = emp_address.strip()
            break

    # Get Employee Salary - must be a float between 18 and 27
    while True:
        salary_input = input("Enter Employee Salary (18.00 - 27.00): ")
        if validate_employee_salary(salary_input):
            emp_salary = float(salary_input.strip())
            break

    # Build the dictionary for this employee and add it to the list
    employee = {
        'id': emp_id,
        'name': emp_name,
        'email': emp_email,
        'address': emp_address,
        'salary': emp_salary
    }
    employee_list.append(employee)
    print(f"  >> Employee '{emp_name}' added!")

    # Ask if they want to keep going
    while True:
        another = input("\nEnter another employee? (yes/no): ").strip().lower()
        if another in ('yes', 'y', 'no', 'n'):
            break
        print("  >> Just type 'yes' or 'no'.")

    # User said no - break out of the main collection loop
    if another in ('no', 'n'):
        break


# COMPREHENSION MODIFICATIONS
# Assignment requires two specific changes using list comprehensions:
# 1. Append "IT Department" to every employee name
# 2. Bump salary up 30% to reflect total compensation with benefits


print("\n" + "=" * 55)
print("       APPLYING COMPREHENSION MODIFICATIONS")
print("=" * 55)

# Comprehension 1 - Add "IT Department" to each name
# {**emp} unpacks the whole dictionary, then we override just the 'name' key

employee_list = [{**emp, 'name': emp['name'] + ' - IT Department'} for emp in employee_list]
print(">> Added 'IT Department' to all employee names.")

# Comprehension 2 - Increase salary by 30% for benefits
# round() keeps it to 2 decimal places since we're dealing with money

employee_list = [{**emp, 'salary': round(emp['salary'] * 1.30, 2)} for emp in employee_list]
print(">> Updated all salaries with 30% benefits adjustment.")


# FINAL OUTPUT
# Print the updated employee list with formatted output.
# Using enumerate() from Chapter 13 to track the employee number.


print("\n" + "=" * 55)
print("       FINAL EMPLOYEE REPORT (UPDATED)")
print("=" * 55)

# Loop through each employee dictionary and display their info
for i, emp in enumerate(employee_list, 1):
    print(f"\n  Employee #{i}")
    print(f"  {'ID:':<12} {emp['id']}")
    print(f"  {'Name:':<12} {emp['name']}")
    print(f"  {'Email:':<12} {emp['email']}")
    # Only show address if they actually gave us one
    if emp['address']:
        print(f"  {'Address:':<12} {emp['address']}")
    else:
        print(f"  {'Address:':<12} (not provided)")
    print(f"  {'Salary:':<12} ${emp['salary']:.2f}/hr (includes 30% benefits)")
    print(f"  {'-' * 43}")

# Quick summary at the bottom
print(f"\n  Total Employees Entered: {len(employee_list)}")

# One more comprehension - pull all salaries to calculate the average
avg_salary = sum(emp['salary'] for emp in employee_list) / len(employee_list)
print(f"  Average Adjusted Salary:  ${avg_salary:.2f}/hr")

print("\n" + "=" * 55)
print("       END OF REPORT")
print("=" * 55)
