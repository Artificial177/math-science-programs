// Just a fun implementation in F#.
let mutable num = 0
let range = [0..999]

for i in range do
 if (i % 3 = 0) || (i % 5 = 0) then
  num <- i + num

printfn "%A" num
