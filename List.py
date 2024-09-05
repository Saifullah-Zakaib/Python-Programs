shopping_list={"apple":"2kg","chicken":1,"onion":"2kg"}
for i in range(3):
    item=input("Enter item: ")
    quantity=input("Enter quantity: ")
    shopping_list[item]=quantity # The Item will be updated if it exists otherwise it will be added in thr dictionary
print("Shopping list:",shopping_list)
