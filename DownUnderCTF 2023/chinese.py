def chineseremainder(operators: list, results: list, printme: bool):
    opprod = 1
    products = []
    multipliers = []
    for each in operators:
        opprod *= each

    print(opprod)

    for eachh in operators:
        products.append(int(opprod/eachh))

    print(products)

    for eachhh in products:
        n = 1
        while int((eachhh*n) % (operators[products.index(eachhh)])) != 1:
            n += 1
        multipliers.append(n)

    print(multipliers)

    total = 0
    for i in range(len(operators)):
        total += (results[i] * products[i] * multipliers[i])

    base_original = int(total % opprod)
    if printme:
        print("With original values " + str(operators) + " and results " + str(results))
        print("The original number can be expressed by the formula " + str(base_original) + " + (" + str(opprod) + " * n) for any integer n.")
    return base_original, opprod


print(chineseremainder([2, 3, 5, 7], [1, 1, 1, 2], False))
