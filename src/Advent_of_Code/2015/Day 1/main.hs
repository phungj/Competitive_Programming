calc_floor :: String -> Integer

calc_floor ('(':rest) = 1 + calc_floor rest
calc_floor (')':rest) = (-1) + calc_floor rest
calc_floor [] = 0

find_first_basement_floor :: String -> Integer -> Integer -> Integer

find_first_basement_floor _ (-1) string_pos = string_pos
find_first_basement_floor ('(':rest) cur_floor string_pos = find_first_basement_floor rest (1 + cur_floor) (1 + string_pos)
find_first_basement_floor (')':rest) cur_floor string_pos = find_first_basement_floor rest ((-1) + cur_floor) (1 + string_pos)
