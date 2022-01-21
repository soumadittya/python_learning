# adding another set to a set

# **** Difference between update() and union()
# update() - its directly updates the set
# union() - it does not update the set directly but returns
# the updated value and that value can be stored in a variable  

s1 = {0, 1}
s2 = {2, 3, 0, 1}

# update() function
# this will take only the unique values
s1.update(s2)
print("s1 final : ", s1)

s3 = {0,1, 3}
s4 = {2, 3, 4, 5}
s5 = s3.union(s4)
print("s3 final : ", s3)
print("s5 : ", s5)
