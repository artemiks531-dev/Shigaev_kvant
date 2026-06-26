def privet(who_from, **who_to):
    who_to_list = []

    items = list(who_to.items())
    for item in items:
        who_to_list.append(', '.join(item))

    print(
        f'вам привет от {who_from}!:\n'
        f'кому: {'\n'.join(who_to_list)}\n'
    )


privet('artiom', raushan='hello bro', karim='krutoy')