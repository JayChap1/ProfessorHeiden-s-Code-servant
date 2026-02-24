# Week 7-8 Assignment - Functions, Scopes, and Arguments
# Jason Chapman - Python Programming I - Professor Heiden
# Walsh College
# Repo: https://github.com/JayChap1/ProfessorHeiden-s-Code-servant
#
# This is my Week 6 employee program but refactored to use functions.
# Main thing I changed was getting rid of all the repeated while True loops
# and putting them into one reusable function. Also added JSON file output.

import json


# ---- VALIDATION FUNCTIONS ----
# These are the same from Week 6, they were already functions.
# They check user input and return True if it's good, False if not.

def validate_employee_id(emp_id):
    """Checks Employee ID - required, digits only, max 7 characters."""
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
    """Checks name - required, letters/spaces/apostrophes/hyphens only."""
    if name.strip() == '':
        print("  >> Employee Name is required. Try again.")
        return False
    for char in name.strip():
        if not (char.isalpha() or char in " '-"):
            print(f"  >> '{char}' isn't allowed in a name. Letters, spaces, apostrophes, and hyphens only.")
            return False
    return True


def validate_employee_email(email):
    """Checks email - required, no banned special characters."""
    disallowed_email = set('!"\'#$%^&*()=+,<>/?;:[]{}\\')
    if email.strip() == '':
        print("  >> Employee Email is required. Try again.")
        return False
    for char in email.strip():
        if char in disallowed_email:
            print(f"  >> '{char}' isn't allowed in an email address. Try again.")
            return False
    return True


def validate_employee_address(address):
    """Checks address - this one is optional so empty is fine."""
    disallowed_address = set('!"\'@$%^&*_=+<>?;:[]{}')
    # empty is OK since address isn't required
    if address.strip() == '':
        return True
    for char in address.strip():
        if char in disallowed_address:
            print(f"  >> '{char}' isn't allowed in an address. Try again.")
            return False
    return True


def validate_employee_salary(salary_input):
    """Checks salary - required, must be a number between 18 and 27."""
    if salary_input.strip() == '':
        print("  >> Employee Salary is required. Try again.")
        return False
    try:
        salary = float(salary_input.strip())
    except ValueError:
        print("  >> That's not a valid number. Try again.")
        return False
    if salary < 18 or salary > 27:
        print("  >> Salary has to be between 18.00 and 27.00. Try again.")
        return False
    return True


# ---- GET VALIDATED INPUT ----
# This is the main refactor. In Week 6 I had the same while True / break
# pattern copied 5 times (once per field). That's the redundancy
# Chapter 16 talks about. Now it's one function - you pass in what to
# ask and which validator to use. The convert parameter is for salary
# since that one needs to come back as a float instead of a string.

def get_validated_input(prompt, validator, convert=None):
    """Loops until input passes validation. Can optionally convert the result."""
    while True:
        user_input = input(prompt)
        if validator(user_input):
            cleaned = user_input.strip()
            if convert:
                return convert(cleaned)
            return cleaned


# ---- GATHER ALL EMPLOYEE DATA ----
# Collects the 5 fields for one employee. Each field is now just
# one function call instead of its own while True block.

def gather_employee_data():
    """Gets all 5 fields for one employee, returns a dictionary."""

    emp_id = get_validated_input(
        "Enter Employee ID (up to 7 digits): ",
        validate_employee_id
    )

    emp_name = get_validated_input(
        "Enter Employee Name: ",
        validate_employee_name
    )

    emp_email = get_validated_input(
        "Enter Employee Email: ",
        validate_employee_email
    )

    emp_address = get_validated_input(
        "Enter Employee Address (optional - press Enter to skip): ",
        validate_employee_address
    )

    # salary needs float conversion so I pass convert=float
    emp_salary = get_validated_input(
        "Enter Employee Salary (18.00 - 27.00): ",
        validate_employee_salary,
        convert=float
    )

    employee = {
        'id': emp_id,
        'name': emp_name,
        'email': emp_email,
        'address': emp_address,
        'salary': emp_salary
    }
    return employee


# ---- COMPREHENSION FUNCTIONS ----
# Same comprehensions from Week 6 but wrapped in functions now.
# Added default arguments so they could be reused with different
# values if needed (different department, different raise amount, etc.)

def add_department_to_names(employee_list, department="IT Department"):
    """Adds department name to every employee using a comprehension."""
    return [{**emp, 'name': emp['name'] + ' - ' + department} for emp in employee_list]


def adjust_salaries(employee_list, multiplier=1.30):
    """Bumps salaries by the multiplier. Default is 1.30 for the 30% benefits increase."""
    return [{**emp, 'salary': round(emp['salary'] * multiplier, 2)} for emp in employee_list]


# ---- JSON OUTPUT ----
# New for this assignment. Writes the employee list to a JSON file
# so the data persists after the program ends.

def save_to_json(employee_list, filename="employee_data.json"):
    """Saves employee list to a JSON file."""
    try:
        with open(filename, 'w') as json_file:
            json.dump(employee_list, json_file, indent=4)
        print(f"  >> Employee data saved to '{filename}'")
    except IOError:
        print(f"  >> Error: Could not write to '{filename}'")


# ---- PRINT REPORT ----
# Formats and prints the final employee report.

def print_employee_report(employee_list):
    """Prints the formatted employee report."""
    print("\n" + "=" * 55)
    print("       FINAL EMPLOYEE REPORT (UPDATED)")
    print("=" * 55)

    for i, emp in enumerate(employee_list, 1):
        print(f"\n  Employee #{i}")
        print(f"  {'ID:':<12} {emp['id']}")
        print(f"  {'Name:':<12} {emp['name']}")
        print(f"  {'Email:':<12} {emp['email']}")
        if emp['address']:
            print(f"  {'Address:':<12} {emp['address']}")
        else:
            print(f"  {'Address:':<12} (not provided)")
        print(f"  {'Salary:':<12} ${emp['salary']:.2f}/hr (includes 30% benefits)")
        print(f"  {'-' * 43}")

    print(f"\n  Total Employees Entered: {len(employee_list)}")
    avg_salary = sum(emp['salary'] for emp in employee_list) / len(employee_list)
    print(f"  Average Adjusted Salary:  ${avg_salary:.2f}/hr")

    print("\n" + "=" * 55)
    print("       END OF REPORT")
    print("=" * 55)


# ---- MAIN PROGRAM ----

def main():
    employee_list = []
    employee_count = 0

    print("=" * 55)
    print("       EMPLOYEE INFORMATION GATHERING SYSTEM")
    print("=" * 55)

    while True:
        employee_count += 1
        print(f"\n--- Employee #{employee_count} ---")

        # this one function call replaces all the validation loops from week 6
        employee = gather_employee_data()
        employee_list.append(employee)
        print(f"  >> Employee '{employee['name']}' added!")

        while True:
            another = input("\nEnter another employee? (yes/no): ").strip().lower()
            if another in ('yes', 'y', 'no', 'n'):
                break
            print("  >> Just type 'yes' or 'no'.")

        if another in ('no', 'n'):
            break

    # apply the comprehension modifications
    print("\n" + "=" * 55)
    print("       APPLYING MODIFICATIONS")
    print("=" * 55)

    employee_list = add_department_to_names(employee_list)
    print("  >> Added 'IT Department' to all employee names.")

    employee_list = adjust_salaries(employee_list)
    print("  >> Updated all salaries with 30% benefits adjustment.")

    # print report and save to file
    print_employee_report(employee_list)
    save_to_json(employee_list)


if __name__ == "__main__":
    main()