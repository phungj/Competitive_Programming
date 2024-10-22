-- Part 1

-- import Data.List as L

-- containsNaughtySubstrings :: String -> Bool

-- containsNaughtySubstrings s = L.isInfixOf "ab" s || L.isInfixOf "cd" s || L.isInfixOf "pq" s || L.isInfixOf "xy" s

-- containsAtLeastThreeVowels :: String -> Bool

-- containsAtLeastThreeVowels s = length (filter (== 'a') s) + length (filter (== 'e') s) + length (filter (== 'i') s) + length (filter (== 'o') s) + length (filter (== 'u') s) >= 3

-- containsRepeatedCharacter :: String -> Bool

-- containsRepeatedCharacter (c1:c2:rest) = c1 == c2 || containsRepeatedCharacter (c2:rest)
-- containsRepeatedCharacter _ = False

-- isNiceString :: String -> Bool

-- isNiceString s = not (containsNaughtySubstrings s) && containsAtLeastThreeVowels s && containsRepeatedCharacter s

countNiceStrings :: [String] -> Int

countNiceStrings strings = length $ filter id (map isNiceString strings)

generateInputString :: String -> String

generateInputString (c1:c2:c3:c4:c5:c6:c7:c8:c9:c10:c11:c12:c13:c14:c15:c16:rest) = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16, '\n'] ++ generateInputString rest
generateInputString [] = ""

-- Part 2

searchForRepeatedCharacterPair :: Char -> Char -> String -> Bool

searchForRepeatedCharacterPair t1 t2 (c1:c2:s) = t1 == c1 && t2 == c2 || searchForRepeatedCharacterPair t1 t2 (c2:s)
searchForRepeatedCharacterPair _ _ _ = False

containsRepeatedCharacterPair :: String -> Bool

containsRepeatedCharacterPair (c1:c2:s) = searchForRepeatedCharacterPair c1 c2 s || containsRepeatedCharacterPair (c2:s)
containsRepeatedCharacterPair _ = False

containsOneRepeatingLetterWithGap :: String -> Bool

containsOneRepeatingLetterWithGap (c1:c2:c3:s) = c1 == c3 || containsOneRepeatingLetterWithGap (c2:c3:s)
containsOneRepeatingLetterWithGap _ = False

isNiceString :: String -> Bool

isNiceString s = containsRepeatedCharacterPair s && containsOneRepeatingLetterWithGap s