# Chapter 11 Assignment: Statement Types in Python
# Jason Chapman - Python Programming I


# =============================================================================
# STATEMENT 1: Tuple Unpacking Assignment
# Reference: Table 11-1
# =============================================================================
# Scenario: Job posting data comes from an API as tuples. Unpacking lets me
# assign each piece to a named variable in one line instead of using indexes.

job_data = ("Data Scientist", "Ford Motor Company", 125000)
job_title, company, salary = job_data

print("=== Tuple Unpacking ===")
print(f"Position: {job_title}")
print(f"Employer: {company}")
print(f"Salary: ${salary:,}")
print()


# =============================================================================
# STATEMENT 2: Extended Sequence Unpacking with Star (*)
# Reference: Table 11-1
# =============================================================================
# Scenario: A skills assessment returns a list where the first item is the
# user's name, the last is their level, and everything in between is scores.
# The star captures that middle section without knowing how many scores exist.

assessment = ["Jason Chapman", 85, 92, 78, 88, 91, "Advanced"]
name, *scores, level = assessment

print("=== Extended Unpacking ===")
print(f"Candidate: {name}")
print(f"Scores: {scores}")
print(f"Level: {level}")
print()


# =============================================================================
# STATEMENT 3: Augmented Assignment (+=)
# Reference: Table 11-2
# =============================================================================
# Scenario: Tracking engagement points as a user completes actions on a
# career platform. Augmented assignment updates the total without retyping
# the variable name.

points = 0

points += 10  # Viewed profile
points += 25  # Completed assessment
points += 15  # Applied to job

print("=== Augmented Assignment ===")
print(f"Total Points: {points}")
print()


# =============================================================================
# STATEMENT 4: Expression Statement (Method Calls)
# Reference: Table 11-4
# =============================================================================
# Scenario: Building a list of in-demand skills. Methods like append() and
# sort() are expression statements - we call them for their side effects,
# not their return value.

skills = ["Python", "SQL"]

skills.append("Machine Learning")
skills.append("Power BI")
skills.sort()

print("=== Expression Statements ===")
print("Skills List:")
for skill in skills:
    print(f"  - {skill}")
print()


# =============================================================================
# STATEMENT 5: Print with sep and end
# Reference: Table 11-5
# =============================================================================
# Scenario: Formatting a report header. The sep parameter controls what goes
# between items, and end controls what comes after.

title = "Career Report"
date = "2025-02-02"
region = "Michigan"

print("=== Print Formatting ===")
print(title, date, region, sep=" | ")
print("Status: ", end="")
print("Complete")