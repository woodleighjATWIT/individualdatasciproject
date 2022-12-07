import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import tools

data = pd.read_csv('crime.csv', encoding='windows-1254')

# cleaning
crime_data = tools.cleaner(data)
crime_data.loc[crime_data['UCR_PART'] == 'Part One', 'UCR_PART'] = 'Part 1'
crime_data.loc[crime_data['UCR_PART'] == 'Part Two', 'UCR_PART'] = 'Part 2'
crime_data.loc[crime_data['UCR_PART'] == 'Part Three', 'UCR_PART'] = 'Part 3'


# data manipulation
all_crime_data_by_crime = crime_data.groupby(['OFFENSE_CODE_GROUP', 'UCR_PART'])['OFFENSE_CODE_GROUP'].count().to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by='FREQUENCY', ascending=False).sort_values(by='FREQUENCY', ascending=False)

# finding top 20 categories
all_top20_crime = crime_data.groupby(['OFFENSE_CODE_GROUP'])['OFFENSE_CODE_GROUP'].count().to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by='FREQUENCY', ascending=False)[:20].set_index(['OFFENSE_CODE_GROUP']).drop(columns=['FREQUENCY'])
ucr1_top20_crime = crime_data[crime_data['UCR_PART'] == 'Part 1'].groupby(['OFFENSE_CODE_GROUP'])['OFFENSE_CODE_GROUP'].count().to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by='FREQUENCY', ascending=False)[:10].set_index(['OFFENSE_CODE_GROUP']).drop(columns=['FREQUENCY'])
ucr2_top20_crime = crime_data[crime_data['UCR_PART'] == 'Part 2'].groupby(['OFFENSE_CODE_GROUP'])['OFFENSE_CODE_GROUP'].count().to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by='FREQUENCY', ascending=False)[:10].set_index(['OFFENSE_CODE_GROUP']).drop(columns=['FREQUENCY'])
ucr3_top20_crime = crime_data[crime_data['UCR_PART'] == 'Part 3'].groupby(['OFFENSE_CODE_GROUP'])['OFFENSE_CODE_GROUP'].count().to_frame().set_axis(['FREQUENCY'], axis=1).reset_index().sort_values(by='FREQUENCY', ascending=False)[:10].set_index(['OFFENSE_CODE_GROUP']).drop(columns=['FREQUENCY'])


# finding crime over time
crime_by_offense_over_time = crime_data[['OCCURRED_ON_DATE', 'OFFENSE_CODE_GROUP', 'UCR_PART']]
crime_by_offense_over_time = crime_by_offense_over_time.groupby(['OCCURRED_ON_DATE', 'OFFENSE_CODE_GROUP', 'UCR_PART']).value_counts().to_frame().reset_index().set_axis(['OCCURRED_ON_DATE', 'OFFENSE_CODE_GROUP', 'UCR_PART', 'FREQUENCY'], axis=1)
crime_by_offense_over_time = crime_by_offense_over_time.sort_values(by=['OCCURRED_ON_DATE']).set_index(['OFFENSE_CODE_GROUP'])


# measuring top 20 over time
all_top20_crime_over_time = all_top20_crime.merge(crime_by_offense_over_time, left_index=True, right_index=True).reset_index().sort_values(by=['FREQUENCY', 'UCR_PART'], ascending=False)
urc1_top20_crime_over_time = ucr1_top20_crime.merge(crime_by_offense_over_time, left_index=True, right_index=True).reset_index().sort_values(by=['FREQUENCY', 'UCR_PART'], ascending=False)
urc2_top20_crime_over_time = ucr2_top20_crime.merge(crime_by_offense_over_time, left_index=True, right_index=True).reset_index().sort_values(by=['FREQUENCY', 'UCR_PART'], ascending=False)
urc3_top20_crime_over_time = ucr3_top20_crime.merge(crime_by_offense_over_time, left_index=True, right_index=True).reset_index().sort_values(by=['FREQUENCY', 'UCR_PART'], ascending=False)




# plotting
sns.set_style("whitegrid")
datasets_info = {
    'x': 'OCCURRED_ON_DATE',
    'y': 'FREQUENCY',
    'hue': 'OFFENSE_CODE_GROUP',
    'style': None,
    'x_label': 'Date (Month)',
    'y_label': 'Number of Crimes',
}
datasets = [urc1_top20_crime_over_time, urc2_top20_crime_over_time, urc3_top20_crime_over_time]
titles = ['Top UCR1 Crimes Over Time', 'Top 10 UCR2 Crimes Over Time', 'Top 10 UCR3 Crimes Over Time']


# line plots of crimes by UCR
fig1, ax1 = plt.subplots(ncols=3, figsize=(21, 7))
fig1.subplots_adjust(hspace=.4, wspace=.2)
for i in range(3):
    p = sns.lineplot(ax=ax1[i], x=datasets_info['x'], y=datasets_info['y'], hue=datasets_info['hue'], style=datasets_info['style'], data=datasets[i])
    p.set(xlabel=datasets_info['x_label'], ylabel=datasets_info['y_label'], title=titles[i])
    ax1[i].tick_params(axis='x', rotation=45)
    ax1[i].xaxis.labelpad = 10
    ax1[i].legend(loc='upper center', bbox_to_anchor=(.5, -.25))


fig1.subplots_adjust(right=0.975, left=.05, bottom=.45, top=.95)


# top 20 crimes line plot
fig2, ax = plt.subplots(figsize=(14, 7))
fig2.subplots_adjust(hspace=.4, wspace=.2)

p1 = sns.lineplot(ax=ax, x='OCCURRED_ON_DATE', y='FREQUENCY', hue='OFFENSE_CODE_GROUP', style='UCR_PART', data=all_top20_crime_over_time)
p1.set(xlabel='Date (Month)', ylabel='Number of Crimes', title='Top 20 Crimes Over Time')
ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1))
fig2.subplots_adjust(right=0.72, left=.075)


# bar graph of all crimes by offense
fig3, ax = plt.subplots(figsize=(14, 7))
fig3.subplots_adjust(hspace=.4, wspace=.2)

p2 = sns.barplot(ax=ax, x='OFFENSE_CODE_GROUP', y='FREQUENCY', hue='UCR_PART', data=all_crime_data_by_crime, dodge=False)
p2.set(xlabel='Crimes', ylabel='Number of Reports', title='All Reported Crimes by Offense')
ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1))
ax.tick_params(axis='x', rotation=90)
fig3.subplots_adjust(right=0.9, left=0.09, bottom=.5, top=.95)

plt.rc("savefig", dpi=300)
plt.rcParams['figure.dpi'] = 300
#fig1.savefig("CrimesOverTime.png")
#fig2.savefig("Top20CrimesOverTime.png")
fig3.savefig("AllReportedCrimesbyOffense.png")


plt.show()






