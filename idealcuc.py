print('Привет! ты здесь для того что-бы спасти галактику, нет времени объяснять, введи мне Cucumber!')

def fail_cuc():
    passw = input('До конца света осталось 10 секунд! Введи правильно, срочно!!! \nДавай ты сможешь: ')
    assert passw == 'Cucumber', 'Неревный пароль!!!'
while True:
    try:
       word = fail_cuc()
       print('Чувааак😎 да ты всех нас спас!!!❤❤❤')
       quit()
    except AssertionError as err:
       print(err)
