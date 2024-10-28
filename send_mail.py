massage = input('Введите текст сообщения')
recipient = input('Введите почту получателя')
sender = input('Введите почту отправителя (необязательно заполнять, если хотите отправить письмо от university.help@gmail.com)')

def send_email(massage, recipient, sender = 'university.help@gmail.com'):
    if sender == 'university.help@gmail.com' and recipient != sender:
        print('Письмо успешно отправлено с адреса university.help@gmail.com на адрес', recipient)
    else:
        if (sender != 'university.help@gmail.com' and recipient != sender and recipient.find('@') != -1
                and (recipient.find('.ru') != -1 or recipient.find('.com') != -1 or recipient.find('.net') != -1)
                and (sender.find('.ru') != -1 or sender.find('.com') != -1 or sender.find('.net') != -1)):
            print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender,'на адрес', recipient)
        else:
            if recipient == sender:
                print('Нельзя отправить письмо самому себе!')
            else:
                print('Невозможно отправить письмо с адреса', sender,'на адрес', recipient)
if sender == '':
    send_email(massage, recipient)
else:
    send_email(massage,recipient,sender)