from random import random
ORIGINAL_ACC = .95
NUM_TRIALS = 1_000_000
PRECISION = .6
SENSITIVITY = .96
PROPORTION_SICK = .7
overall_success = (SENSITIVITY * PROPORTION_SICK) + ((1-PROPORTION_SICK)*SENSITIVITY)

true_pos = true_neg = false_pos = false_neg = 0
pos_count = neg_count = 0
correct_count = 0
sick_count = 0

for _ in range(NUM_TRIALS):
    is_sick = random() < PROPORTION_SICK
    if is_sick:
        test_sick = random() < SENSITIVITY
        if test_sick:
            correct_count += 1
            pos_count += 1
            true_pos += 1
        else:
            neg_count += 1
            false_neg += 1
        sick_count += 1
    else:
        test_not_sick = random() < PRECISION
        if test_not_sick:
            correct_count += 1
            neg_count += 1
            true_neg += 1
        else:
            pos_count += 1
            false_pos += 1

print('correct / NUM_TRIALS =', correct_count/NUM_TRIALS)
true_pos /= pos_count
true_neg /= neg_count
false_pos /= pos_count
false_neg /= neg_count
print("P(+|D)P(D) + P(-|D')P(D')", (true_pos * PROPORTION_SICK) + ((1-PROPORTION_SICK) *true_neg))
#print(f'{true_pos=}, {true_neg=}, {false_pos=}, {false_neg=}')


    
    
