def new_user_param():
    user_param_str = (input('введите поочереди: имя пользователя, фамилия пользователя, год рождения, город проживания, e-mail, номер телефона '))
    user_param_list = user_param_str.split()
    user_param_dict = {'имя пользователя': (user_param_list[0]), 'фамилия пользователя': (user_param_list[1]), 'год рождения': (user_param_list[2]), 'город проживания': (user_param_list[3]), 'e-mail': (user_param_list[4]), 'номер телефона': (user_param_list[5])}
    return user_param_dict

print(new_user_param())
