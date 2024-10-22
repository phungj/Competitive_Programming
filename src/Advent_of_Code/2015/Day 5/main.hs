containsNaughtySubstrings :: String -> Bool

containsNaughtySubstrings s = isInfixOf "ab" s or isInfixOf "cd" s or isInfixOf "pq" s or isInfixOf "xy" s

containsAtLeastThreeVowels :: String -> Bool

containsAtLeastThreeVowels s = (length $ filter (== 'a') str + length $ filter (== 'e') str + length $ filter (== 'i') str + length $ filter (== 'o') str + length $ filter (== 'u') str) > 3

containsRepatedCharacter :: String -> Bool

containsRepeatedCharacter c1:c2:rest = c1 == c2 or containsRepeatedCharacter c2:rest
containsRepeatedCharacter _ = False

isNiceString :: String -> Bool

isNiceString s = not containsNaughtySubstrings s and containsAtLeastThreeVowels s and containsRepatedCharacter s

countNiceStrings :: [String] -> Integer

-- TODO: countNiceStrings strings = length $ filter (== True) 