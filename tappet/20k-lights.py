# the problem from NPR show Click and Clack (Tappet Brothers). It's about an array of 20,000 lights.
# The first person turns on all the lights, the 2nd person switches every 2nd light, 
# the 3rd person switches every 3rd light and so on.
# 20,000 people do this.

import math as m

lights = 20000
answer = [1]
for i in xrange(2,int(m.sqrt(lights))+1):
    term = i*i
    answer.append(term)

print "There will be ", len(answer), " lights left on out of the original ", lights, "."
print "These lights will be on: ", answer   
 
# Explanation:
# The factors of any number come in pairs of unique numbers, unless they involve squares:
# factors of  8: 1 2 4 8
# The 8th light is switched an even number of times, 2 times in each factor pair (1*8,2*4)
# factors of 16: 1 2 4 4 8 16
# In the case of 16, the 4th switcher only switches light 16 once, so this "pair" (4*4) is not completed.
# Any odd number of flips means the light is on at the end. 
# So to answer this riddle, you have to find the squares <= 20,000.
