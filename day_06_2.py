with open('inputs/input_06.txt', 'r') as infile:
    groups = infile.read().split('\n\n')

individual_questions = [[set(q) for q in g.split('\n')] for g in groups]

num_questions = 0

for group_questions in individual_questions:
    num_questions += len(set.intersection(*group_questions))

print(num_questions)
