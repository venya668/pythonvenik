calls = 0
schet = 0
list_to_search = []
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    spisok = []
    dl = len(string)
    spisok.append(dl)
    vr = string.upper()
    spisok.append(vr)
    nr = vr.lower()
    spisok.append(nr)
    kortez = tuple(spisok)
    print(kortez)

def is_contains(string, list_to_search):
    count_calls()
    global schet
    while schet != 4:
        schet += 1
        t = input('Добавьте элементы списка(4)')
        list_to_search.append(t)
    if string in list_to_search:
        print(True)
    else:
        print(False)




string = input('Напишите что-нибуть')
string_info(string)
is_contains(string, list_to_search)
print(calls)