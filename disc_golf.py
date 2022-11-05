import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

scorecard_data = pd.read_csv('scorecards.csv')

scorecards = scorecard_data[(scorecard_data.PlayerName == 'Karl Bjorkman') & (scorecard_data.CourseName == 'D. F. Buchmiller Park')]
scorecards = scorecards.drop(columns = ['PlayerName', 'CourseName', 'LayoutName'])
print()

print(scorecards.Total.describe())

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

plt.figure(figsize = (15, 8))
ax = plt.subplot()

plt.title('Total Scores Over Time at D.F. Buchmiller Park')
plt.xlabel('Round Number (In Order)')
plt.ylabel('Total Score (Par: 54)')

ax.set_xticks(range(len(total_scores)))
ax.set_yticks(range(scores_min, scores_max + 1))

plt.plot(total_scores, color = 'green', marker = 'o')
plt.show()

plt.savefig('total_scores.png')