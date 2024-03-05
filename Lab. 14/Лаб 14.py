class Tomato:
    states = {0: 'Нифига＼(￣▽￣)／', 1: 'цветёт и пахнет (✯◡✯)', 2: 'ещё зелёная (o-_-o)', 3: 'уже покраснела o(>ω<)o'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        self._change_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Помидорка {self._index + 1} {Tomato.states[self._state]}')


class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print('Садовничек ухаживает за помидорками (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', '\n')
        self._plant.grow_all()
        print('\n', 'Садовничек закончил ухаживать! (╯✧▽✧)╯', '\n')

    def harvesting(self):
        print('Садовничек тырит помидрки (*¯︶¯*)', '\n')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Все стырил!(o˘◡˘o)')
        else:
            print('Эээ, это слишком рано! Они же зелёненькие ٩(｡•́‿•̀｡)۶', '\n')

    def reference():
        print('''Вообще, самое классное это собирать помидорки
когда они почти созрели и потхоньку дозревают на лозе!
Если их так собирать они не расслаиваются,
не набивают шишек и вообще намного вкусней!
Ну и за ними проще следить, конечно (＠＾◡＾)''', '\n')

say_1 = input('Хе) Привет! Хочешь расскажу когда лучше собирать помидорки? (да/нет) ')
if say_1 == 'да':
    print('\n', 'Хе! Я так и знала)', '\n')
    Gardener.reference()
elif say_1 == 'нет':
    print('\n', '...злюка...', '\n')
    Gardener.reference()
else:
    print('\n', 'Раз ты вредничаешь, то точно нифига не скажу!', '\n')

if __name__ == '__main__':
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Яяяяя', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvesting()
    gardener.work()
    gardener.harvesting()
