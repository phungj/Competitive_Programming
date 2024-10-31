-- Part 1

data Heading = North | East | South | West

advance :: Heading -> Int -> (Int, Int) -> (Int, Int)

advance North distance currentPosition = (fst currentPosition, snd currentPosition + distance)
advance East distance currentPosition = (fst currentPosition + distance, snd currentPosition)
advance South distance currentPosition = (fst currentPosition, snd currentPosition - distance)
advance West distance currentPosition = (fst currentPosition - distance, snd currentPosition)

turn :: Heading -> Char -> Heading

turn North 'L' = West
turn North 'R' = East
turn East 'L' = North
turn East 'R' = South
turn South 'L' = East
turn South 'R' = West
turn West 'L' = South
turn West 'R' = North

followDirections :: [String] -> Heading -> (Int, Int) -> (Int, Int)

followDirections ((currentTurn:currentDistance):rest) currentHeading currentPosition = followDirections rest newHeading (advance newHeading (read currentDistance :: Int) currentPosition)
    where newHeading = turn currentHeading currentTurn

followDirections _ _ currentPosition = currentPosition

-- Part 2

intersect :: (Eq a) => [a] -> [a] -> [a]

intersect [] = const []
intersect xs = filter (`elem` xs)

advanceWithSteps :: Heading -> Int -> (Int, Int) -> ((Int, Int), [(Int, Int)])

advanceWithSteps North distance currentPosition = ((fst currentPosition, snd currentPosition + distance), [(fst currentPosition, y) | y <- [snd currentPosition + 1..snd currentPosition + distance]])
advanceWithSteps East distance currentPosition = ((fst currentPosition + distance, snd currentPosition), [(x, snd currentPosition) | x <- [fst currentPosition + 1..fst currentPosition + distance]])
advanceWithSteps South distance currentPosition = ((fst currentPosition, snd currentPosition - distance), [(fst currentPosition, y) | y <- [snd currentPosition - distance..snd currentPosition - 1]])
advanceWithSteps West distance currentPosition = ((fst currentPosition - distance, snd currentPosition), [(x, snd currentPosition) | x <- [fst currentPosition - distance..fst currentPosition - 1]])

findLocationVisitedTwice :: [String] -> Heading -> (Int, Int) -> [(Int, Int)] -> (Int, Int)

findLocationVisitedTwice ((currentTurn:currentDistance):rest) currentHeading currentPosition visited
    | not (null intersection) = head intersection
    | otherwise = findLocationVisitedTwice rest newHeading newPosition (visitedPositions ++ visited)
        where newHeading = turn currentHeading currentTurn
              distance = read currentDistance :: Int
              advanceResult = advanceWithSteps newHeading distance currentPosition
              newPosition = fst advanceResult
              visitedPositions = snd advanceResult
              intersection = visitedPositions `intersect` visited