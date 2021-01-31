class Road:

    def __init__(self):
        print('начинаем расчет массы асфальта, необходимого для покрытия всего дорожного полотна')
        self._length = float(input('введите длину дороги в метрах ', ))
        self._width = float(input('введите ширину дороги в метрах ', ))

    def mass(self):
        return self._length * self._width * 25 * 5

road_msk_khv = Road()
print('для покрытия всего дорожного полотна необходимо ', road_msk_khv.mass(), 'тонн')