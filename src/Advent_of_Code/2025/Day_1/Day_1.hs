parse_safe_instructions :: Int -> Int -> [(Char, Int)] -> Int
parse_safe_instructions zero_count dial_position ((direction, rotation_count):instructions)
    | direction == 'L' && (dial_position - rotation_count) `mod` 100 == 0 = parse_safe_instructions (zero_count + 1) 0 instructions
    | direction == 'R' && (dial_position + rotation_count) `mod` 100 == 0 = parse_safe_instructions (zero_count + 1) 0 instructions
    | direction == 'L' = parse_safe_instructions zero_count ((dial_position - rotation_count) `mod` 100) instructions
    | direction == 'R' = parse_safe_instructions zero_count ((dial_position + rotation_count) `mod` 100) instructions

parse_safe_instructions zero_count dial_position ((direction, rotation_count):instructions)
    | direction == 'L' && dial_position /= 0 && (dial_position - (rotation_count `mod` 100)) <= 0 = parse_safe_instructions (zero_count + 1 + (rotation_count `div` 100)) ((dial_position - rotation_count) `mod` 100) instructions
    | direction == 'R' && dial_position /= 0 && (dial_position + (rotation_count `mod` 100)) >= 100 = parse_safe_instructions (zero_count + 1 + (rotation_count `div` 100)) ((dial_position + rotation_count) `mod` 100) instructions
    | direction == 'L' = parse_safe_instructions (zero_count + (rotation_count `div` 100)) ((dial_position - rotation_count) `mod` 100) instructions
    | direction == 'R' = parse_safe_instructions (zero_count + (rotation_count `div` 100)) ((dial_position + rotation_count) `mod` 100) instructions

parse_safe_instructions zero_count _ [] = zero_count