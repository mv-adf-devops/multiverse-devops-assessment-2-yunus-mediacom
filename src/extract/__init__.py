def read_csv(filename):
    rows = []
    with open(filename, 'r') as f:
        for line in f.readline():
            rows.append(line.strip().split(','))
    return rows
