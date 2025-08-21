# A base exception class for our code:
class StudentsDataException(Exception):
    pass


# An exception for erroneous lines:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# An exception for an empty file.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# A dictionary for students' data:
data = { }

file_name = input("Enter student's data filename: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Read the whole file into list.
    lines = f.readlines()
    f.close()
    # Is the file empty?
    if len(lines) == 0:
        raise FileEmpty()
    # Scan the file line by line.
    for i in range(len(lines)):
        # Get the i'th line.
        line = lines[i]
        # Divide it into columns.
        columns = line.split()
        # There shoule be 3 columns - are they there?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Build a key from student's given name and surname.
        student = columns[0] + ' ' + columns[1]
        # Get points.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Update dictionary.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Print results.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))
except WrongLine as e:
    print("Wrong line #" + str(e.line_number) + " in source file:" + e.line_string)
except FileEmpty:
    print("Source file empty")