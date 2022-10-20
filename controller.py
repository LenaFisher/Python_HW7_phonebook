import model
import interface


def button_click():
    num2=0
    while num2==0:
        num = interface.format_mode()
        num2 = interface.choice_actoin()
    model.initChoises(num, num2)
    if num2==1:
        surname =interface.get_surname()
        name = interface.get_name()
        phone =interface.get_phone()
        description = interface.get_description()
        model.init(surname, name, phone, description)
    model.do_action()



