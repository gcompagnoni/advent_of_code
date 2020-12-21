with open('inputs/input_06.txt', 'r') as infile:
    groups = infile.read().split('\n\n')

unique_questions = [set(g.replace('\n', '')) for g in groups]

num_questions = 0

for group_questions in unique_questions:
    num_questions += len(group_questions)

print(num_questions)
