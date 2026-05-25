import camelcase  # Keep this as camelcase, NOT test!

# Create a camelcase object
c = camelcase.CamelCase()

# Define a sentence
txt = "hello world, this is a test"

# Convert it
print(c.hump(txt))