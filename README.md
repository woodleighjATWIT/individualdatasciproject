# Individual Data Science Project
## Introduction
The purpose of this projecte is primarily a demonstration of my skill with Numpy, Pandas, and Seaborn using a real-life dataset example. Although, I was drawn to this partiuclar dataset because, as a resident of boston, I was curious as to what our cities crime looks like and what kind of enviroment I'm living in. The primary objectives I'm setting out to explore are what crime are committed, when do crime happen, and where are crime happening. The finding of this project will provide insigt into what the underbelly of Boston is like.

## Selection of Data
All model processing was done in PyCharm and can be found in what.py, when.py, where.py, and tools.py.

The data was sourced from [Kaggle](https://www.kaggle.com/datasets/AnalyzeBoston/crimes-in-boston) and contains three years of boston crime reports from Boston Police. There are a little under 320,000 total reports with 17 different properties: Incident Number, Offense Code, Offense Code Group, Offense Discritption, District, Reported Area, Shooting, Occurred on Date, Year, Month, Day of Week, Hour, UCR Part, Street, Lat, Long, and Location.

This Projects primarily objective is to find information on the what, when, and where of crimes in Boston. 

![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/dataset_picture.PNG)

It is of note that unfortunately the Shooting category is completely empty and thus was unable to be used. 

Going forward we will predominantly be focused on Offense Code Group, District, Reported Area, Occurred on Date, Year, Month, Day of Week, Hour, and UCR Part properties, as these propeties are the keys to finding the answer to the what, when, and where of crimes.

## Methods
Tools:
  * PyCharm as an IDE 
  * Numpy, Pandas, Seaborn, and Matplotlib for data manipluation and visualization
  * Github for hosting 



