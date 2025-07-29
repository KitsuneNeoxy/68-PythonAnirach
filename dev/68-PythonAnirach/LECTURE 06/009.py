animals = ["cat", "dog", "rabbit", "hamster", "dog", "parrot"]
first_dog_index = animals.index("dog")
print(f'The first occurence of dog in at index: {first_dog_index}')

secon_dog_index = animals.index("dog",first_dog_index)
print(f"The second occurence of 'dog' is at index: {secon_dog_index}")