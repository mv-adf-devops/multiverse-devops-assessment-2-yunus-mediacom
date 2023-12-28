from extract import read_csv, remove_duplicates, remove_empty_lines, capitalize_user_names, validate_answer_3, output_to_file
import pytest 
import os
import csv

# Test that file is read into as a list
def test__is_list():
    # Arrange
    filename = 'results.csv'
    expected_type = list
    # Act
    output = read_csv(filename)
    # Assert
    assert type(output) == expected_type

# Test that file exists
    
def verify_remove_duplicates():
    # Prepare
    sample_data = [
        [4, "Harding", "Estrada", "no", 14],
        [5, "India", "Gentry", "yes", 7],
        [6, "Abra", "Sheppard", "yes", 6],
        [6, "Abra", "Sheppard", "no", 8]
    ]
    # Execute
    unique_entries = remove_duplicates(sample_data)
    # Validate
    expected_output = [
        [4, "Harding", "Estrada", "no", 14],
        [5, "India", "Gentry", "yes", 7],
        [6, "Abra", "Sheppard", "yes", 6]
    ]
    assert unique_entries == expected_output

def test_remove_duplicates_from_csv():
    # Setup
    file_path = 'results.csv'
    csv_content = read_csv(file_path)
    # Action
    deduplicated_content = remove_duplicates(csv_content)
    # Verify
    expected_result = [['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'], ['1', 'Charissa', 'Clark', 'yes', 'c', '7'], ['2', 'richard', 'McKinney', 'yes', 'b', '7'], ['', '', '', '', '', ''], ['3', 'patience', 'reeves', 'yes', 'b', '9'], ['4', 'Harding', 'Estrada', 'no', 'b', '14'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], ['7', 'Bryar', 'cooley', 'yes', 'a', '11'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], ['10', 'Graiden', 'Cannon', 'no', 'b', '13'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'dieter', 'alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]
    assert deduplicated_content == expected_result


def test_remove_empty_lines():
     #Arrange
    test_array = [[4,"Harding","Estrada","no",14],["","","","",],
                  [6,"Abra","Sheppard","yes",6],[6,"Abra","Sheppard","no",8]]
    #Act
    array_deduped = remove_duplicates(test_array)
    array_clean = remove_empty_lines(array_deduped)
    #Assert
    assert array_clean == [[4,"Harding","Estrada","no",14],
                  [6,"Abra","Sheppard","yes",6]]

def test_capitalize_user_names():
    # Example dataset with lowercase names
    filename="results.csv"

    dataset_with_lowercase_names = read_csv(filename)

    # Manually capitalize names to create the expected result
    expected_result = [dataset_with_lowercase_names[0]]  # Copy the header

    for row in dataset_with_lowercase_names[1:]:
        capitalized_row = [row[0]]  # Copy the user_id

        # Capitalize first_name and last_name
        for cell in row[1:3]:
            capitalized_row.append(cell.capitalize() if cell else '')

        # Copy the remaining columns
        capitalized_row.extend(row[3:])
        expected_result.append(capitalized_row)

    # Call the capitalise_user_names function
    result = capitalize_user_names(dataset_with_lowercase_names)

    # Assert that the result matches the expected result
    assert result == expected_result

def test_validate_answer_3():
    # Arrange (Define input data)
    data = [
        [1, 'John', 'Doe', 'yes', 'no', 5],
        [2, 'Jane', 'Smith', 'no', 'yes', 12],
        [3, 'Alice', 'Johnson', 'yes', 'yes', 'invalid'],
        [4, 'Bob', 'Brown', 'no', 'no', 8],
    ]

    # Act (Apply the function to the data)
    result = validate_answer_3(data)
    # print("result",result)

    # Assert (Check if the result contains only valid rows)
    for entry in result:
        assert 1 <= entry[5] <= 10  # Directly access 'answer_3' by index 

def test_output_exists():
    # arrange
    in_file = "results.csv"
    out_file = "results_output_test.csv"
    # act
    in_data = read_csv(in_file)
    output_to_file(out_file,in_data)
    out_data = read_csv(out_file)
    # assert
    assert out_data == in_data