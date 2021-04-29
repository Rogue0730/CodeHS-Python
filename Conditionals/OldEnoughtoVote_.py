age = int(input("How old are you?: "))
age_requirement = 19

able_to_vote = age >= age_requirement

if able_to_vote:
    print("old enough to vote")
else:
    print("not old enough to vote")