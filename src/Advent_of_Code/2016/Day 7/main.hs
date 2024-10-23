import Data.List as L
import Data.Maybe as M
import Debug.Trace as T

-- Part 1

substring :: Int -> Int -> String -> String
substring i j s = L.take (j-i) ( L.drop i s )

hasABBA :: String -> Bool

hasABBA (a1:b1:b2:a2:s) = (a1 == a2 && b1 == b2 && a1 /= b1) || hasABBA (b1:b2:a2:s)
hasABBA _ = False

hasABBAInBrackets :: String -> Bool

hasABBAInBrackets ('[':rest) = hasABBA (substring 0 (M.fromJust (L.elemIndex ']' rest)) rest) || hasABBAInBrackets rest
hasABBAInBrackets (c:rest) = hasABBAInBrackets rest
hasABBAInBrackets _ = False

supportsTLS :: String -> Bool

supportsTLS s = hasABBA s && not (hasABBAInBrackets s)

-- Part 2

findFirstABA :: String -> Maybe String

findFirstABA (a1:b1:a2:s) 
    | a1 == a2 && a1 /= b1 = Just [a1, b1, a2]
    | otherwise = findFirstABA (b1:a2:s)

findFirstABA _ = Nothing

hasOppositeABA :: String -> String -> Bool

hasOppositeABA (a1:b1:a2) (c1:d1:c2:s) = (a1 == d1 && b1 == c1 && c1 == c2) || hasOppositeABA (a1:b1:a2) (d1:c2:s)
hasOppositeABA _ _ = False

hasOppositeABAInBrackets :: String -> String -> Bool

hasOppositeABAInBrackets (a1:b1:a2) ('[':rest) = hasOppositeABA (a1:b1:a2) (substring 0 (M.fromJust (L.elemIndex ']' rest)) rest) || hasOppositeABAInBrackets (a1:b1:a2) rest
hasOppositeABAInBrackets (a1:b1:a2) (c:rest) = hasOppositeABAInBrackets (a1:b1:a2) rest
hasOppositeABAInBrackets _ _ = False

supportsSSL :: String -> Bool

supportsSSL s = supportsSSLHelper (removeBracketedSubstrings s) s

removeBracketedSubstrings :: String -> String

removeBracketedSubstrings s
    | M.isJust leftBracketIndex = substring 0 (M.fromJust leftBracketIndex) s ++ removeBracketedSubstrings (substring (M.fromJust rightBracketIndex + 1) (length s) s)
    | otherwise = s
    where leftBracketIndex = L.elemIndex '[' s
          rightBracketIndex = L.elemIndex ']' s

supportsSSLHelper :: String -> String -> Bool

supportsSSLHelper (c:s) sOriginal
    | M.isNothing firstABA = False
    | M.isJust firstABA && hasOppositeABAInBrackets (M.fromJust firstABA) sOriginal = True
    | otherwise = supportsSSLHelper s sOriginal
    where firstABA = findFirstABA (c:s)