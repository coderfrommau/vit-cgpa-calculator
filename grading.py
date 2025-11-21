def grade_from_marks(total):
    if total >= 90:
        return 'S', 10
    elif total >= 80:
        return 'A', 9
    elif total >= 70:
        return 'B', 8
    elif total >= 60:
        return 'C', 7
    elif total >=50:
        return 'D', 6
    elif total >=40:
        return 'E', 5
    else:
        return 'F', 0