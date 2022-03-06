

# def format_address(address_string):
#   # Declare variables
#     house = ""
#     number = ""
#   # Separate the address string into parts
#     lista = address_string.split(" ", 1)
#   # Traverse through the address parts
#     for seccion in lista:
#     # Determine if the address part is the
#     # house number or part of the street name
#         if seccion.isdigit():
#             number = seccion
#         else:
#             direccion = seccion
#   # Does anything else need to be done 
#   # before returning the result?
  
#   # Return the formatted string  
#     return "house number {} on street named {}".format(number, direccion)

# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"

# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"

# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"



# def highlight_word(sentence, word):
#     miniscula = sentence.replace(word ,word.upper())

#     return miniscula
#     # return(sentence.replace(miniscula, miniscula.upper()))

# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


# def combine_lists(list1, list2):
#   # Generate a new list containing the elements of list2
#   # Followed by the elements of list1 in reverse order
#     list2.reverse()

#     # print (list1 + list2.reverse())
#     return  list1 + list2


	
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

# print(combine_lists(Jamies_list, Drews_list))

# def squares(start, end):
#     squares = [value ** 2 for value in range(start,end+1)]
#     return squares

# print(squares(2, 3)) # Should be [4, 9]
# print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# def car_listing(car_prices):
#     result = ""
#     for prop,value in car_prices.items():
      
#         result += "{} costs {} dollars".format(prop, value) + "\n"
#     return result

# print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))



# def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed 
    # only once, and the value from guests1 taking precedence
    
    # final_list = {}
    # for friend in guests1:
    #     if friend in guests2:
    #         final_list[friend] =guests1[friend] + guests2[friend]
    #     else:
    #         final_list[friend] = guests1[friend]
    
    # for friends in guests2:
    #     if not friends in final_list:
    #         final_list[friends] = guests2[friends]
        

    # return final_list

# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

# print(combine_guests(Rorys_guests, Taylors_guests))

# animal = "Hippopotamus"

# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])

# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)


# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# print(host_addresses.keys())


def combine_guests(guests1, guests2):
    #Update function will add new values and update existing values in the dictionary
    guests2.update(guests1)
    return guests2

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, 
"Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, 
"Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))