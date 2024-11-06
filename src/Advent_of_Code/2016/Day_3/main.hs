-- Part 1

isValidTriangle :: [Int] -> Bool

isValidTriangle [a, b, c] = (a + b) > c

-- Part 2

-- Taken from https://stackoverflow.com/a/2028218
every :: Int -> [a] -> [a]

every n xs = case drop (n-1) xs of
              y : ys -> y : every n ys
              [] -> []

countValidTriangles :: [Int] -> Int

countValidTriangles (a:b:c:rest)
    | (a + b) > c && (b + c) > a && (a + c) > b = 1 + countValidTriangles rest
    | otherwise = countValidTriangles rest

countValidTriangles _ = 0