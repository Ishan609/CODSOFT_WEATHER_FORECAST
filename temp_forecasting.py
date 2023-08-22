#!/usr/bin/env python
# coding: utf-8

# In[4]:


from  tkinter import *
from tkinter import ttk

import requests 


# In[5]:


def data_get():
    city_name=city.get()
    data=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=8bf1bc79c597a08ee76ea64accdc7109").json()
    
    current_temp2.config(text=str(int(data["main"]["temp"]-273.15)))
    temp_min2.config(text=str(int(data["main"]["temp_min"]-273.15)))
    temp_max2.config(text=str(int(data["main"]["temp_max"]-273.15)))
    climate_label2.config(text=data["weather"][0]["main"])



# In[6]:


win=Tk()
win.title("Weather Forecasting App")


# In[7]:


win.geometry("600x600")
win.configure(bg="grey")


# In[8]:


name_label=Label(win,text="WEATHER REPORT",font=("Time New Roman",40,"bold"))
name_label.place(x=30,y=25,height=70,width=540)


# In[9]:


city=StringVar()
city_list=["Andhra Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

     


# In[10]:


combo_box=ttk.Combobox(win,text="select the name ",values=city_list,font=("Time New Roman",20),textvariable=city)
combo_box.place(x=60,y=130,height=35,width=480)


# In[11]:


climate_label=Label(win,text="WEATHER TYPE",bg="grey",font=("Time New Roman",15))
climate_label.place(x=45,y=340,height=30,width=250)
climate_label1=Label(win,text="--->",bg="grey",font=("Time New Roman",10))
climate_label1.place(x=310,y=340,height=30,width=18)
climate_label2=Label(win,text=" ",bg="grey",font=("Time New Roman",15))
climate_label2.place(x=335,y=340,height=30,width=100)


# In[12]:


current_temp=Label(win,text="CURRENT TEMPERATURE",bg="grey",font=("Time New Roman",15))
current_temp.place(x=45,y=400,height=30,width=250)
current_temp1=Label(win,text="--->",bg="grey",font=("Time New Roman",10))
current_temp1.place(x=310,y=400,height=30,width=18)
current_temp2=Label(win,text="",bg="grey",font=("Time New Roman",15))
current_temp2.place(x=335,y=400,height=30,width=100)


# In[13]:


temp_min=Label(win,text="MINIMUM TEMPERATURE",bg="grey",font=("Time New Roman",15))
temp_min.place(x=45,y=460,height=30,width=250)
temp_min1=Label(win,text="--->",bg="grey",font=("Time New Roman",10))
temp_min1.place(x=310,y=460,height=30,width=18)
temp_min2=Label(win,text="",bg="grey",font=("Time New Roman",15))
temp_min2.place(x=335,y=460,height=30,width=100)


# In[14]:


temp_max=Label(win,text="MAXIMUM TEMPERATURE",bg="grey",font=("Time New Roman",15))
temp_max.place(x=45,y=520,height=30,width=250)
temp_max1=Label(win,text="--->",bg="grey",font=("Time New Roman",10))
temp_max1.place(x=310,y=520,height=30,width=18)

temp_max2=Label(win,text="",bg="grey",font=("Time New Roman",15))
temp_max2.place(x=335,y=520,height=30,width=100)


# In[15]:


button=Button(win,text="DONE",font=("Time New Roman",30,"bold"),command=data_get)
button.place(x=200,y=200,height=60,width=200)


# In[16]:


win.mainloop()


# In[ ]:




