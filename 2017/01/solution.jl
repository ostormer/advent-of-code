in_string = read(open("2017/01/in.txt", "r"), String)

nums = [parse(Int64, c) for c in in_string]
println(nums)