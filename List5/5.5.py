def palindrom(słowo):
    słowo = słowo.lower()
    for i in range(int(len(słowo)/2)):
        if słowo[i] != słowo[len(słowo)-1-i]:
            return False
        else:
            return True

print(palindrom("banan"))
print(palindrom("Kajak"))
print(palindrom("zakaz"))
print(palindrom("pomidor"))
    
