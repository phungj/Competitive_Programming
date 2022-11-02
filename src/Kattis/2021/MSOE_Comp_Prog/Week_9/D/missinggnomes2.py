params = input().split(" ")
params = [int(param) for param in params]

if params[0] == params[1]:
    for i in range(1, params[0] + 1):
        print(input())

    exit(0)

else:
    all_gnomes = set(range(1, params[0] + 1))
    remaining_gnomes = []
    sorted = True
    prev_gnome = -1

    for _ in range(params[1]):
        current_gnome = int(input())

        remaining_gnomes.append(current_gnome)
        all_gnomes.remove(current_gnome)

        if sorted and prev_gnome > current_gnome:
            sorted = False
        elif sorted:
            prev_gnome = current_gnome

    if sorted:
        print('\n'.join([str(i) for i in range(1, params[0] + 1)]))

        exit(0)
    else:
        missing = False

        for missing_gnome in all_gnomes:
            for remaining_gnome in remaining_gnomes:
                if missing_gnome < remaining_gnome:
                    print(missing_gnome)
                    missing = True
                    break
                else:
                    print(remaining_gnome)
                    remaining_gnomes = remaining_gnomes[1:]

            if missing:
                missing = False
                continue
            else:
                print(missing_gnome)

        remaining_gnomes = [str(gnome) for gnome in remaining_gnomes]

        print('\n'.join(remaining_gnomes))
