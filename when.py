import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar
import tools




days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
total_weeks = float((pd.to_datetime(pd.to_datetime("2018-08", format='%Y-%m')) - pd.to_datetime(pd.to_datetime("2015-08", format='%Y-%m'))) / np.timedelta64(1, 'W'))
total_years = float((pd.to_datetime(pd.to_datetime("2018-08", format='%Y-%m')) - pd.to_datetime(pd.to_datetime("2015-08", format='%Y-%m'))) / np.timedelta64(1, 'Y'))
total_days = float((pd.to_datetime(pd.to_datetime("2018-08", format='%Y-%m')) - pd.to_datetime(pd.to_datetime("2015-08", format='%Y-%m'))) / np.timedelta64(1, 'D'))


# Cleaning
# Dropping not used columns. Reformatting dates, removing anything columns outside date range, and setting them to pandas dates.
data = pd.read_csv('crime.csv', encoding='windows-1254')
crime_data = tools.cleaner(data)



# data manipulation
# data for day of week



crime_by_dow = crime_data[['OFFENSE_CODE_GROUP', 'UCR_PART', 'DAY_OF_WEEK']]

all_crime_frequency_by_dow = crime_by_dow.groupby('DAY_OF_WEEK')['DAY_OF_WEEK'].count().div(total_weeks).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().set_index('DAY_OF_WEEK').reindex(days).reset_index()
p1_crime_frequency_by_dow = crime_by_dow[crime_by_dow['UCR_PART'] == 'Part One'].groupby('DAY_OF_WEEK')['DAY_OF_WEEK'].count().div(total_weeks).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().set_index('DAY_OF_WEEK').reindex(days).reset_index()
p2_crime_frequency_by_dow = crime_by_dow[crime_by_dow['UCR_PART'] == 'Part Two'].groupby('DAY_OF_WEEK')['DAY_OF_WEEK'].count().div(total_weeks).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().set_index('DAY_OF_WEEK').reindex(days).reset_index()
p3_crime_frequency_by_dow = crime_by_dow[crime_by_dow['UCR_PART'] == 'Part Three'].groupby('DAY_OF_WEEK')['DAY_OF_WEEK'].count().div(total_weeks).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().set_index('DAY_OF_WEEK').reindex(days).reset_index()


# data for months
crime_by_month = crime_data[['OFFENSE_CODE_GROUP', 'UCR_PART', 'MONTH']]

all_crime_frequency_by_month = crime_by_month.groupby('MONTH')['MONTH'].count().div(total_years).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['MONTH'])
p1_crime_frequency_by_month = crime_by_month[crime_by_dow['UCR_PART'] == 'Part One'].groupby('MONTH')['MONTH'].count().div(total_years).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['MONTH'])
p2_crime_frequency_by_month = crime_by_month[crime_by_dow['UCR_PART'] == 'Part Two'].groupby('MONTH')['MONTH'].count().div(total_years).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['MONTH'])
p3_crime_frequency_by_month = crime_by_month[crime_by_dow['UCR_PART'] == 'Part Three'].groupby('MONTH')['MONTH'].count().div(total_years).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['MONTH'])


# changing month to name
all_crime_frequency_by_month['MONTH'] = all_crime_frequency_by_month['MONTH'].apply(lambda x: calendar.month_abbr[x])
p1_crime_frequency_by_month['MONTH'] = p1_crime_frequency_by_month['MONTH'].apply(lambda x: calendar.month_abbr[x])
p2_crime_frequency_by_month['MONTH'] = p2_crime_frequency_by_month['MONTH'].apply(lambda x: calendar.month_abbr[x])
p3_crime_frequency_by_month['MONTH'] = p3_crime_frequency_by_month['MONTH'].apply(lambda x: calendar.month_abbr[x])


crime_by_hour = crime_data[['OFFENSE_CODE_GROUP', 'UCR_PART', 'HOUR']]
all_crime_frequency_by_hour = crime_by_hour.groupby('HOUR')['HOUR'].count().div(total_days).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['HOUR'])
p1_crime_frequency_by_hour = crime_by_hour[crime_by_dow['UCR_PART'] == 'Part One'].groupby('HOUR')['HOUR'].count().div(total_days).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['HOUR'])
p2_crime_frequency_by_hour = crime_by_hour[crime_by_dow['UCR_PART'] == 'Part Two'].groupby('HOUR')['HOUR'].count().div(total_days).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['HOUR'])
p3_crime_frequency_by_hour = crime_by_hour[crime_by_dow['UCR_PART'] == 'Part Three'].groupby('HOUR')['HOUR'].count().div(total_days).to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by=['HOUR'])





