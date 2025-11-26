import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("pokemon_data.csv")

"""
Data Cleaning First Step: 
By making sure the info of data types and the missing values are laid out.
print(df.info())
print(df.describe())
print(df.isnull().sum())
df.fillna('None')
"""

#Data Cleaning by Duplicate Checking
#df.duplicated().sum()


#Data Cleaning by Capitalization
df['Type 1'] = df['Type 1'].str.strip().str.capitalize()
df['Type 2'] = df['Type 2'].str.strip().str.capitalize()

df['Name'] = df['Name'].str.strip().str.title()

"""
Removing Venusaurmega Venusaur to be Mega Venusaur only to make it readable
df['Name'] = df['Name'].str.replace(r'^(\\w+)Mega\\s*(.*)', r'Mega \2', regex=True)
df[df['Name'].str.contains('Mega ', regex=False)]
print(df[df['Name'].str.contains('Mega')]['Name'].unique())
"""

"""
The first step in Data Correlations 
print(df[['HP', 'Attack', 'Defense']].corr())
"""

#Show which Pokemon type has Highest avg attack

"""
avg_attack_by_type = df.groupby('Type 1')['Attack'].mean().sort_values(ascending=False)
print(avg_attack_by_type)
"""

#DATA VISUALIZATION
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Pokémon Power Grid: Attack Stats Across Types and Traits', fontsize=16, fontweight='bold')
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'

#Flatten axes for easy indexing
axs = axs.flatten()

#Chart 1: Scatterplot
sns.scatterplot(x='Attack', y='Defense', data=df, ax=axs[0])
axs[0].set_title('Attack vs Defense')

#Chart 2: Bubble Chart
sns.scatterplot(x='Attack', y='Speed', size='HP', sizes=(20, 200), hue='Type 1', data=df, ax=axs[1], legend=False)
axs[1].set_title('Attack vs Speed')

#Chart 3: Violin Plot
sns.violinplot(
    x='Attack',
    y='Type 1',
    hue = 'Type 1',  
    palette='Set2',
    dodge = False, 
    data=df, 
    ax=axs[2])
axs[2].set_title('Attack Distribution by Pokemon Type')
axs[2].tick_params(axis='x', labelsize=9)
#add legend mapping colors to the types like i wanted


#Chart 4: Grouped bar chart
top5 = df[df['Type 1']=='Dragon'].nlargest(5, 'Attack')
axs[3].bar(top5['Name'], top5['Attack'])
axs[3].set_title('Top 5 Dragon Pokemon Attack')
axs[3].tick_params(axis='x', rotation=10)


plt.tight_layout(pad=2.0)
plt.show()

#---------------------------------------------------------------------
#Chart 5: Heatmap(final piece)
plt.figure(figsize=(8,6))
corr = df[['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].corr()
hm = sns.heatmap(corr, annot=True, cmap='YlOrRd', fmt='.2f', linewidths=0.5, linecolor='white', square=True, annot_kws={"size": 10})


plt.title('Overall Pokemon Stat Correlation', fontweight='bold')
plt.xticks(rotation=45)
plt.yticks(rotation=0)


plt.show()