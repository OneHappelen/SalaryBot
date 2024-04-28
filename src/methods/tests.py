class Test:
    def int_test(self, data_bot: str) -> bool:
        if data_bot.isdigit() and data_bot != "0":
            return True
        return False


    def str_test(self, data_bot: str) -> bool:
        if not data_bot.isdigit():
            return True
        return False
    
    def anwswer_test(self, data_bot: str) -> bool:
        answer_list = ["да", "нет"]
        if data_bot.lower() in answer_list:
            return True
        return False
    
    def hack_test(self, data_bot: str) -> bool:
        mounth_list = ['янв', 'фев', 'март', 'апрел', 'ма', 'июн', 'июл', 'август', 'сентяб', 'октябр', 'ноябр', 'декабр']
        answer_flag = False
        mounth_flag = False
        stack = ''

        for i in data_bot:
            if i in ['д', 'н']:
                answer_flag = True
                break


        for mounth in data_bot:
            if mounth.isalpha():
                stack += mounth
            else:
                for i in mounth_list:
                    if i in stack.lower():
                        stack = ''
                        mounth_flag = True
                        break

        if mounth_flag and answer_flag:
            return True
        return False
            

    
test = Test()
