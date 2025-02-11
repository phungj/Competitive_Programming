-- Part 1

findMinimumUnblockedIP :: [[Int]] -> Int

findMinimumUnblockedIP ([low1, high1]:[low2, high2]:rest)
    | high1 + 1 < low2 = high1 + 1
    | otherwise = findMinimumUnblockedIP ([low2, high2]:rest)

findMinimumUnblockedIP ([low, high]:rest) = high + 1
findMinimumUnblockedIP _ = -1

-- Part 2

mergeRanges :: [[Int]] -> [[Int]]

mergeRanges ([low1, high1]:[low2, high2]:rest)
    | high1 + 1 >= low2 && high1 > high2 = mergeRanges ([low1, high1]:rest)
    | high1 + 1 >= low2 = mergeRanges ([low1, high2]:rest)
    | otherwise = [low1, high1]:mergeRanges ([low2, high2]:rest)

mergeRanges ([low, high]:rest) = [[low, high]]

countBlockedIPs :: [[Int]] -> Int

countBlockedIPs ([low, high]:rest) = (high - low + 1) + countBlockedIPs rest
countBlockedIPs _ = 0