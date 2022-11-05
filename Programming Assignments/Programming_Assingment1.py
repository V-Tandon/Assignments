#!/usr/bin/env python
# coding: utf-8

# # Programming Assignmet 1

# ### 1.	Write a Python program to print "Hello Python"?

# In[1]:


print("Hello Python")


# ### 2.	Write a Python program to do arithmetical operations addition and division.?

# In[7]:


a = 10
b= 2
x = a+b
y = int(a/b)
print("Addition of a and b: ",x, " and a divided by b:",y)


# ### 3.	Write a Python program to find the area of a triangle?

# In[18]:


import math

x = int(input("Enter first side of the triangle: "))
y = int(input("Enter second side: "))
z = int(input("Enter third side: "))

s = (x+y+z)/2

area = math.sqrt((s*(s-x)*(s-y)*(s-z))) 
print(area)


# ### 4.	Write a Python program to swap two variables

# In[20]:


x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

x, y = y, x
print("x after swapping: ", x)
print("y after swapping: ", y)


# ### 5.	Write a Python program to generate a random number

# In[26]:


#Generating a random number between 0 and 100

import random

print(random.randint(0,100))

