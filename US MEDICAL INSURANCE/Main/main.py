# Average age of insurance users
import csv
from statistics import mean

def average_age(csv_path):
    with open(csv_path) as US_insurance:
        content = csv.DictReader(US_insurance)
        age_list = []
        for line in content:
            age_list.append(line['age'])
        average_age = mean(map(float, age_list))
        return 'The average age of patients with medical insurance in the US is '+str(average_age) + '.'

# # print (age_list)
# print(average_age('insurance.csv'))
# print(' ')


# Majority of user's region
from collections import Counter

def most_common_region(csv_path):
    with open(csv_path) as US_insurance:
        content = csv.DictReader(US_insurance)
        location_list = []
        for line in content:
            location_list.append(line['region'])
    def most_frequent(list):
        occurence_count = Counter(list)
        return occurence_count.most_common(1)[0][0]
    return 'The most common region of US medical insurance users is '+ most_frequent(location_list)+'.'
# print('The most common region of US medical insurance users is '+ most_frequent(location_list)+'.')
# print(most_common_region('insurance.csv'))
# print('')


# Difference between insurance costs of smokers and non-smokers.
from statistics import mean

def smoker_vs_nonsmokers(csv_path):
    with open(csv_path) as US_insurance:
        content = csv.DictReader(US_insurance)
        smokers_list = []
        nonsmokers_list = []
        for line in content:
            if line['smoker'] == 'yes':
                smokers_list.append(line['charges'])
            else:
                nonsmokers_list.append(line['charges'])
        average_smokers = mean(map(float, smokers_list))
        average_nonsmokers = mean(map(float, nonsmokers_list))
        return '''The average insurance cost of smokers is ${} and the average insurance cost of non-smokers is ${}.
Thus, on average, medical insurance for smokers in the US cost ${} more than the insurance costs of non-smokers.'''.format(str(round(average_smokers,2)),str(round(average_nonsmokers,2)),str(round(average_smokers-average_nonsmokers,2)))

# print(smoker_vs_nonsmokers('insurance.csv'))
# print(' ')


# Average age of insurance users with children.
def parent_age(csv_path):
    with open(csv_path) as US_insurance:
        content = csv.DictReader(US_insurance)
        parent_list = []
        for line in content:
            if int(line['children']) >= 1:
                parent_list.append(line['age'])
    return ('The average age of medical insurance users with one or more children is ' + str(mean(map(float, parent_list)))+' in the US.')

# print(parent_list)
# print(parent_age('insurance.csv'))


# A function that takes CSV file breaks down all the crucial trends of US Medical Insurance users and presents the findings in 1 summary
def full_analysis(csv_path):
    return average_age(csv_path) + 2*'\n' + most_common_region(csv_path) +2*'\n' + smoker_vs_nonsmokers(csv_path) + 2*'\n' + parent_age(csv_path)
print(full_analysis('insurance.csv'))


print('''

Now, to determine which factors are the most influential towards medical insurance costs we will analyse smoking status, region and parenthood:''')
def smoker_v_nonsmokers(csv_path):
    with open(csv_path) as US_insurance:
        content = csv.DictReader(US_insurance)
        smokers_list = []
        nonsmokers_list = []
        for line in content:
            if line['smoker'] == 'yes':
                smokers_list.append(line['charges'])
            else:
                nonsmokers_list.append(line['charges'])
        average_smokers = mean(map(float, smokers_list))
        average_nonsmokers = mean(map(float, nonsmokers_list))
        return '''As previously mentioned, the medical insurance costs of smokers in the US are [${}] higher than non-smokers.'''.format(str(round(average_smokers-average_nonsmokers,2)))
print(smoker_v_nonsmokers('insurance.csv'))

def northwest_v_southwest(csv_path):
    with open(csv_path) as US_insurance:
        content = csv.DictReader(US_insurance)
        north_list = []
        south_list = []
        for line in content:
            if line['region'] == 'southwest':
                south_list.append(line['charges'])
            else:
                north_list.append(line['charges'])
        average_south = mean(map(float, south_list))
        average_north = mean(map(float, north_list))
        return '''The average insurance cost of northwest residents is ${} and the average insurance cost of southwest is ${}.
Thus, on average, medical insurance costs for patients based in the northwest is [${}] higher than the insurance costs of citizens from southwest.'''.format(str(round(average_north,2)),str(round(average_south,2)),str(round(average_north-average_south,2)))

print(northwest_v_southwest('insurance.csv'))

def children_v_nochildren(csv_path):
    with open(csv_path) as US_insurance:
        content = csv.DictReader(US_insurance)
        child_list = []
        nochild_list = []
        for line in content:
            if line['children'] == '0':
                nochild_list.append(line['charges'])
            else:
                child_list.append(line['charges'])
        average_child = mean(map(float, child_list))
        average_nochild = mean(map(float, nochild_list))
        return '''The average insurance cost of parents is ${} and the average insurance cost of patients with no children is ${}.
Thus, on average, medical insurance costs for patients with children is [${}] higher than the insurance costs of non-parents.'''.format(str(round(average_child,2)),str(round(average_nochild,2)),str(round(average_child-average_nochild,2)))
print(children_v_nochildren('insurance.csv'))

print('''
Ultimately, judging from the difference in average costs across the 3 categories of demographic information,
It is evident that smoking status is the most influential factor towards the cost of medical insurance as it yielded the largest difference in average costs.''')