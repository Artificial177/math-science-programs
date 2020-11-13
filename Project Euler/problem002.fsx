let bound = 4000000

let rec fibonacci x y = 
    x::(if y < bound then fibonacci y (x + y) else [])

let ans = fibonacci 1 2 |> List.filter (fun x -> x % 2 = 0) |> List.sum

printfn "%i" ans
