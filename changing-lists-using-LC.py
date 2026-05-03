filenames = ["1.todos", "2.report", "3.docs"]

filenames = [filename.replace('.', '-') + ".txt" for filename in filenames]
print(filenames)