#!/usr/bin/python2.7

import re
import mechanize


# Open D&D website survey in English
br = mechanize.Browser()

br.addheaders = [('User-agent', 'Android')]
#Tell the robot to say it's not a robot
br.set_handle_robots(False)
page1= br.open("https://www.telldunkin.com/Index.aspx?LanguageID=US")
#        _.-------._
#      .'    ___    '.
#     /     (___)     \
#     |'._         _.'|
#     |   `'-----'`   |
#      \             /
#       '-.______..-'

print "        _.-------._\n      .'    ___    '.\n     /     (___)     \\\n     |'._         _.'|\n     |   `'-----'`   |\n      \             /\n       '-.______..-'\n"
print "     ---FREE DONUT!---\n"
# Prints out the page
# print page1.read()

# Prints each form for debugging purposes
#for form in br.forms():
#     print "Form name:", form.name
#     print form

# Select the "form" on the page to edit further

# when the form has a name use
#     br.select_form("form1")

# when the form has no name
br.form = list(br.forms())[0]

# Prints the controls for the selected form
#for control in br.form.controls:
#     print control
#     print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

# Controls can be found by name
box1 = br.form.find_control("CN1")
box2 = br.form.find_control("CN2")
box3 = br.form.find_control("CN3")
box4 = br.form.find_control("CN4")

# User Input

code = raw_input("Enter Survey Code: \n")
# Set values

box1.value = code[0:5]
box2.value = code[5:10]
box3.value = code[10:14]
box4.value = code[14:18]


# Submit the code
response = br.submit()

# Prints the HTML spaghetti
# print response.read()

# Should be the same as the response
page2= br.response()
# print page2.read()

# Select the next form
br.form = list(br.forms())[0]

# Grab each survey option
option1 = br.form.find_control("R00232")
option2 = br.form.find_control("R00381")
option3 = br.form.find_control("R00247")
option4 = br.form.find_control("R00238")
option5 = br.form.find_control("R00243")
option6 = br.form.find_control("R00245")
option7 = br.form.find_control("R00011")
option8 = br.form.find_control("R00389")
option9 = br.form.find_control("R00384")
option10 = br.form.find_control("R00251")

# Set each option to 'Highly Satisfied'

option1.value = ["5"]
option2.value = ["5"]
option3.value = ["5"]
option4.value = ["5"]
option5.value = ["5"]
option6.value = ["5"]
option7.value = ["5"]
option8.value = ["5"]
option9.value = ["5"]
option10.value = ["5"]

# Submit the code                                                                                                  
response2 = br.submit()                                                                                                          
# Prints the HTML spaghetti                                                                                        
# print response.read()                                                                                              
                                                                                                                   
# Should be the same as the response                                                                               
page3= br.response()                                                                                               
# print page3.read()

# Select the next form
br.form = list(br.forms())[0]

# Grab each survey option
option1 = br.form.find_control("R00252")
option2 = br.form.find_control("R00283")
option3 = br.form.find_control("R00284")
option4 = br.form.find_control("R00288")
option5 = br.form.find_control("R00286")
option6 = br.form.find_control("R00287")
option7 = br.form.find_control("R00285")
option8 = br.form.find_control("R00376")

# Were you satified with your purchase
option1.value = ["2"]
option2.value = ["1"]
option3.value = ["1"]
option4.value = ["1"]
option5.value = ["1"]
option6.value = ["1"]
option7.value = ["1"]
option8.value = ["1"]

response3 = br.submit()
# print response.read()
page4= br.response()
# print page4.read()


br.form = list(br.forms())[0]

option1 = br.form.find_control("R00391")
option2 = br.form.find_control("R00392")
option3 = br.form.find_control("R00387")
option4 = br.form.find_control("R00388")
option5 = br.form.find_control("R00356")
option6 = br.form.find_control("R00366")

option1.value = ["5"]
option2.value = ["5"]
option3.value = ["2"]
option4.value = ["1"]
option5.value = ["1"]
option6.value = ["2"]

response4 = br.submit()
# print response.read()
page5= br.response()
# print page5.read()

br.form = list(br.forms())[0]

option1 = br.form.find_control("R00078")
option1.value = ["1"]

response5 = br.submit()
# print response.read()
page6= br.response()
# print page6.read()

br.form = list(br.forms())[0]

option1 = br.form.find_control("S58200")
option2 = br.form.find_control("S00082")

#email= raw_input("Enter your email")
#option1.value = email
#option2.value = email

option1.value = "chrisae9@gmail.com"
option2.value = "chrisae9@gmail.com"

response6 = br.submit()
# print response.read()
page7= br.response()
# print page7.read()

print "\nYou should Receive an email soon :)"
