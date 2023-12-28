from extract import *

def main():
    print("Inside main function")
    filename = 'results.csv'
    input_data = read_csv(filename)
    input_headers = input_data[0]  # Assuming the headers are in the first row
    input_deduped = remove_duplicates(input_data)
    removed_blanks = remove_empty_lines(input_deduped)
    capitalised_names = capitalize_names(input_headers, removed_blanks)
    valid_ans_3 = validate_answer_3(capitalised_names)
    output_to_file("clean_results.csv", valid_ans_3)

if __name__ == '__main__':
    main()