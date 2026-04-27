from oopconcepts.agecal import AgeCalculation
from oopconcepts.myexception import AgeException

age = int(input(('Age: ')))
aobj = AgeCalculation()

try:
    #if aobj.voting_age_check(age):
        #print('Eligible, Contact next step....')
    aobj.voting_age_check(age)
    aobj.pension_age_check(age)
except AgeException as ae:
    print(ae)
else:
    print('Eligible to Vote, Contact next step....')
