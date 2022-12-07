# Individual Data Science Project
## Introduction
The purpose of this projecte is primarily a demonstration of my skill with Numpy, Pandas, and Seaborn using a real-life dataset example. Although, I was drawn to this partiuclar dataset because, as a resident of boston, I was curious as to what our cities crime looks like and what kind of enviroment I'm living in. The primary objectives I'm setting out to explore are what crime are committed, when do crime happen, and where are crime happening. The finding of this project will provide insigt into what the underbelly of Boston is like.

## Selection of Data
All model processing was done in PyCharm and can be found in what.py, when.py, where.py, and tools.py.

The data was sourced from [Kaggle](https://www.kaggle.com/datasets/AnalyzeBoston/crimes-in-boston) and contains three years of boston crime reports from Boston Police. There are a little under 320,000 total reports with 17 different properties: Incident Number, Offense Code, Offense Code Group, Offense Discritption, District, Reported Area, Shooting, Occurred on Date, Year, Month, Day of Week, Hour, UCR Part, Street, Lat, Long, and Location.

This Projects primarily objective is to find information on the what, when, and where of crimes in Boston. 

![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/dataset_picture.PNG)

It is important to note that UCR stands for Uniform Crime Reporting and represents a scale which crime can me measured on. More information can be found [here](https://ucr.fbi.gov/crime-in-the-u.s/2011/crime-in-the-u.s.-2011/offense-definitions), but essentially the worst of the crimes are categorized as Part 1 and decrease in severity as the part level increases to a maximum of 3. 

Going forward we will predominantly be focused on Offense Code Group, District, Reported Area, Occurred on Date, Year, Month, Day of Week, Hour, and UCR Part properties, as these propeties are the keys to finding the answer to the what, when, and where of crimes. So, the first step in the data munging process was to drop all remaining unused categories. Following that, the 'OCCURRED_ON_DATE' column was converted into pandas datetime values so that future date caculations would be easier. Then, another ease of life change was made by adding the 'UCR_PART' column value onto the 'OFFENSE_CODE_GROUP' to help differenciate between the same offense code group with two different UCR levels. For example, the 'Other' offense code group had reports with a UCR of both 2 and 3 so it helped furthur differentiate them in the data. Additionally, any values in the 'UCR_PART' column that had 'Other' instead of a numerical level was dropped because there were so few of these reports, making up 0.386 percent of that data. Finally, the last step was to replace all the police districts with the corresponding city district found on the [city of bostons website](https://www.boston.gov/departments/police). 

![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/data_munging_code.PNG)

## Methods
Tools:
  * PyCharm as an IDE 
  * Numpy, Pandas, Seaborn, and Matplotlib for data manipluation and visualization
  * Github for hosting 

## Results
What kinds of crimes are committed in boston?
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/AllReportedCrimesbyOffense.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/What_Top20CrimesOverTime.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/What_CrimesOverTime.png)




