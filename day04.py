import copy
subjects = [1,2,[3,4],5]
a = subjects
b = a.copy()
c = list(subjects)
d = subjects[:]
e = copy.deepcopy(subjects)
subjects[2][1] = 2
print(subjects ,a, b, c, d, e)