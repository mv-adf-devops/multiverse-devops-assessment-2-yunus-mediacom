import sys
from extract import read_csv, remove_duplicates

def main():
    filename="results.csv"
    # print(read_csv(filename))
    input = read_csv(filename)
    input_deduped = remove_duplicates(input) 
    print(input_deduped)

if __name__ == "__main__":
    sys.exit(main())