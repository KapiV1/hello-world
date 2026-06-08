from funkcje.akcje import *



while True:
    print('co chcesz teraz porobić:')
    print('a - idź na polowanie')
    print('b - idź powalczyć z lasem')
    inp = input()
    if inp == 'a':
        walka(moby, Twoja_postać)

    elif inp == 'b':
        ścinaj_las(kłody, Twoja_postać)