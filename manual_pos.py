
datelist = list()

with open('historic_inventions_plain.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        date = line.split(':')[0]
        date_split = date.split()
        if date_split[-1] == "Mya":
