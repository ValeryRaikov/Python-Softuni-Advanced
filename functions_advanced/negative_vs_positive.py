def compare_nums(positive, negative):
    print(sum(negative))
    print(sum(positive))
    
    if sum(positive) > abs(sum(negative)):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")
    
    
numbers = [int(x) for x in input().split()]
positive_nums = [x for x in numbers if x > 0]
negative_nums = [x for x in numbers if x < 0]

compare_nums(positive_nums, negative_nums)