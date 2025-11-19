from attendence import attendence_marks
from grading import grade_from_marks

def calculate_marks(course_type):
    print(f" Enter Marks for {course_type} course: ")
    
    if course_type in ['LT','LTP','LP']:
        mid= float(input("Enter Mid-Term Marks (out of 50): "))
        tee= float(input("Enter Term- End Marks (out of 100): "))
        att_percent= float(input(" Attendence Percentage % : "))
        att= attendence_marks(att_percent)
        
        if course_type == 'LT':
            assignment= float(input("Enter Assignment Marks (out of 10): "))
            group= float(input("Enter Group Activity Marks (out of 5): "))
            quiz= float(input("Enter Quiz marks (out of 10): "))
            tutorial= float(input("Enter Tutorial marks (out of 10): "))
            total= (mid/50*30)+ (tee/100*30)+ att+ assignment +group +quiz +tutorial
            
        elif course_type == 'LTP':
            class_assess= float(input("Enter Class Assessment Marks (out of 10)[5 marks-Tutorial + 5 marks- Group activity]: "))
            lab_assess= float(input("Enter Lab Assessment Marks (out of 25)[10 marks for Continous Assessment + 10 marks for Challenging Task + 5 marks for Quiz]: "))
            total= (mid/50*30)+ (tee/100*30)+ class_assess+ lab_assess
            
        elif course_type == 'LP':
            lab_assess= float(input("Enter Lab Assessment Marks (out of 35)[20 marks for Continous Assessment + 15 marks for Challenging Task]: "))
            total= (mid/50*30)+ (tee/100*30)+ lab_assess
            
        pass_cond= (tee >=40) and (mid +tee >= 60)
        
    elif course_type == 'P':
        tee= float(input("Enter Term- End Marks (out of 100): "))
        
        assignment= float(input("Enter Assignment Marks (out of 5): "))
        lab_assess= float(input("Enter Lab Assessment Marks (out of 60)[(40 marks for Continous Assessment + 10 marks for Challenging Task+ 10 Marks for Viva )]: "))
        att_percent= float(input(" Attendence Percentage % : "))
        att= attendence_marks(att_percent)
        total=(tee/100*30) + assignment+ lab_assess +att
        
        pass_cond = (lab_assess >=25) and (lab_assess + tee >= 50)
        
    elif course_type == 'PJ':
        review1= float(input("Enter Review 1 Marks (out of 20): "))
        review2= float(input("Enter Review 2 Marks (out of 30): "))
        review3= float(input("Enter Review 3 Marks (out of 50): "))
        total= review1 + review2 + review3
        
        pass_cond = (total >=50)
        
    else:
        print("Invalid course type! ")
        return 0, 'Invalid', 0
    
    grade, gp = grade_from_marks(total)
    if not pass_cond:
     garde, gp = 'F', 0
    return total, grade, gp     
            
        
            
        
        