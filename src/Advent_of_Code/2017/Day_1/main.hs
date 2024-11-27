import Data.Char (digitToInt)

-- Part 1

solveCaptcha :: String -> Int -> Int

solveCaptcha (a:b:rest) sum
    | a == b = solveCaptcha (b:rest) (digitToInt a + sum)
    | otherwise = solveCaptcha (b:rest) sum

solveCaptcha _ sum = sum

-- Part 2

solveCaptcha2 :: String -> Int -> Int -> Int

solveCaptcha2 input i sum
    | i >= inputLength = sum
    | currentChar == input!!(i + (inputLength `div` 2)) = solveCaptcha2 input (i + 1) (digitToInt currentChar + sum)
    | otherwise = solveCaptcha2 input (i + 1) sum
    where inputLength = length input `div` 2
          currentChar = input!!i

