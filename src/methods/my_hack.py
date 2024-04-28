def full_sal(bot_data: str):
    stack = ''
    done = []

    for answer in bot_data:
        if answer.isalpha():
            stack += answer
        else:
            if stack.lower() in ["да", "нет"]:
                done.append(stack)
                stack = ''
                break
            return
            

    days = []
    summ = []

    for find in bot_data:
        if find.isdigit():
            stack += find
            continue
        else:
            if len(stack) <= 2 and stack.isdecimal():
                days.append(stack)
                stack = ''
            elif len(stack) > 2:
                summ.append(stack)
                stack = ''

    full_summ = 0
    for numb in summ: 
        full_summ += int(numb)

    done.append(len(days))
    done.append(full_summ)
    keys = ['service', 'days', 'summ']
    my_dict = dict(zip(keys, done))
    return my_dict








