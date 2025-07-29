fruits_with_dupliactes = ["apple", "banana", "apple", "cherry","apple","kivi"]
while "apple" in fruits_with_dupliactes:
    fruits_with_dupliactes.remove("apple")
print(f'Fruits after remove : {fruits_with_dupliactes}')