def retrieve_positive_num():
  num = int(input("Enter a positive number: "))
  while True:
    try:
      if num < 0:
        print("Invald entry")
        num = int(input("Enter a positive number: "))
    except ValueError:
      print("invald entry")
      num = int(input("Enter a positive number: "))
    if num >= 0:
      return(num)
        
print(retrieve_positive_num())