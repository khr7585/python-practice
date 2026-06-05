#1.BUILT-IN MODULES
# import math
# print(math.sqrt(25))

#2.USERDEFINED MODULES
# def greet(name):
#     return f"hello,{name}"
# #another file
# import file_name
# print(file_name.greet("hemanth"))

#IMPORT ENTIRE MODULE
# import math
# print(math.pi)

#IMPORT SPECIFIC FUNCTION
# from math import sqrt
# print(sqrt(25))

#IMPORT WITH ALIAS
# import math as m
# print(m.pi)

#USEFUL MODULE FUNCTIONS
# import math
# print(dir(math))




#PIP
#INSTALL A PACKAGE
# pip install numpy

#INSTALL A SPECIFIC VERSION
# pip install numpy==2.0.0

#UPGRADE A PACKAGE
# pip install --upgrade numpy

#UNINSTALL A PACKAGE
# pip uninstall numpy

#LIST INSTALLED PACKAGES
# pip list

#SHOW PACKAGE INFORMATION
# pip show numpy




#VENV
#1.CREATE A VIRTUAL ENVIRONMENT
# python -m venv myenv

#2.ACTIVATE THE VIRTUAL ENVIRONMENT
# myenve\scripts\activate

#3.INSTALL PACKAGES
# pip install requests

#4.DEACTIVATE THE ENVIRONMENT
# deactivate

#5.VIEW INSTALLED PACKAGES
# pip list

#6.SAVE DEPENDECIES
# pip freeze > requirements.txt

#7.INSTALL DEPENDENCIES FROM A FILE
# pip install -r requirements.txt