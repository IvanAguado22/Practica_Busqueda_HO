from constraint import *

problem = Problem()

satelites = ['SAT1_F1', 'SAT2_F1', 'SAT3_F1',
    'SAT3_F2' 'SAT4_F1', 'SAT5_F1', 'SAT6_F1', 'SAT6_F2']
antenas = ['ANT1', 'ANT2', 'ANT3', 'ANT4', 'ANT5', 'ANT6',
           'ANT7', 'ANT8', 'ANT9', 'ANT10', 'ANT11', 'ANT12']

satelitesPre12 = [satelites[0], satelites[1],
                  satelites[2], satelites[5], satelites[6]]

satelitesPre12 = [satelites[3], satelites[4], satelites[7]]

problem.addVariables(satelites[0], antenas[:4])
problem.addVariables(satelites[1], antenas[:3])
problem.addVariables(satelites[2], antenas[3:6:2])
problem.addVariables(satelites[3], (antenas[6], antenas[8], antenas[9]))
problem.addVariables(satelites[4], (antenas[7], antenas[10], antenas[11]))
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
