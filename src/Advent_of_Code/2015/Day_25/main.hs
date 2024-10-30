pairingFunction :: Int -> Int -> Int

pairingFunction c r = (((c + r - 2) * (c + r - 1)) `div` 2) + c

r :: Int

r = 2978

c :: Int

c = 3083

targetIndex :: Int

targetIndex = pairingFunction c r

multiplicand :: Integer

multiplicand = 252533

modulus :: Integer

modulus = 33554393

findTargetCode :: Int -> Int -> Integer -> Integer

findTargetCode currentIndex targetIndex currentCode = (((multiplicand ^ (targetIndex - currentIndex)) `mod` modulus) * currentCode) `mod` modulus

