def run():
    # my_list = [1, "hello", True, 4.5]
    # my_dict = {"firstname", "Mirna", "lastname", "Ampuero"}

    super_list= [
        {"firstname": "Mirna", "lastname": "Ampuero"},
        {"firstname": "Maria", "lastname": "Hernandez"},
        {"firstname": "Juana", "lastname": "Arco"},
        {"firstname": "Jose", "lastname": "Ramirez"},
        {"firstname": "Luz", "lastname": "Salas"},
    ]

    # super_dict = {
    #     "natural_nums": [1,2,3,4,5],
    #     "integer_nums": [-1,-2,0,1,2],
    #     "floating_nums": [1.1,2.3, 4.5],
        
    # }

    # for key, value in super_dict.items():
    #     print(key, "-", value)

    
    
    for i in super_list:
            print("Su nombre completo es: ", i["firstname"],  i["lastname"])                

if __name__ == "__main__":
    run()