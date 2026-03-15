#College Records System
#Author: Jason Chapman
#Course: Python Programming 1
#Professor: Dr. Heiden

import re

class Validator:

    # bad chars that can't be in a name
    NAME_BAD_CHARS = r'[!"@#$%^&*()_=+,<>/?;:\[\]{}\\]'

    # bad chars that can't be in an email
    EMAIL_BAD_CHARS = r'''[!"'#$%^&*()=+,<>/?;:\[\]{}\\ ]'''

    #method to validate name in the static way
    @staticmethod
    def validate_name(name):
        # can't be blank
        if not name.strip():
            return False
        # check for banned characters
        if re.search(Validator.NAME_BAD_CHARS, name):
            return False
        # must be primarily letters — at least half the characters
        letter_count = sum(1 for c in name if c.isalpha())
        return letter_count >= len(name) / 2

    #method to validate name in the static way
    @staticmethod
    def validate_name(name):
        # can't be blank
        if not name.strip():
         return False
        # check for banned characters
        if re.search(Validator.NAME_BAD_CHARS, name):
         return False
        # must be primarily letters — at least half the characters
        letter_count = sum(1 for c in name if c.isalpha())
        return letter_count >= len(name) / 2

    #method to validate email in the static way
    @staticmethod
    def validate_email(email):
        # can't be blank
        if not email.strip():
            return False
        # no banned special characters allowed
        if re.search(Validator.EMAIL_BAD_CHARS, email):
            return False
        # must follow standard email format — something@domain.com
        return bool(re.match(r'^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$', email))

    #method to validate student id in the static way
    @staticmethod
    def validate_student_id(sid):
        # must be all digits and 7 or fewer digits long
        return sid.isdigit() and 1 <= len(sid) <= 7

    #method to validate instructor id in the static way
    @staticmethod
    def validate_instructor_id(iid):
        # must be all digits and 5 or fewer digits long
        return iid.isdigit() and 1 <= len(iid) <= 5

    #generic check — no blank fields allowed
    @staticmethod
    def validate_not_empty(value):
        # strip whitespace and check if anything is left
        return bool(value.strip())


#base class — shared fields for everyone
class Person:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def displayInformation(self):
        # print the shared fields every individual has
        print(f"  Name:  {self.name}")
        print(f"  Email: {self.email}")


#Student class — inherits from Person
class Student(Person):

    def __init__(self, name, email, student_id, program):
        # pull in name and email from Person
        super().__init__(name, email)
        self.student_id = student_id
        self.program = program

    def displayInformation(self):
        # label this record as a student
        print("\n  [STUDENT]")
        # call Person's version first to print name and email
        super().displayInformation()
        # then add the student specific fields
        print(f"  Student ID:       {self.student_id}")
        print(f"  Program of Study: {self.program}")


#Instructor class — inherits from Person
class Instructor(Person):

    def __init__(self, name, email, instructor_id, institution, degree):
        # pull in name and email from Person
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.institution = institution
        self.degree = degree

    def displayInformation(self):
        # label this record as an instructor
        print("\n  [INSTRUCTOR]")
        # call Person's version first to print name and email
        super().displayInformation()
        # then add the instructor specific fields
        print(f"  Instructor ID:    {self.instructor_id}")
        print(f"  Last Institution: {self.institution}")
        print(f"  Highest Degree:   {self.degree}")


#helper function — keeps asking until we get a valid answer
def get_valid_input(prompt, validator_fn, error_msg):
    while True:
        value = input(prompt).strip()
        if validator_fn(value):
            return value
        print(f"  ** {error_msg} — try again.")


#collect one individual's info — student or instructor
def collect_individual():

    # figure out who we're dealing with
    while True:
        role = input("\nEnter type (student/instructor): ").strip().lower()
        if role in ('student', 'instructor'):
            break
        print("  ** Please enter 'student' or 'instructor'.")

    # get name and email — shared for both types
    name = get_valid_input(
        "Enter name: ",
        Validator.validate_name,
        "Invalid name — must be primarily letters with no special characters"
    )

    email = get_valid_input(
        "Enter email: ",
        Validator.validate_email,
        "Invalid email — must be a valid format with no special characters"
    )

    # branch based on role — student or instructor
    if role == 'student':
        sid = get_valid_input(
            "Enter Student ID (up to 7 digits): ",
            Validator.validate_student_id,
            "Student ID must be a number with 7 or fewer digits"
        )
        program = get_valid_input(
            "Enter program of study: ",
            Validator.validate_not_empty,
            "Program of study is required"
        )
        return Student(name, email, sid, program)

    else:
        iid = get_valid_input(
            "Enter Instructor ID (up to 5 digits): ",
            Validator.validate_instructor_id,
            "Instructor ID must be a number with 5 or fewer digits"
        )
        institution = get_valid_input(
            "Enter last institution graduated from: ",
            Validator.validate_not_empty,
            "Institution is required"
        )
        degree = get_valid_input(
            "Enter highest degree earned: ",
            Validator.validate_not_empty,
            "Degree is required"
        )
        return Instructor(name, email, iid, institution, degree)


#main — runs the program, collects records, prints them all out
def main():
    college_records = []

    print("=== Walsh College Records System ===")

    # keep going until the user says stop
    while True:
        individual = collect_individual()
        college_records.append(individual)

        again = input("\nAdd another individual? (yes/no): ").strip().lower()
        if again != 'yes':
            break

    # print out everything we collected
    print("\n" + "=" * 40)
    print("       ALL COLLEGE RECORDS")
    print("=" * 40)

    for i, record in enumerate(college_records, start=1):
        print(f"\nRecord #{i}")
        record.displayInformation()

    print("\n" + "=" * 40)
    print(f"Total records: {len(college_records)}")


#standard entry point — only runs if we execute this file directly
if __name__ == "__main__":
    main()