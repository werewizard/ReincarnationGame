#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import Libraries
from os import system
import datetime
import time #Imports a module to add a pause


# In[2]:


#All choices
answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]
yes = ["Y", "y", "yes", "Yes"]
no = ["N", "n", "no", "No"]
#print(yes)


# In[3]:


#Clear Screen
def cls():
    system('cls')


# In[4]:


def CreatePrevLifeCharacter():
    #print(yes)
    name=input("What is your name? ")
    hair=input("What is your hair color? ")
    eyes=input("What is the color of your eyes? ")
    gender=input("Are you a girl? y/n ")
    if (gender in yes):
        gender = "girl"
    else:
        gender = "boy"
    return(name,hair,eyes,gender)


# In[5]:


def CreateNewLifeCharacter():
    name=input("What is your name? ")
    hair=input("What is your hair color? ")
    eyes=input("What is the color of your eyes? ")
    gender=input("Are you a girl? y/n ")
    if (gender in yes):
        gender = "girl"
    else:
        gender = "boy"
    return(name,hair,eyes,gender)


# In[6]:


def PreviousLifeOne(name, gender):
    if (gender=="girl"):
        pronoun1 = "her"
        pronoun2 = "she"
    else:
        pronoun1 = "his"
        pronoun2 = "he"
    print(name+" feels cold sweeping through "+pronoun1+" body. Left alone, in this deserted mountain, is this "+pronoun1+" end? "+pronoun2.capitalize()+" wishes "+pronoun2+" did everything different. Spent more time with people "+pronoun2+" loves. "+pronoun2.capitalize()+" felt her conscious fading into oblivion.")
   


# In[7]:


def InBetween(name, gender):
    if (gender=="girl"):
        pronoun1 = "her"
        pronoun2 = "she"
    else:
        pronoun1 = "his"
        pronoun2 = "he"
    print(name+" feels like "+pronoun2+" weighs nothing, like all "+pronoun2+" is, is a feather.")
    print("Time to create your character for new life!")


# In[8]:


def NewLifeOne(name, gender):
    if (gender=="girl"):
        pronoun1 = "her"
        pronoun2 = "she"
        Character1 = "young man"
        Character1pronoun = "his"
    else:
        pronoun1 = "his"
        pronoun2 = "he"
        Character1 = "young woman"
        Character1pronoun = "her"
        
    print(name+ " feels " +pronoun1+ " eyelids stirring. Instead of cold ice, " +pronoun2+ " feels " +pronoun1+ " body feeling warm. " +pronoun2.capitalize()+ " opens eyes to see a " +Character1+ " with worried look on " +Character1pronoun+ " face. \"Are you alright?\"  " )
    
     
    cls()
    
    print("You are going to make your first choice. Are you ready?")
    
    print("Press Enter, if you are ready, and if you aren't, maybe go grab some water.")
    
    cls()
    
    
    print("\"Are you alright?\" ")
    
    
    choice = input("Option A : Do I look alright to you?"
                   "Option B : Yeah."
                   "Option C : Where did the snow go?"
                   "Type A / B / C \n")
    
    
    
    
    


# In[9]:


required = ("\nUse only A, B, or C\n") #Cutting down on duplication


# In[10]:


#Game Title
gametitle = "I got reincarnated with only death flags in sight!"
system("mode 110,30")
system("title "+gametitle)


# In[11]:


#Defining Variables
DatePrevLife = datetime.datetime.now()
#print(DatePrevLife)
DateNewLife = datetime.datetime(793,1,1)
#print(DateNewLife)


# In[12]:


cls()
print("You got reincarnated, and got a chance to live again. Will you deflect all the death flags and have a pleasant life? Or will you die again?")


# In[13]:


cls()
PrevLifeName, PrevLifeHair, PrevLifeEyes, PrevLifeGender = CreatePrevLifeCharacter()
#print(PrevLifeName, PrevLifeHair, PrevLifeEyes, PrevLifeGender)
cls()

print("Your name is "+PrevLifeName+" and you have "+PrevLifeHair+" hair,  "+PrevLifeEyes+" eyes and you are a "+PrevLifeGender+"."  )
choice = input("Is this information correct? y/n ")
if (choice in yes):
    cls()
else:
    PrevLifeName, PrevLifeHair, PrevLifeEyes, PrevLifeGender = CreatePrevLifeCharacter()


# In[14]:


PreviousLifeOne(PrevLifeName, PrevLifeGender)


# In[15]:


cls()
InBetween(PrevLifeName, PrevLifeGender)


# In[16]:


cls()
NewLifeName, NewLifeHair, NewLifeEyes, NewLifeGender = CreateNewLifeCharacter()
cls()

print("Your name is "+NewLifeName+" and you have "+NewLifeHair+" hair,  "+NewLifeEyes+" eyes and you are a "+NewLifeGender+"."  )
choice = input("Is this information correct? y/n ")
if (choice in yes):
    cls()
else:
    NewLifeName, NewLifeHair, NewLifeEyes, NewLifeGender = CreateNewLifeCharacter()


# In[17]:


cls()
NewLifeOne(NewLifeName, NewLifeGender)


# In[ ]:


#All the variables defined till now 
##PrevLifeName
##PrevLifeHair
##PrevLifeEyes
##PrevLifeGender
##NewLifeName
##NewLifeHair
##NewLifeEyes
##NewLifeGender

#Choices
##answer_a
##answer_b
##answer_c
#yes
#no

#Extraas
##gametitle
##required

##DatePrevLife
##DateNewLife






#FunctionsDefined
##cls()
##CreatePrevLifeCharacter()
##CreateNewLifeCharacter()
##PrevLifeOne()
##NewLifeOne()

