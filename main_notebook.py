#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from marks_calculation import calculate_marks

def main():
    total_courses= int(input("How many courses in this semester? "))
    credits= []  #stores all course credits entered by user
    grades_points= [] #stores all grade points from grades
    
    for i in range(total_courses):
        print(f" Course {i+1} details: ")
        course_type= input("Enter course type (LT,LTP,LP,P,PJ):").upper()
        credit= float(input("Enter course Credits:"))
        total, grade, gp = calculate_marks(course_type)
        print(f" Course {i+1}:\n Total marks: {total: .2f}\n Grade: {grade}\n Grade Points: {gp}")
        credits.append(credit)
        grades_points.append(gp*credit)

    if sum(credits) ==0:
        print("Total credits cannot be zero.")
        
        return 
    cgpa= sum(grades_points)/ sum(credits)
    print(f"Your Semester CGPA is :{cgpa: .2f}")
              
main()


# In[ ]:





# In[ ]:




