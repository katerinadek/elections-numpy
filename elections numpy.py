import codecademylib
import numpy as np
from matplotlib import pyplot as plt


survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])

print (total_ceballos)


percentage_ceballos = 100 * total_ceballos/len(survey_responses)

print(percentage_ceballos)

total_sp = float(len(survey_responses))

possible_surveys = np.random.binomial(total_sp, 0.54, size=10000) /total_sp

plt.hist(possible_surveys, range=(0,1), bins = 20)
plt.show()

ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print (ceballos_loss_surveys)

large_l = float(7000)
possible_surveys_2 = np.random.binomial(large_l, 0.54, size=10000) /large_l

plt.hist(possible_surveys_2, range=(0,1), bins = 20)
plt.show()


ceballos_loss_new = np.mean (possible_surveys_2 < 0.5)
print (ceballos_loss_new)