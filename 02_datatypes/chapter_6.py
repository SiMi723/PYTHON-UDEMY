chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:8:2]}")
print(f"Last word: {chai_description[12:]}")
print(f"Last word: {chai_description[::-1]}") #reverse a string

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")