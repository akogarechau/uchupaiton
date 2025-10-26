import datetime
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': datetime.date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2'), 'expiration_date': datetime.date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ],
}

def add(items, title, amount, expiration_date=None):
    if expiration_date != None:
        expiration_date = map(int, expiration_date.split('-'))
        expiration_date = datetime.date(*expiration_date)
    
    if title not in items.keys():
        items[title] = [
            {'amount': Decimal(amount), 'expiration_date': expiration_date}
            ]

    else:
        items[title].append({'amount': Decimal(amount), 'expiration_date': expiration_date})

def add_by_note(items, note):
    form_note = note.split(' ')
    if '-' in form_note[-1]:
        expiration_dateFromNote = form_note.pop()
        amountFromNote = form_note.pop()
        titleFromNote = ' '.join(form_note)
        add(items, titleFromNote, amountFromNote, expiration_dateFromNote)
    else:
        amountFromNote = form_note.pop()
        titleFromNote = ' '.join(form_note)
        add(items, titleFromNote, amountFromNote)
    
def find(items, needle):
    ListOfGoods = list(items.keys())
    FoundGoods = []
    for name in ListOfGoods:
        if needle.lower() in name.lower():
            FoundGoods.append(name)
    return FoundGoods

def amount(items, needle):
    count = 0
    ExactGoods = find(items, needle)
    for i in ExactGoods:
        for rev in items[i]:
            count += rev['amount']
    return count

add(goods, 'Пельмени Универсальные', '2', '2023-8-1')

add_by_note(goods, 'Яйца 4 2024-10-10')

print(*goods)