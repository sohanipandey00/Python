def sum_subject()

def get_percentage(total):
    return total/5
def get_grade(per):
    if per<101 and per>=80:
        return "A"
    elif per<80 and per>=60:
        return "B"
    elif per<60 and per>=40:
        return "C"
    else:
        return "Fail"
total=sum_subject((int(input("Enter marks of English:"))),
                 (int(input("Enter marks of Maths:"))),
                 (int(input("Enter marks of Science:"))),
                 (int(input("Enter marks of SST:"))),
)
print("Sum of all subjects:",total)
percentage=get_percentage(total)
print("Percentage",percent)
gr=get_grade(percent)
print("\n")
print("Grade:",gr)
print("\n")