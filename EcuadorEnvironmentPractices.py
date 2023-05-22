# -*- coding: utf-8 -*-
"""
Created on Wed May 10 16:17:39 2023

@author: Maria del Carmen Pantoja
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

## Information from Environmental Information in Households in Ecuador:
#CSV files from: https://www.ecuadorencifras.gob.ec/hogares/ 
#Open the databases in CSV of the five years of analysis (2015 - 2022)
#2022 the survey is recolected in two phases with diferent questions and houlseholds

csv_files = [
    'ambiente_2015.csv', 
    'ambiente_2016.csv',
    'ambiente_2017.csv', 
    'ambiente_2018.csv', 
    'ambiente_2019.csv', 
    'ambiente_2022_08.csv',
    'ambiente_2022_10.csv']

#PREPARE THE DATABASES

#Read the Province f (Level of Territory as County) and change to string type
provinces = pd.read_excel('provinces.xlsx')
provinces['ID_1'] = provinces['ID_1'].astype(str)

#Separate first one o two numbers in the city code to identify the Province and match it with the name
for file in csv_files:
    data = pd.read_csv(file)
    data['ciudad'] = data['ciudad'].astype(str)
    conditions = [data['ciudad'].str.len() == 5, data['ciudad'].str.len() == 6]
    provcode = [data['ciudad'].str[0], data['ciudad'].str[:2]] 

# Merge the data based on the "NEW_VARIABLE" for code of provinces in order to match "ID_1"
# After merging rename with province names
    data['NEW_VARIABLE'] = pd.np.select(conditions, provcode, default=None)
    merged_data = pd.merge(data, provinces[['ID_1', 'NAME_1']], left_on='NEW_VARIABLE', right_on='ID_1', how='left')
    merged_data.rename(columns={'NAMEP': 'PROVINCE_NAME'}, inplace=True)
    
# Save the new files _including the province as a variable and open the files
output_file = file.replace('.csv', '_Prov.csv')
merged_data.to_csv(output_file, index=False)

environmentEC_2015 = pd.read_csv('ambiente_2015_Prov.csv')
environmentEC_2016 = pd.read_csv('ambiente_2016_Prov.csv')
environmentEC_2017 = pd.read_csv('ambiente_2017_Prov.csv')
environmentEC_2018 = pd.read_csv('ambiente_2018_Prov.csv')
environmentEC_2019 = pd.read_csv('ambiente_2019_Prov.csv')
environmentEC_2022_08 = pd.read_csv('ambiente_2022_08_Prov.csv')
environmentEC_2022_10 = pd.read_csv('ambiente_2022_10_Prov.csv')


#Unifying the names of the columns according to the questions for the topics of analysis:
#Unify the factor of expansion in the dataframe

#Chart to rename variables according to 2022_08 

#QUESTION 1
#What environmental problems affect neighborhoods?:                                                                         2015    2016    2017   2018     2019    2022_08 2022_10
#s101p121 What are those that affect your neighborhood: Visual pollution: Advertising, billboards, cables, antennas, poles? A1701   A1701   A1001  x        x       x       s91p91
#s101p122 What are those that affect your neighborhood: Contaminated water?                                                 A1702   A1702   A1002  x        x       x       s91p92
#s101p123 What are those that affect your neighborhood: Excessive noise?                                                    A1703   A1703   A1003  x        x       x       s91p93
#s101p124 What are those that affect your neighborhood: Garbage Accumulation?                                               A1704   A1704   A1004  x        x       x       s91p94
#s101p125 What are those that affect your neighborhood: Air pollution (smog                                                 A1705   A1705   A1005  x        x       x       s91p95

#QUESTION 2
#Households that sorted or separated some type of waste:                            2015    2016    2017  2018 2019 2022_08 
#s101p11  SORTED during the LAST 12 MONTHS waste:  Organic                          A0301   A0301   A01     x    x    x
#s101p12a SORTED during the LAST 12 MONTHS waste: Inorganic: Paper, cardboard       A0302A  A0302A  A0102A  x    x    x
#s101p12b SORTED during the LAST 12 MONTHS waste: Inorganic: Plastic                A0302B  A0302B  A0102B  x    x    x
#s101p12c SORTED during the LAST 12 MONTHS waste: Inorganic: Glass                  A0302C  A0302C  A0102C  x    x    x

#QUESTION 3
#Water use practices carried out by households.                                                            2015   2016  2017  2018 2019 2022_08
#s101p61 Usually: They reuse water                                                                         A1001  a1001 A0601   x   x    x
#s101p62 Usually: They use a bucket instead of a hose for certain activities                               A1002  a1002 A0602   x   x    x
#s101p63 Usually: They turn off the faucets while soaping the dishes, bathing, brushing their teeth, etc.  A1003  a1003 A0603   x   x    x
#s101p64 Usually: They shower in less than 10 minutes                                                      NO     a1004 A0604   x   x    x
#s101p65 Usually: They regularly check the pipes                                                           A1004  a1005 A0605   x   x    x
#s101p66 Usually: They have jet economizers                                                                A1005  a1006 A0606   x   x    x
#s101p67 Usually: They have a double flush toilet                                                          A1006  a1007 A0607   x   x    x
#s101p68 Usually:Place a bottle of water or other object inside the toilet tank                            A1007  a1008 A0608   x   x    x

#QUESTION 4
#How do Ecuadorian households save energy?                                         2015  2016  2017  2018 2019 2022_08 
#s101p71 Disconnect electronic devices and appliances when not in use              A1201 a1201 A0701  x    x    x 
#s101p72 They turn off the lights when leaving a room                              A1202 a1202 A0702  x    x    x 
#s101p73 Put hot food in the refrigerator                                          A1203 a1203 A0703  x    x    x 
#s101p74 They iron as much laundry as possible in one go                           A1204 a1204 A0704  x    x    x 
#s101p75 They open the curtains and blinds to take advantage of the sunlight       A1205 a1205 A0705  x    x    x 
#s101p76 Has energy-saving household appliances                                    A1206 a1206 A0706  x    x    x 
#s101p77 It has solar panels                                                       A1207 a1207 A0707  x    x    x 

column_change = {
  'A1701': 's101p121',
  'A1702': 's101p122',
  'A1703': 's101p123',
  'A1704': 's101p124',
  'A1705': 's101p125',
  'A0301': 's101p11',
  'A0302A': 's101p12a',
  'A0302B': 's101p12b',
  'A0302C': 's101p12c',
  'A1001': 's101p61',
  'A1002': 's101p62',
  'A1003': 's101p63',
  'A1004': 's101p65',
  'A1005': 's101p66',
  'A1006': 's101p67',
  'A1007': 's101p68',
  'A1201': 's101p71',
  'A1202': 's101p72',
  'A1203': 's101p73',
  'A1204': 's101p74',
  'A1205': 's101p75',
  'A1206': 's101p76',
  'A1207': 's101p77'}
#Water use practices carried out by households does not include s101p64 in the survey
environmentEC_2015 = environmentEC_2015.rename(columns=column_change)
environmentEC_2015['s101p64'] = None

column_change2 = {
  'a1701': 's101p121',
  'a1702': 's101p122',
  'a1703': 's101p123',
  'a1704': 's101p124',
  'a1705': 's101p125',
  'a0301': 's101p11',
  'a0302a': 's101p12a',
  'a0302b': 's101p12b',
  'a0302c': 's101p12c',
  'a1001': 's101p61',
  'a1002': 's101p62',
  'a1003': 's101p63',
  'a1004': 's101p65',
  'a1005': 's101p66',
  'a1006': 's101p67',
  'a1007': 's101p68',
  'a1201': 's101p71',
  'a1202': 's101p72',
  'a1203': 's101p73',
  'a1204': 's101p74',
  'a1205': 's101p75',
  'a1206': 's101p76',
  'a1207': 's101p77'}
environmentEC_2016 = environmentEC_2016.rename(columns=column_change2)
environmentEC_2016['s101p64'] = None

column_change3 = {
  'A1001': 's101p121',
  'A1002': 's101p122',
  'A1003': 's101p123',
  'A1004': 's101p124',
  'A1005': 's101p125',
  'A01': 's101p11',
  'A0102A': 's101p12a',
  'A0102B': 's101p12b',
  'A0102C': 's101p12c',
  'A0601': 's101p61',
  'A0602': 's101p62',
  'A0603': 's101p63',
  'A0604': 's101p64',
  'A0605': 's101p64',
  'A0606': 's101p66',
  'A0607': 's101p67',
  'A0608': 's101p68',
  'A0701': 's101p71',
  'A0702': 's101p72',
  'A0703': 's101p73',
  'A0704': 's101p74',
  'A0705': 's101p75',
  'A0706': 's101p76',
  'A0707': 's101p77'}
 
environmentEC_2017 = environmentEC_2017.rename(columns=column_change3)
environmentEC_2017['s101p64'] = None
environmentEC_2017['s101p65'] = None

environmentEC_2022_08['s101p121'] = None
environmentEC_2022_08['s101p122'] = None
environmentEC_2022_08['s101p123'] = None
environmentEC_2022_08['s101p124'] = None
environmentEC_2022_08['s101p125'] = None

column_change4 = {
  's91p91': 's101p121',
  's91p92': 's101p122',
  's91p93': 's101p123',
  's91p94': 's101p124',
  's91p95': 's101p125'}
  
environmentEC_2022_10 = environmentEC_2022_10.rename(columns=column_change4)
environmentEC_2022_10['s101p11'] = None
environmentEC_2022_10['s101p12a'] = None
environmentEC_2022_10['s101p12b'] = None
environmentEC_2022_10['s101p12c'] = None
environmentEC_2022_10['s101p61'] = None
environmentEC_2022_10['s101p62'] = None
environmentEC_2022_10['s101p63'] = None
environmentEC_2022_10['s101p64'] = None
environmentEC_2022_10['s101p65'] = None
environmentEC_2022_10['s101p66'] = None
environmentEC_2022_10['s101p67'] = None
environmentEC_2022_10['s101p68'] = None
environmentEC_2022_10['s101p71'] = None
environmentEC_2022_10['s101p72'] = None
environmentEC_2022_10['s101p73'] = None
environmentEC_2022_10['s101p74'] = None
environmentEC_2022_10['s101p75'] = None
environmentEC_2022_10['s101p76'] = None
environmentEC_2022_10['s101p77'] = None

convert_dict = {
  'area': str,
  's101p121': str,
  's101p122': str,
  's101p123': str,
  's101p124': str,
  's101p125': str,
  's101p11': str,
  's101p12a': str,
  's101p12b': str,
  's101p12c': str,
  's101p61': str,
  's101p62': str,
  's101p63': str,
  's101p64': str,
  's101p65': str,
  's101p66': str,
  's101p67': str,
  's101p68': str,
  's101p71': str,
  's101p72': str,
  's101p73': str,
  's101p74': str,
  's101p75': str,
  's101p76': str,
  's101p77': str}

environmentEC_2015 = environmentEC_2015.astype(convert_dict)
environmentEC_2016 = environmentEC_2016.astype(convert_dict)
environmentEC_2017 = environmentEC_2017.astype(convert_dict)
environmentEC_2018 = environmentEC_2018.astype(convert_dict)
environmentEC_2019 = environmentEC_2019.astype(convert_dict)
environmentEC_2022_08 = environmentEC_2022_08.astype(convert_dict)
environmentEC_2022_10 = environmentEC_2022_10.astype(convert_dict)

years1 = [2015, 2016, 2017, 2018, 2019, 2022_10]  # Exclude 2022_08
years2 = [2015, 2016, 2017, 2018, 2019, 2022_08] # Exclude 2022_10
areas = ['1', '2']

dbs = {2015: environmentEC_2015, 
       2016: environmentEC_2016,
       2017: environmentEC_2017, 
       2018: environmentEC_2018, 
       2019: environmentEC_2019, 
       2022_08: environmentEC_2022_08,
       2022_10: environmentEC_2022_10}


#%% ANALISIS

### QUESTIONS
#question_1 = What environmental problems affect neighborhoods?
#question_2 = Households that sorted or separated some type of waste
#question_3 = Water use practices carried out by households
#question_4 = How do Ecuadorian households save energy?

#Graphs Questions
#Q.0. Graph identifying number of households
#Q.1. % househods that identifyied contamination
#Q.2. Graph Households by area (Rural and Urban)
#Q.3. Distribution of Households by area in %
#Q.4. Distribution of Households by type of contamination
#Q.5. Heatmap of Contamination Problem Perception of Households
#Q.6. Graph per provinces

#%% IDENTIFYING NUMBER OF HOUSEHOLDS
#%%  Graphs identifying number of households

##### 1.1. GRAPH FOR ENVIRONMENTAL PROBLEMS

#List of variables and lables
envs_cols = ['s101p121', 's101p122', 's101p124', 's101p123', 's101p125']
envs_labels = ['Visual pollution', 'Contaminated water', 'Hearing pollution', 'Accumulated garbage', 'Air pollution']

res11 = []

#Filter database 'db' form 'dbs' for each year selecting the affirmative variables and append to factor of expansion 'fexp' for the survey in res10
for year in years1:
  db = dbs[year]
  db = db.query("s101p121 == '1' or s101p122 == '1' or s101p123 == '1' or s101p124 == '1' or s101p125 == '1'")
  res11.append(db['fexp'].sum().round(0))

#Divide the 'households' column values by 1000000 to convert them to millions.
res11 = pd.DataFrame({'years': years1, 'households_env': res11})
res11['households_env'] = res11['households_env'] / 1000000

#Plot a bar graph
ax = res11.plot.bar(x='years', y='households_env', rot=0, width=0.5, ylabel='Number of Households (in Millions)',
xlabel='Years', title=' Households that Identified Contamination Problems', color='#1f4068')

#Put values in the graph
for i, v in enumerate(res11['households_env']):
    ax.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontweight='bold', color='black')
ax.set_ylim(0, 4.0)

#Save the figure
ax.figure.savefig("CPhouseholds.png")

#%%
##### 2.1. GRAPH FOR SORTING WASTE: Household yearly count related to waste types

# List of waste variables and labels
waste_cols = ['s101p11', 's101p12a', 's101p12b', 's101p12c']
waste_labels = ['Organic', 'Paper, Cardboard', 'Plastic', 'Glass']

res21 = []

# Calculate the sums of waste variables by year
for year in years2:
    db = dbs[year]
    db = db.query("s101p11 == '1' or s101p12a == '1' or s101p12b == '1' or s101p12c == '1'")
    res21.append(db['fexp'].sum().round(0))
    
# Create DataFrame for waste sums
res21 = pd.DataFrame({'years': years2, 'households_w': res21})
res21['households_w'] = res21['households_w'] / 1000000

# Plot a line graph
ax = res21.plot.bar(x='years', y='households_w', rot=0, width=0.5, ylabel='Number of Households (in Millions)',
xlabel='Years', title=' Households that Sorted Waste', color='#1f4068')

# Include data in the chart and customize it
for i, v in enumerate(res21['households_w']):
    ax.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontweight='bold', color='black')
ax.set_ylim(0, 4.0)

# Save the figure
ax.figure.savefig("SortedWasteHouseholds.png")

#%%

#1.1. % househods that identifyied contamination

envs_cols = ['s101p121', 's101p122', 's101p124', 's101p123', 's101p125']
envs_labels = ['Visual pollution', 'Contaminated water', 'Hearing pollution', 'Accumulated garbage', 'Air pollution']

res11 = []

for year in years1:
    db = dbs[year]

# Calculate percentage of households that responded '1' for envs_cols variables
    db_1 = db[envs_cols].isin(['1']).any(axis=1)
    db_12 = db[envs_cols].isin(['1', '2']).any(axis=1)
       
    percentage = (db_1.sum() / db_12.sum()) * 100
    
    res11.append({'year': year, 'percentage': percentage})

res11 = pd.DataFrame(res11)
print(res11)

#Plot a bar graph
plt.figure(figsize=(10, 6))
ax = res11.plot.bar(x='year', y='percentage', rot=0, width=0.5, ylabel='Percentage',
xlabel='Year', title='Percentage of Households Identifying Environmental Problems')

# Include data labels in the bar plot
for i, v in enumerate(res11['percentage']):
    ax.text(i, v, f'{v:.1f}%', ha='center', va='bottom', fontweight='bold', color='black')

plt.ylim(0, 100)

plt.xticks(ticks=range(len(years1)), labels=years1)

plt.tight_layout()
plt.show()

# Save the figure
ax.figure.savefig("%EnvProblemPerception.png")



#%%
#1.2. Q1 Graph Households by area (Rural and Urban)

res12 = []

for year in years1:
  db = dbs[year]
  for area in areas:
    db1 = db.query("((s101p121 == '1') or (s101p122 == '1') or (s101p123 == '1') or (s101p124 == '1') or (s101p125 == '1')) and (area == @area)")
    res12.append(db1['fexp'].sum().round(0))

res12 = pd.DataFrame({'Urban': res12[::2], 'Rural': res12[1::2]}, index=years1)
res12['Urban'] = res12['Urban'] / 1000000
res12['Rural'] = res12['Rural'] / 1000000

ax = res12.plot.bar(rot=0, width=0.7, ylabel='Number of Households (in Millions)', xlabel='Years', title='Households that Identified Contamination Problems by area')

for i, v in enumerate(res12['Urban']):
    ax.text(i, v, f'{v:.2f}', ha='right', va='bottom', fontweight='bold', color='black')

for i, v in enumerate(res12['Rural']):
    ax.text(i, v, f'{v:.2f}', ha='left', va='bottom', fontweight='bold', color='black')

ax.set_ylim(0, 3.0)
ax.legend(loc='center', bbox_to_anchor=(0.5, -0.25), ncol=2)

plt.tight_layout()
plt.show()
plt.savefig("CPhouseholdsbyarea.png")



#%%
#1.3. Q1 Distribution of Households by area in %

res13 = []

for year in years1:
  db = dbs[year]
  for area in areas:
    db1 = db.query("((s101p121 == '1') or (s101p122 == '1') or (s101p123 == '1') or (s101p124 == '1') or (s101p125 == '1')) and (area == @area)")
    res13.append(db1['fexp'].sum().round(0))

res13 = pd.DataFrame({'Rural': res13[1::2], 'Urban': res13[::2]}, index=years1)

res13['Total'] = res13['Urban'] + res13['Rural']
res13['Rural%'] = res13['Rural'] / res13['Total'] * 100
res13['Urban%'] = res13['Urban'] / res13['Total'] * 100

ax = res13[['Rural%', 'Urban%']].plot(kind='bar', stacked=True, rot=0, width=0.7, ylabel='Percentage share of households', xlabel='Years', title='Households that Identified Contamination Problems by area', color=['#ff7f0e', '#1f4068'])

for i, v in enumerate(res13['Rural%']):
    ax.text(i, v-10, f'{v:.1f}%', ha='center', va='center', fontweight='bold', color='white')
for i, v in enumerate(res13['Urban%']):
    ax.text(i, v-10, f'{v:.1f}%', ha='center', va='center', fontweight='bold', color='white')

ax.set_ylim(0, 115)
ax.legend(loc='center', bbox_to_anchor=(0.5, -0.25), ncol=2)
plt.tight_layout()
plt.show()
plt.savefig("CPbyarea.png")


#%%
#1.4. Q1 Distribution of Households by type of contamination

envs_cols = ['s101p121', 's101p122', 's101p124', 's101p123', 's101p125']
envs_labels = ['Visual pollution', 'Contaminated water', 'Accumulated garbage', 'Hearing pollution', 'Air pollution']

res14 = {
    'Visual pollution': [],
    'Contaminated water': [],
    'Accumulated garbage': [],
    'Hearing pollution': [],
    'Air pollution': []}

for year in years1:
    db = dbs[year]
    tmp = []
    for col, label in zip(envs_cols, envs_labels):
        db1 = db[db[col] == '1']
        val = db1['fexp'].sum().round(0)
        tmp.append(val)
    res14['Visual pollution'].append(tmp[0])
    res14['Contaminated water'].append(tmp[1])
    res14['Accumulated garbage'].append(tmp[2])
    res14['Hearing pollution'].append(tmp[3])
    res14['Air pollution'].append(tmp[4])

res14 = pd.DataFrame(res14, index=years1)

res14['Visual pollution'] = res14['Visual pollution'] / 1000000
res14['Contaminated water'] = res14['Contaminated water'] / 1000000
res14['Accumulated garbage'] = res14['Accumulated garbage'] / 1000000
res14['Hearing pollution'] = res14['Hearing pollution'] / 1000000
res14['Air pollution'] = res14['Air pollution'] / 1000000

# Plot the stacked bar chart
res14.plot(kind='bar', stacked=True, figsize=(12, 8))

# Set the labels and title
plt.xlabel('Year',fontsize=16)
plt.ylabel('Number of Households (in millions)', fontsize=16)
plt.title('Households that Identified Contamination Problems by Type', fontsize=18)

plt.legend(title='Contamination Types', labels=envs_labels)
plt.xticks(rotation=45, ha='right')

#Save the figure
plt.show()
plt.savefig("CPbyarea.png")


#%% 1.5. Heatmap of Contamination Problem Perception of Households

envs_cols = ['s101p121', 's101p122', 's101p124', 's101p123', 's101p125']
envs_labels = ['Visual pollution', 'Contaminated water', 'Accumulated garbage', 'Hearing pollution', 'Air pollution']

res15 = {
    '%Visual pollution': [],
    '%Contaminated water': [],
    '%Accumulated garbage': [],
    '%Hearing pollution': [],
    '%Air pollution': []
}

for year in years1:
    db = dbs[year]
    perc = []
    for col, label in zip(envs_cols, envs_labels):
        db1 = db[db[col] == '1']
        val = db1['fexp'].sum().round(0)
        perc.append(val)
    res15['%Visual pollution'].append((perc[0] / sum(perc)) * 100)
    res15['%Contaminated water'].append((perc[1] / sum(perc)) * 100)
    res15['%Accumulated garbage'].append((perc[2] / sum(perc)) * 100)
    res15['%Hearing pollution'].append((perc[3] / sum(perc)) * 100)
    res15['%Air pollution'].append((perc[4] / sum(perc)) * 100)

res15 = pd.DataFrame(res15, index=years1)

print("Table of Percentage of Households per Contamination Type:")
print(res15)

# Create heatmap
plt.figure(figsize=(7, 5))
ax = sns.heatmap(res15[['%Visual pollution', '%Contaminated water', '%Accumulated garbage', '%Hearing pollution', '%Air pollution']],
            annot=True, cmap='YlGnBu', fmt=".1f", cbar=True)
plt.title('Contamination Problem Perception of Households by Type')
plt.xlabel('Contamination Type')
plt.ylabel('Year')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("%HouseholdsPerContaminationType_Year.png")
plt.show()



#%% Graph per provinces

envs_cols = ['s101p121', 's101p122', 's101p124', 's101p123', 's101p125']
envs_labels = ['Visual pollution', 'Contaminated water', 'Accumulated garbage', 'Hearing pollution', 'Air pollution']

db = dbs[2019].copy()
db[envs_cols] = db[envs_cols].apply(pd.to_numeric)

counts = db.groupby('PROVINCE_NAME')[envs_cols].sum().round(0)
counts_df = pd.DataFrame(counts, columns=envs_cols)
counts_df['Total'] = counts_df.sum(axis=1)
counts_df = counts_df.sort_values(by='Total', ascending=False)
counts_df = counts_df.drop('Total', axis=1)

# Generate the bar plot
ax = counts_df.plot.bar(rot=90, figsize=(10, 6))
ax.legend(loc='center', bbox_to_anchor=(0.5, -0.25), ncol=2)

plt.xlabel('Provinces', fontsize=14)
plt.ylabel('Households', fontsize=14)
plt.title('Environmental Problems identified by Provinces - 2022', fontsize=16)

ax.set_xticklabels(counts_df.index)
ax.legend(envs_labels)
plt.tight_layout()
plt.savefig("%HouseholdsPerContaminationProvinces_YearBAR.png")
plt.show()

# Generate the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(counts, annot=True, cmap='YlGnBu', fmt='.0f', linewidths=0.5)

plt.xlabel('Environmental Problems', fontsize=14)
plt.ylabel('Provinces', fontsize=14)
plt.title('Environmental Problems identified by Provinces - 2019', fontsize=16)

plt.xticks(ticks=range(len(envs_cols)), labels=envs_labels, rotation=50)
plt.savefig("%HouseholdsPerContaminationProvinces_YearHM.png")
plt.show()


