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
Using the graphical representations provided, it is possible to answers a broad number of possible questions, including the questions this project set out to find the answers to.

### [What](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/what.py) kinds of crimes are committed in boston?
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/AllReportedCrimesbyOffense.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/What_Top20CrimesOverTime.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/What_CrimesOverTime.png)

The answer to the first question, 'what kind of crimes are being committed in boston?', is that there are many crimes being committed but there are a few that really stand out. Firstly, motor vehicle accidents are the number one most reported crime. This makes sense in Boston with its notoriously difficult and confusing roads. Its also of note that larceny is the most popular UCR Part 1 crime, even coming in third overall, while homicide is distinctly not present. There was only a total of 161 homicides reported, making up 0.05 percent of crime reports. So, although theres a larceny is popular, the odds of getting killed in boston are extremely low.


### [When](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/when.py) are crimes committed in boston?
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/When_AverageNumberofAllCrimeByMonth.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/When_AverageNumberofCrimeByDayofTheWeek.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/When_AverageNumberofAllCrimeByHour.png)

The results for the second question, 'when are crimes being committed in boston?', were largely conclusive. Crime is relatively stagnent throughout the year expect for a small decline around the new year and a sharp all around the board increase in August. The sharp spike could potietnally be related to an increase in new people from all the new college freshman moving onto campus. Crime also experienced an uptick on Fridays and fell below normal levels for the rest of the weekend. Finally, we saw crime peak around 6pm during rush hour and slowly start to decrease as night falls and morning comes around.

To truly explore if the widely accepted belief that nightime is the most dangerous time of day, future research could be done exploring the relation between amount of crimes committed and number of people out and about. 


### [Where](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/where.py) are most crimes committed in boston?
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/Where_AllCrimesbyDistrict.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/Where_URCCrimesbyDistrict.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/Where_URCCrimesbyStreet_3.png)
![](https://github.com/woodleighjATWIT/individualdatasciproject/blob/main/Where_AllCrimesbyStreet_3.png)

To help answer the last question, 'where are most crime committed in boston?', we can break down the police reports be district and street. Looking at the break down of crime by district there are immedietntly a few candidetes for most dangerous district that stand out. However, it is important to note that some districts see a higher traffic of people entering a leaving, which is bound to lead to an increase in crime. Roxbury and Dorchester are immeditately obvious pick for the districts with highest overall crime, along with UCR part 2 and 3 crimes. Interestingly though, the district with the highest level of UCR part 1 crime is the south end. This likely means that if you were looking for a place to get robbed, the South End is the best place. 

To find the street with the highest level of crime is a little more difficult since the length of the street could correlate with an increase in crimes since there is more area covered. This could be a potiential point of future research, but for this project, it wont be considered.




## Discussion


## Summary


## References

