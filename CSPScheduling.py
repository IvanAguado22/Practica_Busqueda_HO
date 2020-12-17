from constraint import *

problem = Problem()

satelites = ['SAT1', 'SAT2', 'SAT3', 'SAT4', 'SAT5', 'SAT6']

problem.addVarible(satelites[6], antenas[6:10:2])
problem.addVarible(satelites[7], antenas[2:5])


def ConsecutiveConstraint(a, b):
    if a == 'ANT12' and b == 'ANT11':
        return False
    return True


def SameFA7_A12(a, b):
    if(a == 'ANT7' and b == 'ANT12') or (a == 'ANT12' and b == 'ANT7'):
        return False
    return True


problem.addConstraint(AllDifferentConstraint(), (satelites[:2])

problem.addConstraint(AllDifferentConstraint(),
                      (satelites[1], satelites[3], satelites[4]))

problem.addConstraint(ConsecutiveConstraint, satelites[5:3:-1])

for i in range(len(satelitesPre12)):
    for j in range(len(satelitesPost12)):
        problem.addConstraint(
            SameFA7_A12, (satelitesPre12[i], satelitesPost12))

solutions=problem.getSolutions()

print(solutions)