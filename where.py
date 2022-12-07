import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as md
import tools
import matplotlib as mpl


# Cleaning
# Dropping not used columns. Reformatting dates, removing anything columns outside date range, and setting them to pandas dates.
data = pd.read_csv('crime.csv', encoding='windows-1254')
crime_data = tools.cleaner(data)

all_crime_by_street_over_time = crime_data[['OCCURRED_ON_DATE', 'STREET', 'UCR_PART']]

# data manipulation
# crime by district
all_crime_by_district_over_time = crime_data[['OCCURRED_ON_DATE', 'DISTRICT', 'UCR_PART']]

all_crime_by_district_over_time = all_crime_by_district_over_time.groupby(['OCCURRED_ON_DATE', 'DISTRICT', 'UCR_PART']).value_counts().to_frame().reset_index().set_axis(['OCCURRED_ON_DATE', 'DISTRICT', 'UCR_PART', 'FREQUENCY'], axis=1)
ucr1_crime_by_district_over_time = all_crime_by_district_over_time[all_crime_by_district_over_time['UCR_PART'] == 'Part One'].sort_values(by='DISTRICT')
ucr2_crime_by_district_over_time = all_crime_by_district_over_time[all_crime_by_district_over_time['UCR_PART'] == 'Part Two'].sort_values(by='DISTRICT')
ucr3_crime_by_district_over_time = all_crime_by_district_over_time[all_crime_by_district_over_time['UCR_PART'] == 'Part Three'].sort_values(by='DISTRICT')

# crime by street
all_crime_by_street_over_time = crime_data[['STREET', 'DISTRICT', 'UCR_PART']].dropna()

all_crime_by_street_over_time = all_crime_by_street_over_time.groupby(['STREET', 'DISTRICT', 'UCR_PART']).value_counts().to_frame().reset_index().set_axis(['STREET', 'DISTRICT', 'UCR_PART', 'FREQUENCY'], axis=1).sort_values(by='FREQUENCY', ascending=False)[:20]
all_crime_by_street_over_time_2 = all_crime_by_street_over_time.reset_index().drop(columns=['UCR_PART']).groupby(['STREET', 'DISTRICT'])['FREQUENCY'].sum().to_frame().sort_values(by='FREQUENCY', ascending=False).reset_index()
ucr1_crime_by_street_over_time = all_crime_by_street_over_time[all_crime_by_street_over_time['UCR_PART'] == 'Part One'].sort_values(by='FREQUENCY', ascending=False)
ucr2_crime_by_street_over_time = all_crime_by_street_over_time[all_crime_by_street_over_time['UCR_PART'] == 'Part Two'].sort_values(by='FREQUENCY', ascending=False)
ucr3_crime_by_street_over_time = all_crime_by_street_over_time[all_crime_by_street_over_time['UCR_PART'] == 'Part Three'].sort_values(by='FREQUENCY', ascending=False)
print(all_crime_by_street_over_time_2)

# plotting
sns.set_style("whitegrid")

datasets_info = {
    'x': 'OCCURRED_ON_DATE',
    'y': 'FREQUENCY',
    'hue': 'DISTRICT',
    'style': None,
    'x_label': 'Date (Month)',
    'y_label': 'Number of Crimes',
}
datasets = [ucr1_crime_by_district_over_time, ucr2_crime_by_district_over_time, ucr3_crime_by_district_over_time]
titles = ['UCR1 Crimes by District', 'UCR2 Crimes by District', 'UCR3 Crimes by District']

# district p1
fig1, ax1 = plt.subplots(ncols=3, figsize=(21, 7))
fig1.subplots_adjust(hspace=.4, wspace=.2)
legend1 = False
for i in range(3):
    if i == 2: legend1 = True
    p = sns.lineplot(ax=ax1[i], x=datasets_info['x'], y=datasets_info['y'], hue=datasets_info['hue'], style=datasets_info['style'], data=datasets[i], legend=legend1)
    p.set(xlabel=datasets_info['x_label'], ylabel=datasets_info['y_label'], title=titles[i])
    ax1[i].tick_params(axis='x', rotation=45)
    ax1[i].xaxis.labelpad = 10



ax1[2].legend(ncol=6, bbox_to_anchor=(-1.8, 1.15), loc='upper left', borderaxespad=0, frameon=False)
fig1.subplots_adjust(right=0.975, left=.05, bottom=.15)

# District p2
fig2, ax2 = plt.subplots(figsize=(20, 7))
fig2.subplots_adjust(hspace=.4, wspace=-.8)

p1 = sns.lineplot(ax=ax2, x='OCCURRED_ON_DATE', y='FREQUENCY', hue='DISTRICT', style='UCR_PART', data=all_crime_by_district_over_time)
p1.set(xlabel='Date (Month)', ylabel='Number of Crimes', title='All Crimes by District')

ax2.legend(bbox_to_anchor=(1.18, 1), loc='upper right', borderaxespad=0)
fig2.subplots_adjust(right=0.84, left=.05)


# streets p1
datasets_info = {
    'x': 'STREET',
    'y': 'FREQUENCY',
    'hue': 'DISTRICT',
    'style': None,
    'x_label': 'Street Names',
    'y_label': 'Number of Crimes',
}
datasets = [ucr1_crime_by_street_over_time, ucr2_crime_by_street_over_time, ucr3_crime_by_street_over_time]
titles = ['UCR1 Crimes by Street', 'UCR2 Crimes by Street', 'UCR3 Crimes by Street']


fig3, ax3 = plt.subplots(ncols=3, figsize=(21, 7))
fig3.subplots_adjust(hspace=.4, wspace=.2)
legend1 = False
for i in range(3):

    p = sns.barplot(ax=ax3[i], x=datasets_info['x'], y=datasets_info['y'], hue=datasets_info['hue'], data=datasets[i], dodge=False)
    p.set(xlabel=datasets_info['x_label'], ylabel=datasets_info['y_label'], title=titles[i])
    ax3[i].tick_params(axis='x', rotation=45)
    ax3[i].xaxis.labelpad = 10


#ax3[2].legend(ncol=6, bbox_to_anchor=(-1.8, 1.15), loc='upper left', borderaxespad=0, frameon=False)
fig3.subplots_adjust(right=0.975, left=.05, bottom=.15)



# street p2
fig4, ax4 = plt.subplots(figsize=(20, 7))
fig4.subplots_adjust(hspace=.4, wspace=-.8)

p1 = sns.barplot(ax=ax4, x='STREET', y='FREQUENCY', hue='DISTRICT', data=all_crime_by_street_over_time_2, dodge=False)
p1.set(xlabel='Street Names', ylabel='Number of Crimes', title='All Crimes by Street')
ax4.tick_params(axis='x', rotation=45)
ax4.legend(bbox_to_anchor=(1.18, 1), loc='upper right', borderaxespad=0)
fig4.subplots_adjust(right=0.84, left=.05)



plt.rc("savefig", dpi=300)
plt.rcParams['figure.dpi']= 300

fig1.savefig("Where_AllCrimesbyDistrict.png")
fig2.savefig("Where_URCCrimesbyDistrict.png")
fig3.savefig("Where_AllCrimesbyStreet.png")
fig4.savefig("Where_URCCrimesbyStreet.png")

plt.show()