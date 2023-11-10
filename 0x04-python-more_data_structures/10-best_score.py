#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return none
    else:
        dict_list = a_dictionary.items()
        best_grade = 0
        for key, value in dict_list:
            if value > best_grade:
                best_grade = value
                best_student = key
        return best_student
