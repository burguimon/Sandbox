def covfefe(s):
    return s.replace("coverage", "covfefe") if "coverage" in s else s+" covfefe"
print(covfefe(input("Enter a sentence: ")))
