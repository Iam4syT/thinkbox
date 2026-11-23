from solution import review
good = {'duration':'one year','mode':'full time'}
assert review('sample-course',good) == 'ready for reviewer'
for course,answer in [('unknown',good),('sample-course',{}),('sample-course',{'link':'example'}),('sample-course',dict(good,duration='two years')),('sample-course',dict(good,fee='free'))]:
    assert review(course,answer) == 'human review'
print('6 course answer checks passed')
