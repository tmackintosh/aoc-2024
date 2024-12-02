with open('day2.txt', 'r') as file:
    reports = [list(map(int, line.split())) for line in file]

def validate_list(l):
    asc = all(l[i] < l[i + 1] for i in range(len(l) - 1))
    desc = all(l[i] > l[i + 1] for i in range(len(l) - 1))
    diff = all(abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1))
    return (asc or desc) and diff

print('valid reports:', sum(validate_list(l) for l in reports))

def dampen_valid_list(l):
    return any(validate_list(l[:i] + l[i+1:]) for i in range(len(l)))

print('dampened valid reports:', sum(validate_list(levels) or dampen_valid_list(levels) for levels in reports))