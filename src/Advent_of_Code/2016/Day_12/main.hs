data AssembunnyState = AssembunnyState Int Int Int Int deriving Show

runAssembunny :: [[String]] -> Int -> Int -> Int -> Int -> Int -> AssembunnyState

runAssembunny inst ip a b c d
    | ip >= length inst || ip < 0 = AssembunnyState a b c d
    | opcode == "cpy" && arg1 == "a" && arg2 == "a" = runAssembunny inst (ip + 1) a b c d
    | opcode == "cpy" && arg1 == "a" && arg2 == "b" = runAssembunny inst (ip + 1) a a c d
    | opcode == "cpy" && arg1 == "a" && arg2 == "c" = runAssembunny inst (ip + 1) a b a d
    | opcode == "cpy" && arg1 == "a" && arg2 == "d" = runAssembunny inst (ip + 1) a b c a
    | opcode == "cpy" && arg1 == "b" && arg2 == "a" = runAssembunny inst (ip + 1) b b c d
    | opcode == "cpy" && arg1 == "b" && arg2 == "b" = runAssembunny inst (ip + 1) a b c d
    | opcode == "cpy" && arg1 == "b" && arg2 == "c" = runAssembunny inst (ip + 1) a b b d
    | opcode == "cpy" && arg1 == "b" && arg2 == "d" = runAssembunny inst (ip + 1) a b c b
    | opcode == "cpy" && arg1 == "c" && arg2 == "a" = runAssembunny inst (ip + 1) c b c d
    | opcode == "cpy" && arg1 == "c" && arg2 == "b" = runAssembunny inst (ip + 1) a c c d
    | opcode == "cpy" && arg1 == "c" && arg2 == "c" = runAssembunny inst (ip + 1) a b c d
    | opcode == "cpy" && arg1 == "c" && arg2 == "d" = runAssembunny inst (ip + 1) a b c c
    | opcode == "cpy" && arg1 == "d" && arg2 == "a" = runAssembunny inst (ip + 1) d b c d
    | opcode == "cpy" && arg1 == "d" && arg2 == "b" = runAssembunny inst (ip + 1) a d c d
    | opcode == "cpy" && arg1 == "d" && arg2 == "c" = runAssembunny inst (ip + 1) a b d d
    | opcode == "cpy" && arg1 == "d" && arg2 == "d" = runAssembunny inst (ip + 1) a b c d
    | opcode == "cpy" && arg2 == "a" = runAssembunny inst (ip + 1) (read arg1 :: Int) b c d
    | opcode == "cpy" && arg2 == "b" = runAssembunny inst (ip + 1) a (read arg1 :: Int) c d
    | opcode == "cpy" && arg2 == "c" = runAssembunny inst (ip + 1) a b (read arg1 :: Int) d
    | opcode == "cpy" && arg2 == "d" = runAssembunny inst (ip + 1) a b c (read arg1 :: Int)
    | opcode == "inc" && arg1 == "a" = runAssembunny inst (ip + 1) (a + 1) b c d
    | opcode == "inc" && arg1 == "b" = runAssembunny inst (ip + 1) a (b + 1) c d
    | opcode == "inc" && arg1 == "c" = runAssembunny inst (ip + 1) a b (c + 1) d
    | opcode == "inc" && arg1 == "d" = runAssembunny inst (ip + 1) a b c (d + 1)
    | opcode == "dec" && arg1 == "a" = runAssembunny inst (ip + 1) (a - 1) b c d
    | opcode == "dec" && arg1 == "b" = runAssembunny inst (ip + 1) a (b - 1) c d
    | opcode == "dec" && arg1 == "c" = runAssembunny inst (ip + 1) a b (c - 1) d
    | opcode == "dec" && arg1 == "d" = runAssembunny inst (ip + 1) a b c (d - 1)
    | opcode == "jnz" && arg1 == "a" && a /= 0 = runAssembunny inst (ip + read arg2 :: Int) a b c d
    | opcode == "jnz" && arg1 == "b" && b /= 0 = runAssembunny inst (ip + read arg2 :: Int) a b c d
    | opcode == "jnz" && arg1 == "c" && c /= 0 = runAssembunny inst (ip + read arg2 :: Int) a b c d
    | opcode == "jnz" && arg1 == "d" && d /= 0 = runAssembunny inst (ip + read arg2 :: Int) a b c d
    | opcode == "jnz" && arg1 /= "a" && arg1 /= "b" && arg1 /= "c" && arg1 /= "d" && (read arg1 :: Int) /= 0 = runAssembunny inst (ip + read arg2 :: Int) a b c d
    | opcode == "jnz" = runAssembunny inst (ip + 1) a b c d
    where currentInst = inst !! ip
          opcode = head currentInst
          arg1 = currentInst !! 1
          arg2 = last currentInst
