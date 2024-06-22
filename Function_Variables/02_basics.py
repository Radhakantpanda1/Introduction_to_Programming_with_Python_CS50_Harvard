user_name=input("Enter your name-")
# remove whitespace from beginning and ending

# methods in python
user_name=user_name.strip()
print("Hello,",user_name)
user_name=user_name.capitalize()
print("Hello,",user_name)
user_name=user_name.title()
print("Hello,",user_name)

user_name=user_name.strip().title()
print("Hello,",user_name)

print("******************************")

# improving code readability

user_id=input("Enter your user Id-").strip().capitalize()
# We can combine as many as functions we want , but after certain point it will look bad and difficult to understand
print(user_id)
