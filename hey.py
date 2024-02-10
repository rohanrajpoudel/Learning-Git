def to_camel_case(name):
    words = name.split()
    camel_case_name = words[0].lower()
    
    for word in words[1:]:
        camel_case_name += word.capitalize()
    
    return camel_case_name

name = input("Enter your name: ")
camel_case_name = to_camel_case(name)
print("Your name in camel case is:", camel_case_name)
