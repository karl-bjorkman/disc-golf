import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

scorecard_data = pd.read_csv('scorecards.csv')

scorecards = scorecard_data[(scorecard_data.PlayerName == 'Karl Bjorkman') & (scorecard_data.CourseName == 'D. F. Buchmiller Park')]
scorecards = scorecards.drop(columns = ['PlayerName', 'CourseName', 'LayoutName'])
print()

# Total Score:

# print(scorecards.Total.array)
# print(np.flip(scorecards.Total.array))

rev_total_scores = np.array(scorecards.Total)
total_scores = np.flip(rev_total_scores)

scores_min = np.min(total_scores)
scores_max = np.max(total_scores)
scores_range = scores_max - scores_min
scores_std = np.std(total_scores)

print('Min: ' + str(scores_min))
print('Max: ' + str(scores_max))
print('Range: ' + str(scores_range))
print('STD: ' + str(scores_std))

plt.figure(figsize = (16, 9))
ax1 = plt.subplot(2, 1, 1)

plt.title('Total Scores Over Time at D.F. Buchmiller Park', pad = 15)
ax1.set_ylabel('Total Score (Par: 54)', labelpad = 15)

ax1.set_xticks(range(len(total_scores)))
ax1.set_yticks(range(scores_min, scores_max + 1))

ax1.axhline(54, color = 'gray', linestyle = '--', linewidth = 0.8)

plt.plot(total_scores, color='green', marker='o')

# Adjusted Score:

plus_minus = np.flip(scorecards['+/-'].array).astype('int')
print(plus_minus)

plus_minus_min = np.min(plus_minus)
plus_minus_max = np.max(plus_minus)

ax2 = plt.subplot(2, 1, 2)

ax2.set_xlabel('Round Number', labelpad = 15)
ax2.set_ylabel('Total Score (Par: E)', labelpad = 15)

pm_yticks = []
plus = ''
for i in range(plus_minus_min, plus_minus_max + 1):
    if i < 0:
        pm_yticks.append(str(i))
    elif i == 0:
        pm_yticks.append('E')
    else:
        plus = str(i)
        pm_yticks.append('+' + plus)

ax2.set_xticks(range(len(plus_minus)))
ax2.set_yticks(range(plus_minus_min, plus_minus_max + 1))
ax2.set_yticklabels(pm_yticks)

ax2.axhline('E', color = 'gray', linestyle = '--', linewidth = 1)

plt.plot(plus_minus, color='blue', marker='o')

plt.show()
plt.close('all')

# Above or below par

over = 0
under = 0
even = 0

outcomes = ['Over', 'Under', 'Even']

for i in total_scores:
    if i > 54:
        over += 1
    elif i < 54:
        under += 1
    else:
        even += 1

outcome_counts = [over, under, even]

plt.figure(figsize = (10, 8))
ax3 = plt.subplot()
ax3.set_title('Score Distribution in Relation to Par', pad = 15)
ax3.set_xlabel('Par Outcomes', labelpad = 15)
ax3.set_ylabel('Number of Rounds', labelpad = 15)

plt.bar(outcomes, outcome_counts, color = ['red', 'green', 'yellow'], edgecolor = 'black')
plt.show()