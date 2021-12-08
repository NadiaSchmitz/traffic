from random import randint

cars = []
check = 0
random_number = randint(1, 10)
# A traffic light at the turn for the “MEGA” shopping center from the Novomoskovskiy highway
# works in such a way that k cars are able to take a turn in one minute. At weekends all the
# residents of the city drive to the mall to take a shopping, which results in a huge traffic
# jam at the turn. Administration of the mall ordered to install a camera at the nearby bridge,
# which is able to calculate the number of cars approaching this turn from the city.
# The observation started n minutes ago. You should use the data from the camera to determine
# the number of cars currently standing in the traffic jam.
# Input
# The first line contains integers k and n (1 ≤ k, n ≤ 100), which are the number of cars that
# can take a turn to “MEGA” in one minute and the number of minutes passed from the beginning
# of observation. The second line contains space-separated integers a1, …, an (0 ≤ ai ≤ 100),
# where ai is the number of cars that approached the turn during the i-th minute.
# The observation started at morning, when there were no cars at the turn.
# Output
# Output the number of cars currently standing in the traffic jam.

while check == 0:
    k = int(input("Enter the number of cars turning in a minute: "))
    n = int(input("Enter the number of minutes from the beginning of registration: "))
    i = 0
    while i <= n:
        cars.append(k * randint(1, 4))
        rest = cars[0]
        i += 1

    if k <= 0 or n <= 0:
        print("Wrong number.")
    else:
        check = 1
        i = 0
        while i <= n:
            cars.append(k * randint(1, 4))
            rest = rest + cars[i] - k
            i += 1
print(rest)


