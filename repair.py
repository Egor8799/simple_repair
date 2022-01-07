#!/usr/bin/env python3
import os
import time
from playsound import playsound
import webbrowser
q_start=input('Приветствую! Чем могу помочь вам?\n1. Проверить звук\n2. Установка драйвера для Windows\n3. Проверить скорость интернета\nВыберите цифру: ')
if q_start == '1':
    print('Убедитесь, что выбрали правильное устройство по умолчанию.')
    time.sleep(2)
    soundcheck=input('Продолжить? [Y/N] ')
    print('Проверка левого динамика...')
    time.sleep(0.6)
    playsound('left.wav')
    leftsound=input('Вы услышали что-нибудь на левом динамике? [Y/N] ')
    if leftsound == 'Y':
        print('Прекрасно!')
        time.sleep(1)
        print('Проверка правого динамика...')
        time.sleep(0.6)
        playsound('right.wav')
        rightsound=input('Вы услышали что-нибудь на правом динамике? [Y/N] ')
        if rightsound == 'Y':
            print('Отлично, проверка звука завершена!')
        elif rightsound == 'N':
            print('Проверка звука завершена. Обратитесь к специалисту или выполните проверку повторно.')
    elif leftsound == 'N':
        print('Окей...')
        time.sleep(1)
        print('Проверка правого динамика...')
        time.sleep(0.6)
        playsound('right.wav')
        rightsound=input('Вы услышали что-нибудь на правом динамике? [Y/N] ')
        if rightsound == 'Y':
            print('Отлично, проверка звука завершена!')
        elif rightsound == 'N':
            print('Проверка звука завершена. Обратитесь к специалисту или выполните проверку повторно.')
elif q_start == '3':
    site=input('На каком сайте или адресе хотите проверить? https://')
    print('Хорошо, будет отправлено 15 запросов используя ping!')
    time.sleep(2)
    os.system('ping ' + site + ' -c 15')
    print('Работа ping завершена. Подробности написаны выше.')
elif q_start == '2':
    q_driver=input('Какой драйвер вам нужен?\n1. Интернет\n2. Видеокарта\n3. Звук\n4. Другое\nВыберите цифру: ')
    if q_driver == '1':
        print('Хорошо, сейчас найду информацию о текущих адаптерах...')
        time.sleep(2)
        print('--- ВНИМАНИЕ! ЭТО ВАЖНАЯ ИНФОРМАЦИЯ! ---')
        os.system("lspci | grep -i 'net'")
        print('----------------------------------------')
        inet_dr=input('Теперь, можете поискать драйвер на сайте.\n1. sector.biz.ua\n2. driver.ru\nВыберите сайт, где хотите поискать драйвер: ')
        if inet_dr == '1':
            print('Сейчас откроется выбранный вами сайт. Вы должны найти драйвер на сайте по информации, которую я дал вам выше. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://sector.biz.ua/drivers/index.phtml?fldr=%2FLAN_WiFi%2F')
        elif inet_dr == '2':
            print('Сейчас откроется выбранный вами сайт. Вы должны найти драйвер на сайте по информации, которую я дал вам выше. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://driver.ru/?C=74')
    elif q_driver == '2':
        print('Хорошо, сейчас найду информацию о текущих видеокартах...')
        time.sleep(2)
        print('--- ВНИМАНИЕ! ЭТО ВАЖНАЯ ИНФОРМАЦИЯ! ---')
        os.system("lspci -v | grep --color -E '(VGA|3D)'")
        print('----------------------------------------')
        video_dr=input('Теперь, можете поискать драйвер на сайте.\n1. sector.biz.ua\n2. driver.ru\nВыберите сайт, где хотите поискать драйвер: ')
        if video_dr == '1':
            print('Сейчас откроется выбранный вами сайт. Вы должны найти драйвер на сайте по информации, которую я дал вам выше. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://sector.biz.ua/drivers/index.phtml?fldr=%2FVideo%2F')
        elif video_dr == '2':
            print('Сейчас откроется выбранный вами сайт. Вы должны найти драйвер на сайте по информации, которую я дал вам выше. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://driver.ru/?C=1')
    elif q_driver == '3':
        print('Хорошо, сейчас найду информацию о текущих звуковых устройств...')
        time.sleep(2)
        print('--- ВНИМАНИЕ! ЭТО ВАЖНАЯ ИНФОРМАЦИЯ! ---')
        os.system("lspci | grep Audio")
        print('ИНФОРМАЦИЯ О ЗВУКЕ МОЖЕТ БЫТЬ НЕ ТОЧНОЙ!')
        sound_dr=input('Теперь, можете поискать драйвер на сайте.\n1. sector.biz.ua\n2. driver.ru\nВыберите сайт, где хотите поискать драйвер: ')
        if sound_dr == '1':
            print('Сейчас откроется выбранный вами сайт. Вы должны найти драйвер на сайте по информации, которую я дал вам выше. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://sector.biz.ua/drivers/index.phtml?fldr=%2FAudio%2F')
        elif sound_dr == '2':
            print('Сейчас откроется выбранный вами сайт. Вы должны найти драйвер на сайте по информации, которую я дал вам выше. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://driver.ru/?C=3')
    elif q_driver == '4':
        print('Вы выбрали другое потому-что вам нужен другой драйвер, или не удалось установить драйвер.')
        time.sleep(2)
        print('Я выдам всю информацию о всех устройств...')
        time.sleep(3)
        os.system("lspci -vmm")
        other_dr=input('Найдите нужное вам устройств и перейдите на один из предложенных сайтов.\n1. sector.biz.ua\n2. driver.ru\nВыберите сайт: ')
        if other_dr == '1':
            print('Сейчас откроется выбранный вами сайт. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://sector.biz.ua/drivers/')
        elif other_dr == '2':
            print('Сейчас откроется выбранный вами сайт. Удачи!')
            time.sleep(4)
            webbrowser.open_new_tab('https://driver.ru/')
