-- Part 1

findMinimumUnblockedIP :: [[Int]] -> Int

findMinimumUnblockedIP ([low1, high1]:[low2, high2]:rest)
    | high1 + 1 < low2 = high1 + 1
    | otherwise = findMinimumUnblockedIP ([low2, high2]:rest)

findMinimumUnblockedIP ([low, high]:rest) = high + 1
findMinimumUnblockedIP _ = -1

-- Part 2

mergeRanges :: [[Int]] -> [[Int]] -> [[Int]]

mergeRanges ([low1, high1]:[low2, high2]:rest) ips
    | high1 + 1 >= low2 && high1 > high2 = mergeRanges ([low1, high1]:rest) ips
    | high1 + 1 >= low2 = mergeRanges ([low1, high2]:rest) ips
    | otherwise = [low1, high1]:ips ++ mergeRanges ([low2, high2]:rest) ips

mergeRanges ([low, high]:rest) ips = [low, high]:ips
mergeRanges _ ips = ips

countBlockedIPs :: [[Int]] -> Int

countBlockedIPs ([low, high]:rest) = (high - low + 1) + countBlockedIPs rest
countBlockedIPs _ = 0