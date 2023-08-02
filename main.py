import importlib.util

# Store the file path in a variable
second_file = 'file2.py'

# Create a module specification from the file path
spec = importlib.util.spec_from_file_location('data', second_file)

# Create a new module based on the specification
data_module = importlib.util.module_from_spec(spec)

# Execute the module (run the code in the .py file)
spec.loader.exec_module(data_module)

# Access the data from the imported module
data = data_module.example_var
print(data)  # Output: You're in file2
