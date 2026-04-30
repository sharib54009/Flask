contents = ["Myself Mohammed Sharib", "I am a Python developer", "I have 3 years of experience in Python programming", "I am passionate about coding and learning new technologies"]

fileNames = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]

for content, fileName in zip(contents, fileNames):
    file = open(fileName, "w")
    file.write(content)