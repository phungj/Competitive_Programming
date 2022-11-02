-- https://stackoverflow.com/a/4981265
wordsWhen     :: (Char -> Bool) -> String -> [String]

wordsWhen p s =  case dropWhile p s of
                      "" -> []
                      s' -> w : wordsWhen p s''
                            where (w, s'') = break p s'

total_area :: [Integer] -> Integer

total_area (l:w:h:rest)
total_area [] = 0