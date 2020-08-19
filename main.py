import csv
import pandas as pd

#Using the pandas library, read the elements of the log_file.csv file and store it into a pandas dataframe
df = pd.read_csv("log_file.csv")

#Print the pandas dataframe
print('\n\n*************** Pandas dataframe information ***************\n\n')
print(df.info())

print('\n\n*************** Results for Question 1 ***************\n\n')
#A string list which contains the names of the printed headers
col_list = ['Requestor IP', 'Duration of the request - in microseconds']
#Print the columns Requestor IP and Duration of the Request
print(df[col_list])


print('\n\n*************** Results for Question 2 ***************\n\n')
#Convert the elements of the column Requested Route onto a list and store them into an string list
stringList = df['Requested Route'].to_numpy().tolist()

#Initialize counters
counter_route1 = 0
counter_route2 = 0
counter_route3 = 0
counter_route11 = 0

#Print the entire elements of the Array List
print('Elements of the string list: ', stringList)

# This for loop iterates the array list and seeks for the corresponding values if a value is located
# within the array list then the corresponding counter is increased by 1
# Execution time O(n+1)
for row in stringList:
    # When /route1 is located onto string list increase counter_route1 by 1
    if str(row).count('route1') == 1 and str(row).count('route11') == 0:
        counter_route1 = counter_route1 + 1
    # When /route2 is located onto string list increase counter_route2 by 1
    elif str(row).count('route2') == 1:
        counter_route2 = counter_route2 + 1
    # When /route3 is located onto string list increase counter_route3 by 1
    elif str(row).count('route3') == 1:
        counter_route3 = counter_route3 + 1
    # When /route11 is located onto string list increase counter_route11 by 1
    elif str(row).count('route11') == 1:
        counter_route11 = counter_route11 + 1

#Print on the screen the times which a route appeared
print('\nFor loop execution ended.\n- Execution time: O(N+1) -\n')
print('Route 1 appeared: '  +   str(counter_route1)   +  ' times...')
print('Route 2 appeared: '  +   str(counter_route2)   +  ' times...')
print('Route 3 appeared: '  +   str(counter_route3)   +  ' times...')
print('Route 11 appeared: ' +   str(counter_route11)  +  ' times...')