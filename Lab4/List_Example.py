shopping_list = ["Tuna", "Rice", "Beans"]
shopping_list.append("Apples")
shopping_list.append("Bananas")
shopping_list.append("Milk")
shopping_list.append("Eggs")
shopping_list.append("Bread")
shopping_list.append(42)
print("Shopping list:", shopping_list)

shopping_list.remove("Milk")
print("Updated shopping list:", shopping_list)

shopping_list.pop()
print("Final shopping list:", shopping_list)