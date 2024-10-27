input_data = input('Creating a simulated hell scenario: ').split('/')
max_height = int(input_data[0])
forbidden_thorns = input_data[1].split(',')
max_fatigue = float(input_data[2])
fatigue_costs = {1: 0, 2: 0, 3: 0}
initial_costs = [float(n) for n in (input_data[3].split(','))]
if len(initial_costs) > 1:
    for i in range(1,len(initial_costs)+1):
         fatigue_costs[i] = initial_costs[i-1]
elif initial_costs != 0:
    energy_use_all = initial_costs[0]
    for i in range(1,4):
        fatigue_costs[i] = energy_use_all
banned_thorn_thorns = [int(n) for n in forbidden_thorns]
path_count = 0

def get_path(current_thorn,used_energy):
    global path_count
    if (used_energy > max_fatigue) or (current_thorn != 0 and current_thorn in banned_thorn_thorns) or (current_thorn > max_height): return
    if current_thorn == max_height: 
        path_count += 1
        return
    for step_size in range(1,4):
        get_path(current_thorn+step_size,used_energy+fatigue_costs[step_size])

get_path(0,0)
print(
f'''Height: {max_height}
thorn At: {forbidden_thorns}
Max Tiredness: {max_fatigue}
Tiredness Values: {fatigue_costs}
--------------------------------------------------
The ways to escape is/are {path_count} ways''')