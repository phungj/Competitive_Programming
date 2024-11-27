import Data.List

computeChecksum :: [[Int]] -> Int -> Int

-- Part 1

computeChecksum (row:rest) sum = computeChecksum rest (maximum row - minimum row + sum)
computeChecksum _ sum = sum

-- Part 2

checkDivisiblePairs :: [Int] -> Int -> Int -> Int

checkDivisiblePairs row i j
    | i >= length row = error (show row)
    | j >= length row = checkDivisiblePairs row (i + 1) (i + 2)
    | secondElement `mod` firstElement == 0 = secondElement `div` firstElement
    | otherwise = checkDivisiblePairs row i (j + 1)
    where firstElement = row!!i
          secondElement = row!!j

computeChecksum2 :: [[Int]] -> Int -> Int

computeChecksum2 (row:rest) sum = computeChecksum2 rest (sum + checkDivisiblePairs row 0 1)
computeChecksum2 _ sum = sum