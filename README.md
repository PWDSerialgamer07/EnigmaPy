# EnigmaPy

A small python tool that allows you to encode and decode stuff according to a key you create.

# Requirements:
Pyperclip

# Info
The crypting method is "XOR Bitwise". It's pretty fast, but has a major flaw concerning security: when the text is longer than the key (in this case, 24 letters), it's really easy to break.
Might switch to a more secure way of doing so.
