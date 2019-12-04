
def open_input(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(line)
    return data

def compute_fuel(mass):
    fuel = int(mass / 3)
    return ((fuel - 2) if fuel > 1 else 0)

def compute_full_fuel(mass_init):
    mass = mass_init
    fuel = 0
    while(mass > 2):
        mass = compute_fuel(mass)
        fuel += mass
    return fuel

if __name__ == "__main__":
    data = open_input('input1.txt')
    sum = 0
    print(compute_full_fuel(1969))
    for line in data:
        sum += compute_full_fuel(int(line))
    print('sum = ' + str(sum))
    pass