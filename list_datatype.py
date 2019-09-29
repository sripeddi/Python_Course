#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Introduction to list datatypes
#List is collection of particular items in order. 
#It is muttable type(which means you can change)
#Define a list

bicycles = ['range','hero','redline']
print(bicycles)


# In[2]:


#how to access elements in list and maintain a proper formatting
print(bicycles[0].title())


# In[3]:


print(bicycles[1].title())


# In[12]:


bicycles = ['ranger','hero','redline']

message = f"My first Bicycle was a {bicycles[1].title()}"

print(message)


# In[14]:


#Modify elements in list

students =['sri','divya','neha']
print(students)


# In[15]:


#change the element sri to shree
students[0]= 'shree'
print(students)


# In[22]:


#adding element to the list
students = ['sri','divya','navya','neha']
students.append('kavya')
print (students)


# In[23]:


#insert kavya between sri and divya
students.insert(1,'kavya')
print(students)


# In[24]:


del students[2]
print(students)


# In[25]:


poped_students = students.pop()
print(poped_students)


# In[30]:


students.append('test')
print(students)


# In[34]:


del students[5]
print(students)


# In[36]:


poped_students =students.pop()
print(poped_students)


# In[ ]:




