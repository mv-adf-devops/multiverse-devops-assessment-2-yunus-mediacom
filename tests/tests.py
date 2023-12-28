from extract import read_csv, remove_duplicates
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
