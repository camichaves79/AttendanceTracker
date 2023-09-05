import sys
from models import Student
from utilities import add_time

def main():
    """ Prepare a students hash table for ease of writing/access to student's record """
    students = dict()

    """ load the input file using the argument from the command line as the file's name (ei. input.txt) """
    with open (sys.argv[1], "r") as f:

        """ Generate a list of commands """
        line = f.read().split("\n")

        """ iterate the command list the fewest times possible """
        for instruction in line:

            """ validate in order to exclude empty lines in the input file """
            if instruction:

                """ separate each command line  into a list for easy retrieval using indexes """
                instruction_set = instruction.split(" ")
                """ load the student's name into a variable for easy access as it will be used many times """
                student_name = instruction_set[1]

                """ Validate the kind of instruction and proceed accordingly """
                if instruction_set[0] == "Student":

                    """ when there's a command to create a student, instanciate the Student class and associate the resulting
                    object with the studen't name """
                    students[student_name] = Student(student_name)
                
                elif instruction_set[0] == "Presence":
                    """ when a student's presence command, add the minutes and the day of the week of the presence
                    add presence minutes """
                    students[student_name].minutes += add_time(instruction_set[3],instruction_set[4])
                    """ record a day of the week """
                    students[student_name].days.add(instruction_set[2])
    
    """ Sort the students' presence records in descending order, and filter out and presence of less than 5 minutes
    """
    sorted_students = sorted(students.values(), key=lambda student: student.minutes, reverse=True)

    for student in sorted_students:
        if student.minutes < 5:
            continue
        print("{}: {} minutes in {} days".format(student.name, student.minutes, len(student.days)))

if __name__ == "__main__":
    main()
    