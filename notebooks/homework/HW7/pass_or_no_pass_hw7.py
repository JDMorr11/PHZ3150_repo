#!/usr/bin/env python
# coding: utf-8

# In[16]:


def pass_or_no_pass(all_grades):
    """Input a 10 by 10 array: 10 students, 1 column of student ID's, 5 columns of HW grades, 3 columns of quiz grades, 1 column of final exam grades. \n Calculates each student's grade using 60% the final exam grade, 15% the quizzes grade and 25% the homework grade. \n Outputs student ID, grade, and whether they earnded a passing grade of at least 60% """
    import numpy as np
    student = int(input('Student 1-10: '))
    out = []
    for i in all_grades:
        ID = int(i[0])
        HW = np.mean(i[1:6])
        QZ = np.mean(i[6:9])
        grade = round((0.6 * i[9]) + (0.15 * QZ) + (0.25 * HW), 2)
        if grade < 60:
            passed = 'no pass'
        else:
            passed = 'pass'
        results = (ID, grade, passed)
        out.append(results)
    return out[student-1]

