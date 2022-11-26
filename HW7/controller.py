import model
import view

def start_program():
    view.user_menu()
    choice()
       
def choice():
    choice = input("Введите номер: ")
    next_step(choice)    

def next_step(choice):
    match choice:
        case "1":
           print(model.get_Spravochnik())
        case "2":
            model.export_xml_Spravochnik()
        case "3":
            model.new_record()
        case _:
            start_program()