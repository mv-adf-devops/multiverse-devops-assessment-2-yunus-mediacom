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


def validate_answer_3(data):
    valid_data = [data[0]]

    for entry in data:
        # Extract 'answer_3' and attempt to convert it to an integer
        try:
            answer_3 = int(entry[5])
            if 1 <= answer_3 <= 10:
                valid_data.append(entry)

        except (ValueError, IndexError):
            # Skip the entry if conversion fails or if index is out of range
            continue

        # Check if answer_3 is between 1 and 10


    return valid_data


def output_to_file(output_filename, data):
    print("Writing to file:", output_filename)
    with open(output_filename, "w", encoding="UTF8", newline="\n") as f:
        writer = csv.writer(f)
        writer.writerows(data)
