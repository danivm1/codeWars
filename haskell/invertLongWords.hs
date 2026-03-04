kata :: String -> String
kata x = unwords $ inverte (words x)

inverte :: [String] -> [String]
inverte [] = []
inverte (x:xs)
    | length x >= 5 = foldl (flip (:)) [] x : inverte xs
    | otherwise = x : inverte xs
