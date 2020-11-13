let divisiblebynums x = [1..20] |> List.forall (fun n -> x % n = 0)

let result = Seq.initInfinite (fun x -> x + 1) |> Seq.map((*) 20) |> Seq.filter divisiblebynums |> Seq.head

printfn "%i" result
