marks = {
    "Rakesh": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Rakesh"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Rakesh": 99, "Shivam": 100})
# print(marks)

print(marks.get("Rakesh1")) # Prints None
print(marks["Rakesh1"]) # Returns an error