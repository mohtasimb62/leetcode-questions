def format_string(input_string):
    lowercased = input_string.lower()
    formatted = lowercased.replace(" ", "-").replace(".", "-")
    return formatted

input_string = "1283. Find the Smallest Divisor Given a Threshold"
output = format_string(input_string)
print(output)
