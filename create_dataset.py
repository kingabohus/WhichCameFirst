sources = list()
inventions = list()
links = list()
with open('historic_inventions_table.tsv', 'r') as file:
    for line in file:
        line = line.strip()
        line_split = line.split('\t')
        sources.append(line_split[0])
        inventions.append(line_split[1])
        if len(line_split) == 3:
            links.append(line_split[2])
        else:
            link = line_split[1]
            link = link.replace(' ','_')
            links.append('/wiki/{}'.format(link))

del sources[0]
del inventions[0]
del links[0]

date_texts = list()
value_mins = list()
value_maxs = list()
flavor_texts = list()

century_dict = {
    "1st century" : "0 - 100",
    "2nd century" : "100 - 200",
    "3rd century": "200 - 300"
}
for i in range(20):
    century_dict["{}th century".format(i+4)] = "{}00 - {}00".format(i+3, i+4)


date_dict = {
    "Mya" : -1e6,
    "kya" : -1000,
    "BC" : -1,
    "AD" : 1
}

def date_to_num(date):
    date = date.replace(',','')
    keys = list(century_dict.keys())
    keys.reverse()
    for key in keys:
        date = date.replace(key, century_dict[key])
    print(date)
    if len(date.split('-')) == 1:
        date = date.strip()
        if date.isnumeric():
            return int(date), int(date)
        else:
            first_part = date.split(' ')[0]
            second_part = date.split(' ')[1]
            value = float(first_part) * date_dict[second_part]
            return value, value

    elif len(date.split('-')) == 2:
        # if beginning date has no text (e.g. BC), copy text from end date
        begin_date = date.split('-')[0]
        end_date = date.split('-')[1]
        begin_date = begin_date.strip()
        end_date = end_date.strip()

        if begin_date.isnumeric() and end_date.isnumeric():
            return min(int(begin_date), int(end_date)), max(int(begin_date), int(end_date))
        else:
            if len(begin_date.split(' ')) == 1:
                begin_date = float(begin_date) * date_dict[end_date.split(' ')[1]]
                end_date = float(end_date.split(' ')[0]) * date_dict[end_date.split(' ')[1]]
            else:
                begin_date = float(begin_date.split(' ')[0] ) * date_dict[end_date.split(' ')[1]]
                end_date = float(end_date.split(' ')[0] ) * date_dict[end_date.split(' ')[1]]

        #basically same code here
        return min((begin_date), (end_date)), max((begin_date), (end_date))
    else:
        Exception("problem with date {}".format(date))


for source in sources:
    date_split = source.split(':')
    date = date_split[0].replace('"','')
    date = date.replace('–','-')

    value_min, value_max = date_to_num(date)
    print(value_min, value_max)

    date = date.replace("Mya", "million years ago")
    date = date.replace("kya", "thousand years ago")
    date_texts.append(date)
    value_mins.append(value_min)
    value_maxs.append(value_max)
    flavor_text = date_split[1].strip("\"")
    flavor_texts.append(flavor_text)

with open("dataset.txt", 'w') as file:
    for i in range(len(inventions)):
        file.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(i, inventions[i], links[i], date_texts[i], value_mins[i], value_maxs[i], flavor_texts[i] ))

