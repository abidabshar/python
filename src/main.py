usernames1=input("give the input: - ")
usernames2=input("give the input: - ")
usernames=[usernames1, usernames2]
if usernames:
  for username in usernames:
    print (f"Hello {username}")
else:
    print ("We need to find some users.")