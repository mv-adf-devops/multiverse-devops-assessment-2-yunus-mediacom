def get_input(filename):
    try:
        with open(filename, 'r') as file:
            rows = file.readlines()
    except OSError as e:
        print(f"Unable to open {filename}: {e}")
        raise
    return rows