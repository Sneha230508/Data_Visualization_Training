# 5. Online Exam Result Processor

scores = [35, 20, 50, 30, 80, 25, 40]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count pass students
passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Number of Passed Students:", passed)
#output
"""Updated Scores:[30,40,45,50,80]
Number of Passed Students: 4"""