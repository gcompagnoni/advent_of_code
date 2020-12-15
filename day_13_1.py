with open('inputs/input_13.txt', 'r') as infile:
    arrival_time, ids = infile.read().split()

arrival_time = int(arrival_time)
valid_ids = [int(k) for k in ids.split(',') if k.isdigit()]

min_wait = 2 ** 30
first_bus = None
for bus in valid_ids:
    wait = -arrival_time % bus
    if wait < min_wait:
        first_bus = bus
        min_wait = wait

print(f'Shortest waiting time is {min_wait} minutes for bus {first_bus}.\n', min_wait * first_bus)
