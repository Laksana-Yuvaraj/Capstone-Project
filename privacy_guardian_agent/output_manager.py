def save_output(text, filename="redacted_output.txt"):
    with open(filename, "w") as f:
        f.write(text)
