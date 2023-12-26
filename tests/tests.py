from extract import read_csv

def test_file_read_into_list():
    filename = "results.csv"
    # expected_output = list

    output = read_csv(filename)

    assert len(output) > 0

def test_first_row_is_correct():
    filename = "results.csv"
    expected_output = list

    output = read_csv(filename)