import os
import re

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

valid_count = 0

with open(file_path, 'r') as input:
    all_passports = input.read().split("\n\n")


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


for i in range(len(all_passports)):
    byr = False
    iyr = False
    eyr = False
    hgt = False
    hcl = False
    ecl = False
    pid = False

    current_passport = all_passports[i]
    passport_fields = re.findall("[a-z]{3}[:]#?[0-z]*", current_passport)
    split_passport_fields = []
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for j in range(len(passport_fields)):
        split_passport_fields.append(passport_fields[j].split(":"))

    split_passport_fields = [k for sub in split_passport_fields for k in sub]

    if "byr" in split_passport_fields:
        field_index = split_passport_fields.index("byr")
        birth_year = int(split_passport_fields[field_index + 1])

        if not (birth_year < 1920 or birth_year > 2002):
            byr = True

    if "iyr" in split_passport_fields:
        field_index = split_passport_fields.index("iyr")
        issue_year = int(split_passport_fields[field_index + 1])

        if not (issue_year < 2010 or issue_year > 2020):
            iyr = True

    if "eyr" in split_passport_fields:
        field_index = split_passport_fields.index("eyr")
        expiry_year = int(split_passport_fields[field_index + 1])

        if not (expiry_year < 2020 or expiry_year > 2030):
            eyr = True

    if "hgt" in split_passport_fields:
        field_index = split_passport_fields.index("hgt")
        unit = split_passport_fields[field_index + 1][-2:]

        if unit == "cm" or unit == "in":
            split_passport_fields[field_index + 1] = split_passport_fields[field_index + 1][:-2]
            num = int(split_passport_fields[field_index + 1])

            if unit == "cm" and not (num < 150 or num > 193):
                hgt = True

            elif unit == "in" and not (num < 59 or num > 76):
                hgt = True

    if "hcl" in split_passport_fields:
        field_index = split_passport_fields.index("hcl")
        hair_color = split_passport_fields[field_index + 1]

        if re.search("#[0-9,a-f]{0,6}", hair_color):
            hcl = True

    if "ecl" in split_passport_fields:
        field_index = split_passport_fields.index("ecl")
        eye_color = split_passport_fields[field_index + 1]

        if eye_color in eye_colors:
            ecl = True

    if "pid" in split_passport_fields:
        field_index = split_passport_fields.index("pid")
        passport_id = split_passport_fields[field_index + 1]

        if len(passport_id) == 9 and represents_int(passport_id):
            pid = True

    fields = [byr, iyr, eyr, hgt, hcl, ecl, pid]

    if all(fields):
        valid_count += 1

print(valid_count)
