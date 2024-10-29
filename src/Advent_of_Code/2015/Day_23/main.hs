data TuringState = TuringState Int Int deriving Show

runTuringAsm :: [[String]] -> Int -> Int -> Int -> TuringState

runTuringAsm inst ip a b
    | ip >= length inst || ip < 0 = TuringState a b
    | opcode == "hlf" && arg1 == "a" = runTuringAsm inst (ip + 1) (a `div` 2) b
    | opcode == "hlf" && arg1 == "b" = runTuringAsm inst (ip + 1) a (b `div` 2)
    | opcode == "tpl" && arg1 == "a" = runTuringAsm inst (ip + 1) (a * 3) b
    | opcode == "tpl" && arg1 == "b" = runTuringAsm inst (ip + 1) a (b * 3)
    | opcode == "inc" && arg1 == "a" = runTuringAsm inst (ip + 1) (a + 1) b
    | opcode == "inc" && arg1 == "b" = runTuringAsm inst (ip + 1) a (b + 1)
    | opcode == "jmp" = runTuringAsm inst (ip + read arg1 :: Int) a b
    | opcode == "jie" && arg1 == "a" && even a = runTuringAsm inst (ip + read arg2 :: Int) a b 
    | opcode == "jie" && arg1 == "b" && even b = runTuringAsm inst (ip + read arg2 :: Int) a b 
    | opcode == "jie" = runTuringAsm inst (ip + 1) a b
    | opcode == "jio" && arg1 == "a" && a == 1 = runTuringAsm inst (ip + read arg2 :: Int) a b 
    | opcode == "jio" && arg1 == "b" && b == 1 = runTuringAsm inst (ip + read arg2 :: Int) a b 
    | opcode == "jio" = runTuringAsm inst (ip + 1) a b
    where currentInst = inst!!ip
          opcode =  head currentInst
          arg1 = currentInst!!1
          arg2 = last currentInst