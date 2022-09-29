import re

str ="Suneel@gmail.com"

splChars = re.compile('[`!@#$%^&*(){}\|;,./:<>?]')

if (splChars.search(str) == None):
    print ("No special characters in the given statement!")
else:
    print ("Special Characters:", splChars.search(str))