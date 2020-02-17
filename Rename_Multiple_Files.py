import os
import re
import pydoc
"""This programe will rename all the files within the specified directory"""
dir1=str(input("Enter the full directory path for which you want to rename files:  "))
ori=str(input("Enter the prefix with which you want to rename the file:  "))
ren="_" + ori
Before=[]
After=[]
os.chdir(dir1)
os.getcwd()
for file in os.listdir(dir1):
    A=file.split(".")
    B1=str(A[0])
    B2=str(A[1])
    C=B1 + ren
    D=C + "." + B2
    Before.append(file)
    os.rename(file, D)
    After.append(D)
print("************Before***********\n" )
print(Before)
print("\n")
print("************After***********\n" )
print(After)
print("\n")
print("All Files renamed Successfully")