# plotting
sns.set_style("whitegrid")


month_datasets_info = {
    'x': 'MONTH',
    'y': 'FREQUENCY',
    'hue': None,
    'x_label': 'Month',
    'y_label': 'Number of Crimes',
}

month_titles = ['Average Number of All Crime By Month', 'Average Number of UCR-1 Crime By Month', 'Average Number of UCR-2 Crime By Month', 'Average Number of UCR-3 Crime By Month']
month_datasets = [all_crime_frequency_by_month, p1_crime_frequency_by_month, p2_crime_frequency_by_month, p3_crime_frequency_by_month]

fig1, ax1 = plt.subplots(nrows=2, ncols=2, figsize=(20, 7))
fig1.subplots_adjust(hspace=.4, wspace=.2)
for row in range(2):
    for col in range(2):
        p = sns.lineplot(ax=ax1[row, col], x=month_datasets_info['x'], y=month_datasets_info['y'], hue=month_datasets_info['hue'], data=month_datasets[col + (row * 2)])
        p.set(xlabel=month_datasets_info['x_label'], ylabel=month_datasets_info['y_label'], title=month_titles[col + (row * 2)])
        ax1[row, col].xaxis.labelpad = 10


dow_datasets_info = {
    'x': 'DAY_OF_WEEK',
    'y': 'FREQUENCY',
    'hue': None,
    'x_label': 'Day',
    'y_label': 'Number of Crimes',
}

dow_titles = ['Average Number of All Crime By Day of The Week', 'Average Number of URC-1 Crime By Day of The Week', 'Average Number of UCR-2 Crime By Day of The Week', 'Average Number of UCR-3 Crime By Day of The Week']
dow_datasets = [all_crime_frequency_by_dow, p1_crime_frequency_by_dow, p2_crime_frequency_by_dow, p3_crime_frequency_by_dow]
fig2, ax2 = plt.subplots(nrows=2, ncols=2, figsize=(20, 7))
fig2.subplots_adjust(hspace=.4, wspace=.2)
for row in range(2):
    for col in range(2):
        p = sns.lineplot(ax=ax2[row, col], x=dow_datasets_info['x'], y=dow_datasets_info['y'], hue=dow_datasets_info['hue'], data=dow_datasets[col + (row * 2)])
        p.set(xlabel=dow_datasets_info['x_label'], ylabel=dow_datasets_info['y_label'], title=dow_titles[col + (row * 2)])
        ax2[row, col].xaxis.labelpad = 10




month_datasets_info = {
    'x': 'HOUR',
    'y': 'FREQUENCY',
    'hue': None,
    'x_label': 'Hour',
    'y_label': 'Number of Crimes',
}

month_titles = ['Average Number of All Crime By Hour', 'Average Number of UCR-1 Crime By Hour', 'Average Number of UCR-2 Crime By Hour', 'Average Number of UCR-3 Crime By Hour']
month_datasets = [all_crime_frequency_by_hour, p1_crime_frequency_by_hour, p2_crime_frequency_by_hour, p3_crime_frequency_by_hour]

fig3, ax3 = plt.subplots(nrows=2, ncols=2, figsize=(20, 7))
fig3.subplots_adjust(hspace=.4, wspace=.2)
for row in range(2):
    for col in range(2):
        p = sns.barplot(ax=ax3[row, col], x=month_datasets_info['x'], y=month_datasets_info['y'], hue=month_datasets_info['hue'], data=month_datasets[col + (row * 2)])
        p.set(xlabel=month_datasets_info['x_label'], ylabel=month_datasets_info['y_label'], title=month_titles[col + (row * 2)])
        ax3[row, col].xaxis.labelpad = 10



plt.rc("savefig", dpi=300)
plt.rcParams['figure.dpi']= 300

fig1.savefig("When_AverageNumberofAllCrimeByMonth.png")
fig2.savefig("When_AverageNumberofCrimeByDayofTheWeek.png")
fig3.savefig("When_AverageNumberofAllCrimeByHour.png")


plt.show()