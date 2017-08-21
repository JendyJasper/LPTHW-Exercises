# the %d below formats the text and add the 10 at the end of the code
x = 'There are %d types of people' %10
binary = 'binary'
do_not = "don't"
#this has a multiple string formats and hence added with a parenthesis ()
y = 'Those who know %s and those who %s.' %(binary, do_not)

print x
print y

print 'i said : %r' %x 
#the below code has a string inside a string 
print ' I also said : "%s".' %y 

hilarious = False
# the %r prints everything contained in the variable
joke_evaluation = "Isn't that joke do funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

#This adds this two variables above
print w + e