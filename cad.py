def zamiana(s):
    rzymskie = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
    wynik = 0
    for i in range(len(s)):
        if i > 0 and rzymskie[s[i]] > rzymskie[s[i - 1]]:
            wynik += rzymskie[s[i]] - 2 * rzymskie[s[i - 1]]
        else:
            wynik += rzymskie[s[i]]
    return wynik


print(zamiana(input("Podaj liczbe rzymska: \n")))