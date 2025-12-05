-- Part 1

mergeRanges :: [[Int]] -> [[Int]]

mergeRanges ([low1, high1]:[low2, high2]:rest)
    | high1 + 1 >= low2 && high1 > high2 = mergeRanges ([low1, high1]:rest)
    | high1 + 1 >= low2 = mergeRanges ([low1, high2]:rest)
    | otherwise = [low1, high1]:mergeRanges ([low2, high2]:rest)

mergeRanges ([low, high]:rest) = [[low, high]]


countFreshIngredients :: [Int] -> [[Int]] -> Int

countFreshIngredients (ingredient:ingredients) freshIngredients
    | isIngredientFresh ingredient freshIngredients = 1 + countFreshIngredients ingredients freshIngredients
    | otherwise = countFreshIngredients ingredients freshIngredients

countFreshIngredients [] _ = 0

isIngredientFresh :: Int -> [[Int]] -> Bool

isIngredientFresh ingredient ([low, high]:freshIngredientRanges)
    | ingredient >= low && ingredient <= high = True
    | otherwise = isIngredientFresh ingredient freshIngredientRanges

isIngredientFresh _ [] = False

-- Part 2

countBlockedIPs :: [[Int]] -> Int

countBlockedIPs ([low, high]:rest) = (high - low + 1) + countBlockedIPs rest
countBlockedIPs _ = 0