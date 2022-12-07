# Individual Data Science Project
## Introduction
The purpose of this projecte is primarily a demonstration of my skill with Numpy, Pandas, and Seaborn using a real-life dataset example. Although, I was drawn to this partiuclar dataset because, as a resident of boston, I was curious as to what our cities crime looks like and what kind of enviroment I'm living in. The primary objectives I'm setting out to explore are what crime are committed, when do crime happen, and where are crime happening. The finding of this project will provide insigt into what the underbelly of Boston is like.

## Selection of Data
All model processing was done in PyCharm and can be found in what.py, when.py, where.py, and tools.py.

The data was sourced from [Kaggle](https://www.kaggle.com/datasets/AnalyzeBoston/crimes-in-boston) and contains three years of boston crime reports from Boston Police. There are a little under 320,000 total reports with 17 different properties: Incident Number, Offense Code, Offense Code Group, Offense Discritption, District, Reported Area, Shooting, Occurred on Date, Year, Month, Day of Week, Hour, UCR Part, Street, Lat, Long, and Location.

This Projects primarily objective is to find information on the what, when, and where of crimes in Boston. 

![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/dataset_picture.PNG)

It is of note that unfortunately the Shooting category is completely empty and thus was unable to be used. 

Going forward we will predominantly be focused on Offense Code Group, District, Reported Area, Occurred on Date, Year, Month, Day of Week, Hour, and UCR Part properties, as these propeties are the keys to finding the answer to the what, when, and where of crimes. So, the first step in the data munging process was to drop all remaining unused categories. Following that, the 'OCCURRED_ON_DATE' column was converted into pandas datetime values so that future date caculations would be easier. Then, another ease of life change was made by adding the 'UCR_PART' column value onto the 'OFFENSE_CODE_GROUP' to help differenciate between the same offense code group with two different UCR levels.. For example, the 'Other' offense code group had reports with a UCR of both 2 and 3 so it helped furthur differentiate them in the data. Finally, the last step preformed in the data processing phase was to drop any values in the 'UCR_PART' column that had 'Other' instead of a numerical level because there were so few of these reports, making up 0.386 percent of that data.

## Methods
Tools:
  * PyCharm as an IDE 
  * Numpy, Pandas, Seaborn, and Matplotlib for data manipluation and visualization
  * Github for hosting 

## Results


