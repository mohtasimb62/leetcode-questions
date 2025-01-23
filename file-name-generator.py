def transform_string(input_string: str) -> str:
    lowercased = input_string.lower()
    no_periods = lowercased.replace(".", "")
    hyphenated = no_periods.replace(" ", "-")
    return hyphenated+".py"

input_string = "1011. Capacity To Ship Packages Within D Days"
result = transform_string(input_string)
print(result)
