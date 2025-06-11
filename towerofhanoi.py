def tower_of_hanoi(n, source, helper, target, pegs):

    if n == 1:

        disk = pegs[source].pop()

        pegs[target].append(disk)

        print(f"Move disk {disk} from {source} to {target}")

        return



    tower_of_hanoi(n - 1, source, target, helper, pegs)

    disk = pegs[source].pop()

    pegs[target].append(disk)

    print(f"Move disk {disk} from {source} to {target}")

    tower_of_hanoi(n - 1, helper, source, target, pegs)



n = 4

pegs = {

    'A': [3,2,1,0],

    'B': [],

    'C': []

}



print("\nInitial Pegs State:")

for peg in 'ABC':

    print(f"{peg}: {pegs[peg]}")



tower_of_hanoi(n, 'A', 'B', 'C', pegs)



print("\nFinal Pegs State:")

for peg in 'ABC':

    print(f"{peg}: {pegs[peg]}")

