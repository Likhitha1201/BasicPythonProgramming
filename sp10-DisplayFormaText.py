import textwrap

def format_text(text, width=50):
    wrapped_text = textwrap.fill(text, width=width)
    print(wrapped_text)

# Example usage
sample_text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Pellentesque euismod, urna eu tincidunt consectetur, nisi nibh bibendum neque, 
eget malesuada nunc magna non purus.??Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""

format_text(sample_text, 10)
