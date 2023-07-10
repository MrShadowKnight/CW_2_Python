import json
# name = input("Vvedit imia uchnya: ")
# age = input("Vvedit vik uchnya: ")

# frame_student = {
#     "name": name,
#     "age": age
# }

# with open("students_data.json", "r") as file:
#     students = json.load(file)
#     students.append(frame_student)

# with open("students_data.json", "w") as f:
#     json.dump(students, f)

# 
new_product = {
    "id": 21,
    "title": "Lorem ipsum dolor sit amet",
    "price": 50.99,
    "description": "95%Cotton,5%Spandex, Features: Casual, Short Sleeve, Letter Print,V-Neck,Fashion Tees, The fabric is soft and has some stretch., Occasion: Casual/Office/Beach/School/Home/Street. Season: Spring,Summer,Autumn,Winter.",
    "category": "Lorem ipsum",
    "image": "https://www.lipsum.com/",
    "rating": {
        "rate": 4.9,
        "count": 999
    }
}


with open("products.json", "r") as file:
    products = json.load(file)

    max_rating = 1
    min_rating = 100
    for product in products:
        rating = product['rating']['rate']

        if rating < min_rating:
            min_rating = rating

        if rating > max_rating:
            max_rating = rating

    print("Max reting: ", max_rating)
    print("Min reting: ", min_rating)

products.append(new_product)
with open("products.json", "w") as file:
    json.dump(products, file)

# id_choice = int(input("Vvedit id produktu, dlya vydalenia: "))
# title_choice = input("Vvedit nasvu produktu: ")

# fram = {
#     "id": id_choice,
#     "title": title_choice
# }
# with open("products.json", "r") as file:
#     products = json.load(file)
#     for i in products:
#         id = i['id']
#         title = i['title']
#         if id == id_choice and title == title_choice:
            
#     with open("products.json", "w") as file:
#         json.dump(products, file)
