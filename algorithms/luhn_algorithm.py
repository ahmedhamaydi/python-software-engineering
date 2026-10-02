def verify_card_number(card_number):
    card_number = str(card_number)
    card_number = card_number.replace("-", "")
    card_number = card_number.replace(" ", "")

    card_list = []
    double = False

    for number in reversed(card_number):
        number = int(number)

        if double:
            number = number * 2

            if number > 9:
                number = number - 9

        card_list.append(number)

        double = not double

    verification = sum(card_list)

    if verification % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


print(verify_card_number(453914889))
print(verify_card_number("4111-1111-1111-1111"))