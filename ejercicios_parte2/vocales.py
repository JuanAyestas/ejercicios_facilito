def vocal_count(string, vowels):
    string = string.casefold()
    count = {}.fromkeys(vowels, 0)
    for character in string:
        if character in count:
            count[character] += 1
    keys = list(count.keys())
    values = list(count.values())
    print("Se repitió la vocal: {} {} veces.".format(keys,values))
    return count

vocales = 'aeiou'
oracion = str(input("Ingrese una oración: "))
print(vocal_count(oracion, vocales))
