import os
import re

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

valid_count = 0

with open(file_path, 'r') as input:
    all_passports = input.read().split("\n\n")

for i in range(len(all_passports)):
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    current_passport = all_passports[i]
    passport_fields = re.findall("[a-z]{3}[:]", current_passport)

    if "byr:" in passport_fields:
        byr = True

    if "iyr:" in passport_fields:
        iyr = True

    if "eyr:" in passport_fields:
        eyr = True

    if "hgt:" in passport_fields:
        hgt = True

    if "hcl:" in passport_fields:
        hcl = True

    if "ecl:" in passport_fields:
        ecl = True

    if "pid:" in passport_fields:
        pid = True

    fields = [byr, iyr, eyr, hgt, hcl, ecl, pid]

    if all(fields):
        valid_count += 1

print(valid_count)
