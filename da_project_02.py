import pandas as pd
df = pd.read_csv('adult_csv.csv')
# # print(df.head())
# # print(df.tail())
# # print(df.race.unique()) all unique races in dataframe
# rc = pd.Series(df['race']).value_counts()
# # print(rc) #number of each race
#
# m = round(df[df['sex'] == 'Male'].mean()[0],1)
# # print('avg age of men', m)
#
# b = round(df[df['education'] == 'Bachelors'].count()[3] / df.count()[3],1)
# # print('percentage of people with Bachelors', b)
#
# bac = df[df['education'] == 'Bachelors'].count()[3]
# mas = df[df['education'] == 'Masters'].count()[3]
# doc = df[df['education'] == 'Doctorate'].count()[3]
#
# hied = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[3]
# gr = df[df['class'] == '>50K'].count()[14]
# # print(hied)
# # print(gr)
# #print(df[df['class'] == '<=50K'].count()[14])
# ans = (df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[3] & df[df['class'] == '>50K'].count()[14])
# # print(df.count()[3])
# # ans = round((df.count()[3]-hied)/df.count()[3],1)
# hpw = df['hoursperweek'].min()
# # print('minimum hours', hpw)
# rmh = df[df['hoursperweek'] == hpw].count()[12]
# # print(rmh)
# # print(df['native-country'].value_counts())
# richc = round((df['native-country'].value_counts() & df[df['class'] == '>50K'].count()[14]) / (df['native-country'].value_counts()),1).max()
# print(richc)
# bac = df[df['education'] == 'Bachelors'].count()[3]
# mas = df[df['education'] == 'Masters'].count()[3]
# doc = df[df['education'] == 'Doctorate'].count()[3]
# higher_education = bac + mas + doc
# # print(bac)
# # print(mas)
# # print(doc)
# # print(df.count()[3]) #all people in education column
# higher_education_rich = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[3]
# # & df[df['class'] == '>50K'].count()[14]) / higher_education * 100, 1)
# # print(higher_education_rich)
# rich = ((df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['class'] == '>50K')).value_counts(sort=True)[1]
# # print(rich)
#
# lower = df.count()[3] - higher_education_rich
# # print(lower)
# lowrich = ((~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['class'] == '>50K')).value_counts(sort=True)[1]
# # print(lowrich)
# # print(lowrich/lower)
#
# min_work_hours = df['hoursperweek'].min()
# num_min_workers = df[df['hoursperweek'] == min_work_hours].count()[12]
# rich_percentage = round(((df['hoursperweek'] == min_work_hours) & (df['class'] == '>50K')).value_counts(ascending=True)[1])
# print(min_work_hours)
# print(num_min_workers)
# print(rich_percentage)

hcnt = df[df['class'] == '>50K'].count()[13] #total number of countries with salaries >50K
tot = df.loc[df['class'].isin(['>50K', '<=50K']), ['native-country']].value_counts()
sal = df.loc[df['class'] == '>50K', ['native-country']].value_counts()
# print(tot)
# print(sal)

countrypercent = round((sal/tot) * 100,1)
hg = countrypercent.sort_values(ascending=False).index.tolist()[0] #puts tuples into a list
jk = ''.join(hg)
print(jk)

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = df.loc[((df['native-country'] == 'India') & (df['class'] == '>50K')), ['occupation']].value_counts().index.tolist()[0]
# print(top_IN_occupation)
ai = ''.join(top_IN_occupation) #converts tuple into string
print(ai)




def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult_csv.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = pd.Series(df['race']).value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male'].mean()[0],1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df[df['education'] == 'Bachelors'].count()[3] / df.count()[3],1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    bac = df[df['education'] == 'Bachelors'].count()[3]
    mas = df[df['education'] == 'Masters'].count()[3]
    doc = df[df['education'] == 'Doctorate'].count()[3]
    higher_education = round((bac + mas + doc) / df.count()[3],1)
    lower_education = round(df.count()[3] - (bac+mas+doc) / df.count()[3],1)

    # percentage with salary >50K
    higher_education_rich = round((df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[3] & df[df['salary'] == '>50K'].count()[14]) / (higher_education), 1)
    lower_education_rich = round((df[df['salary'] == '>50K'].count()[14] - df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()[3] & df[df['salary'] == '>50K'].count()[14]) / (lower_education),1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].count()[12]

    rich_percentage = round((df[df['hours-per-week'] == min_work_hours].count()[12] & df[df['salary'] == '>50K'].count()[14]) / (num_min_workers),1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = None
    highest_earning_country_percentage = round((df['native-country'].value_counts() & df[df['salary'] == '>50K'].count()[14]) / (df['native-country'].value_counts()),1).max()

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = None
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
