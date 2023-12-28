import csv

def read_csv(filename):
    rows = []
    try:
        with open(filename, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                rows.append(row)
    except OSError as e:
        print(f"Error: Unable to open {filename} - {e}")
        raise
    return rows

# this function takes in an array input which is of type list and outputs cyz 
def remove_duplicates(array_input):
    unique_rows = []
    user_ids = []

    for row in array_input:
        user_id = row[0]
        if user_id not in user_ids:
            user_ids.append(user_id)
            unique_rows.append(row)
    return unique_rows

def remove_empty_lines(array_input2):
    clean_list = []

    for sublist in array_input2:
        for element in sublist:
            if element != "":
                clean_list.append(sublist)
                break
    return clean_list

def capitalize_names(headers, data):
    first_name_index = headers.index('first_name')
    last_name_index = headers.index('last_name')

    for entry in data:
        entry[first_name_index] = entry[first_name_index].capitalize()
        entry[last_name_index] = entry[last_name_index].capitalize()

    return data

def capitalize_user_names(filename):
    header = filename[0]
    first_name_index = header.index('first_name')
    last_name_index = header.index('last_name')

    for row in filename[1:]:
        if row[first_name_index]:
            row[first_name_index] = row[first_name_index].capitalize()
        if row[last_name_index]:
            row[last_name_index] = row[last_name_index].capitalize()
    return filename