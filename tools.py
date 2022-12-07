import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md

districts = {'A1': 'Downtown & Charlestown', 'A15': 'Downtown & Charlestown', 'A7': 'East Boston', 'B2': 'Roxbury', 'B3': 'Mattapan',
             'C6': 'South Boston', 'D4':'South End', 'C11': 'Dorchester', 'D14': 'Brighton', 'E5': 'West Roxbury',
             'E13': 'Jamaica Plain', 'E18':'Hyde Park'}


def cleaner(data):
    crime_data = data.drop(['SHOOTING', 'Lat', 'Long', 'Location'], axis=1).dropna().sort_values(by=['OCCURRED_ON_DATE'])
    crime_data['OCCURRED_ON_DATE'] = crime_data['OCCURRED_ON_DATE'].str.split(" ").str[0].str[0:-3]
    crime_data = crime_data[(crime_data['OCCURRED_ON_DATE'] >= "2015-08") & (crime_data['OCCURRED_ON_DATE'] <= "2018-08")]
    crime_data['OCCURRED_ON_DATE'] = pd.to_datetime(crime_data['OCCURRED_ON_DATE'], format='%Y-%m')
    crime_data.loc[crime_data['UCR_PART'] == 'Part Three', 'OFFENSE_CODE_GROUP'] += ' (UCR-3)'
    crime_data.loc[crime_data['UCR_PART'] == 'Part Two', 'OFFENSE_CODE_GROUP'] += ' (UCR-2)'
    crime_data.loc[crime_data['UCR_PART'] == 'Part One', 'OFFENSE_CODE_GROUP'] += ' (UCR-1)'
    crime_data = crime_data[(crime_data['UCR_PART'] != 'Other')]
    region = pd.DataFrame.from_dict(districts, orient='index').reset_index().set_axis(['DISTRICT', 'REGION'], axis=1).set_index('DISTRICT')
    crime_data = crime_data.set_index('DISTRICT').merge(region, left_index=True, right_index=True).reset_index(drop=True).rename(columns={"REGION": "DISTRICT"})

    return crime_data


def set_dates(row_num, col_num, ax):
    for row in range(row_num):
        if (row_num == 1 and col_num == 0) or row_num > 1:
            for col in range(col_num):
                ax[col, row].xaxis.set_major_locator(md.MonthLocator(interval=6))
                ax[col, row].xaxis.set_major_formatter(md.DateFormatter('%Y-%m'))
                plt.setp(ax[col, row].xaxis.get_majorticklabels(), rotation=0)
                ax[col, row].xaxis.set_minor_locator(md.MonthLocator(interval=1))
                ax[col, row].tick_params(axis='x', which='major', length=10)
                ax[col, row].tick_params(axis='x', which='minor', length=5)

