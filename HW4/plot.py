import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('HW4-friend-count.csv')

num_friends = df['FRIENDCOUNT']

mean_friends = num_friends.mean()
std_dev_friends = num_friends.std()
median_friends = num_friends.median()

sorted_friends = num_friends.sort_values(ascending=False)

plt.barh(range(len(sorted_friends)), sorted_friends)

user_friends = 250 
plt.axvline(x=user_friends, color='r')

plt.text(user_friends+10, len(sorted_friends)-20, 'U', fontsize=12)

plt.xlabel('Number of friends')
plt.ylabel('Friend number')
plt.title('Number of friends of user\'s friends')

plt.show()

print('Mean number of friends:', mean_friends)
print('Standard deviation of number of friends:', std_dev_friends)
print('Median number of friends:', median_friends)
