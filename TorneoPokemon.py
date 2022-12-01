import random


class Tipo:
    nombre = ''
    debilidades = []
    resistencias = []

    def __init__(self, nombre):
        self.nombre = nombre
        self.debilidades = self.switchDebilidades(nombre)
        self.resistencias = self.switchResistencias(nombre)

    def switchDebilidades(self, nombre):
        sw = {
            'Normal': ['Lucha'],
            'Lucha': ['Volador', 'Psiquico', 'Hada'],
            'Volador': ['Roca', 'Electrico', 'Hielo'],
            'Veneno': ['Tierra', 'Psiquico'],
            'Tierra': ['Agua', 'Planta', 'Hielo'],
            'Roca': ['Lucha', 'Tierra', 'Acero', 'Agua', 'Planta'],
            'Bicho': ['Volador', 'Roca', 'Fuego'],
            'Fantasma': ['Fantasma', 'Siniestro'],
            'Acero': ['Lucha', 'Tierra', 'Fuego'],
            'Fuego': ['Tierra', 'Roca', 'Agua'],
            'Agua': ['Planta', 'Electrico'],
            'Planta': ['Volador', 'Veneno', 'Bicho', 'Fuego', 'Hielo'],
            'Electrico': ['Tierra'],
            'Psiquico': ['Bicho', 'Fantasma', 'Siniestro'],
            'Hielo': ['Lucha', 'Roca', 'Acero', 'Fuego'],
            'Dragon': ['Hielo', 'Dragon', 'Hada'],
            'Siniestro': ['Lucha', 'Bicho', 'Hada'],
            'Hada': ['Veneno', 'Acero']
        }
        return sw.get(nombre, [])

    def switchResistencias(self, nombre):
        sw = {
            'Normal': ['Fantasma'],
            'Lucha': ['Roca', 'Bicho', 'Siniestro'],
            'Volador': ['Lucha', 'Bicho', 'Planta'],
            'Veneno': ['Lucha', 'Veneno', 'Bicho', 'Planta', 'Hada'],
            'Tierra': ['Veneno', 'Roca', 'Electrico'],
            'Roca': ['Normal', 'Volador', 'Veneno', 'Fuego'],
            'Bicho': ['Lucha', 'Tierra', 'Planta'],
            'Fantasma': ['Normal', 'Lucha', 'Veneno', 'Bicho'],
            'Acero': ['Normal', 'Volador', 'Veneno', 'Roca', 'Bicho', 'Acero', 'Planta', 'Psiquico', 'Hielo', 'Dragon', 'Hada'],
            'Fuego': ['Bicho', 'Acero', 'Fuego', 'Planta', 'Hielo', 'Hada'],
            'Agua': ['Acero', 'Fuego', 'Agua', 'Hielo'],
            'Planta': ['Tierra', 'Agua', 'Planta', 'Electrico'],
            'Electrico': ['Volador', 'Acero', 'Electrico'],
            'Psiquico': ['Lucha', 'Psiquico'],
            'Hielo': ['Hielo'],
            'Dragon': ['Fuego', 'Agua', 'Planta', 'Electrico'],
            'Siniestro': ['Fantasma', 'Psiquico', 'Siniestro'],
            'Hada': ['Lucha', 'Bicho', 'Dragon', 'Siniestro']
        }
        return sw.get(nombre, [])


class Pokemon:
    nombre = ''
    tipo = Tipo
    vida = 0
    ataque = 0

    def __init__(self, nombre, tipo, vida, ataque):
        self.nombre = nombre
        self.tipo = Tipo(tipo)
        self.vida = vida
        self.ataque = ataque

    def combate(self, pkmn2):
        print()
        print(self.nombre, 'vs', pkmn2.nombre, ':')
        vida1 = self.vida
        vida2 = pkmn2.vida
        atk1 = self.ataque
        atk2 = pkmn2.ataque
        for i in pkmn2.tipo.debilidades:
            if i == self.tipo.nombre:
                atk1 *= 2
                print('Atk', self.nombre, '=', atk1)
        if atk1 == self.ataque:
            for i in pkmn2.tipo.resistencias:
                if i == self.tipo.nombre:
                    atk1 /= 2
                    print('Atk', self.nombre, '=', atk1)
        for i in self.tipo.debilidades:
            if i == pkmn2.tipo.nombre:
                atk2 *= 2
                print('Atk', pkmn2.nombre, '=', atk2)
        if atk2 == pkmn2.ataque:
            for i in self.tipo.resistencias:
                if i == pkmn2.tipo.nombre:
                    atk2 /= 2
                    print('Atk', pkmn2.nombre, '=', atk2)

        if self.vida < pkmn2.vida:  # turno 0 => pkmn1 ataca a pkmn2; turno 1 => pkmn2 ataca a pkmn1
            turno = 0
        elif pkmn2.vida < self.vida:
            turno = 1
        elif atk1 <= atk2:
            turno = 0
        else:
            turno = 1
        while vida1 > 0 and vida2 > 0:
            if turno == 0:
                print('Turno', self.nombre)
                turno += 1
                vida2 -= atk1
                if vida2 > 0:
                    print('Vida', pkmn2.nombre, '=', vida2)
                else:
                    print('Vida', pkmn2.nombre, '= 0')
            else:
                print('Turno', pkmn2.nombre)
                turno -= 1
                vida1 -= atk2
                if vida1 > 0:
                    print('Vida', self.nombre, '=', vida1)
                else:
                    print('Vida', self.nombre, '= 0')
        if vida2 <= 0:
            print('Ganador:', self.nombre)
            return self.nombre
        else:
            print('Ganador:', pkmn2.nombre)
            return pkmn2.nombre


class Torneo:
    def __init__(self, num):
        self.posiciones = [Pokemon] * num
        self.cuadro = [Pokemon] * (num * 2 - 1)

    def comenzar(self, lista):
        listrand = random.sample(lista, self.posiciones.__len__())
        num = 0
        for i in listrand:
            self.posiciones[num] = i
            num += 1
        num = 0
        for i in self.posiciones:
            print(i.nombre)
            self.cuadro[num] = i
            num += 1
        while num < self.cuadro.__len__():  # aumentar num
            dif = self.cuadro.__len__() - num
            if dif == 1:  # final
                if self.cuadro[num-2].combate(self.cuadro[num-1]) == self.cuadro[num-2].nombre:
                    self.cuadro[num] = self.cuadro[num-2]
                else:
                    self.cuadro[num] = self.cuadro[num-1]
                num += 1
            elif dif == 3:  # semis
                if self.cuadro[num-4].combate(self.cuadro[num-3]) == self.cuadro[num-4].nombre:
                    self.cuadro[num] = self.cuadro[num-4]
                else:
                    self.cuadro[num] = self.cuadro[num-3]
                if self.cuadro[num-2].combate(self.cuadro[num-1]) == self.cuadro[num-2].nombre:
                    self.cuadro[num+1] = self.cuadro[num-2]
                else:
                    self.cuadro[num+1] = self.cuadro[num-1]
                num += 2
            elif dif == 7:  # cuartos
                if self.cuadro[num-8].combate(self.cuadro[num-7]) == self.cuadro[num-8].nombre:
                    self.cuadro[num] = self.cuadro[num-8]
                else:
                    self.cuadro[num] = self.cuadro[num-7]
                if self.cuadro[num-6].combate(self.cuadro[num-5]) == self.cuadro[num-6].nombre:
                    self.cuadro[num+1] = self.cuadro[num-6]
                else:
                    self.cuadro[num+1] = self.cuadro[num-5]
                if self.cuadro[num-4].combate(self.cuadro[num-3]) == self.cuadro[num-4].nombre:
                    self.cuadro[num+2] = self.cuadro[num-4]
                else:
                    self.cuadro[num+2] = self.cuadro[num-3]
                if self.cuadro[num-2].combate(self.cuadro[num-1]) == self.cuadro[num-2].nombre:
                    self.cuadro[num+3] = self.cuadro[num-2]
                else:
                    self.cuadro[num+3] = self.cuadro[num-1]
                num += 4
            elif dif == 15:  # octavos
                if self.cuadro[num-16].combate(self.cuadro[num-15]) == self.cuadro[num-16].nombre:
                    self.cuadro[num] = self.cuadro[num-16]
                else:
                    self.cuadro[num] = self.cuadro[num-15]
                if self.cuadro[num-14].combate(self.cuadro[num-13]) == self.cuadro[num-14].nombre:
                    self.cuadro[num+1] = self.cuadro[num-14]
                else:
                    self.cuadro[num+1] = self.cuadro[num-13]
                if self.cuadro[num-12].combate(self.cuadro[num-11]) == self.cuadro[num-12].nombre:
                    self.cuadro[num+2] = self.cuadro[num-12]
                else:
                    self.cuadro[num+2] = self.cuadro[num-11]
                if self.cuadro[num-10].combate(self.cuadro[num-9]) == self.cuadro[num-10].nombre:
                    self.cuadro[num+3] = self.cuadro[num-10]
                else:
                    self.cuadro[num+3] = self.cuadro[num-9]
                if self.cuadro[num-8].combate(self.cuadro[num-7]) == self.cuadro[num-8].nombre:
                    self.cuadro[num+4] = self.cuadro[num-8]
                else:
                    self.cuadro[num+4] = self.cuadro[num-7]
                if self.cuadro[num-6].combate(self.cuadro[num-5]) == self.cuadro[num-6].nombre:
                    self.cuadro[num+5] = self.cuadro[num-6]
                else:
                    self.cuadro[num+5] = self.cuadro[num-5]
                if self.cuadro[num-4].combate(self.cuadro[num-3]) == self.cuadro[num-4].nombre:
                    self.cuadro[num+6] = self.cuadro[num-4]
                else:
                    self.cuadro[num+6] = self.cuadro[num-3]
                if self.cuadro[num-2].combate(self.cuadro[num-1]) == self.cuadro[num-2].nombre:
                    self.cuadro[num+7] = self.cuadro[num-2]
                else:
                    self.cuadro[num+7] = self.cuadro[num-1]
                num += 8
            elif dif == 31:  # dieciseisavos
                if self.cuadro[num-32].combate(self.cuadro[num-31]) == self.cuadro[num-31].nombre:
                    self.cuadro[num] = self.cuadro[num-32]
                else:
                    self.cuadro[num] = self.cuadro[num-31]
                if self.cuadro[num-30].combate(self.cuadro[num-29]) == self.cuadro[num-30].nombre:
                    self.cuadro[num+1] = self.cuadro[num-30]
                else:
                    self.cuadro[num+1] = self.cuadro[num-29]
                if self.cuadro[num-28].combate(self.cuadro[num-27]) == self.cuadro[num-28].nombre:
                    self.cuadro[num+2] = self.cuadro[num-28]
                else:
                    self.cuadro[num+2] = self.cuadro[num-27]
                if self.cuadro[num-26].combate(self.cuadro[num-25]) == self.cuadro[num-26].nombre:
                    self.cuadro[num+3] = self.cuadro[num-26]
                else:
                    self.cuadro[num+3] = self.cuadro[num-25]
                if self.cuadro[num-24].combate(self.cuadro[num-23]) == self.cuadro[num-24].nombre:
                    self.cuadro[num+4] = self.cuadro[num-24]
                else:
                    self.cuadro[num+4] = self.cuadro[num-23]
                if self.cuadro[num-22].combate(self.cuadro[num-21]) == self.cuadro[num-22].nombre:
                    self.cuadro[num+5] = self.cuadro[num-22]
                else:
                    self.cuadro[num+5] = self.cuadro[num-21]
                if self.cuadro[num-20].combate(self.cuadro[num-19]) == self.cuadro[num-20].nombre:
                    self.cuadro[num+6] = self.cuadro[num-20]
                else:
                    self.cuadro[num+6] = self.cuadro[num-19]
                if self.cuadro[num-18].combate(self.cuadro[num-17]) == self.cuadro[num-18].nombre:
                    self.cuadro[num+7] = self.cuadro[num-18]
                else:
                    self.cuadro[num+7] = self.cuadro[num-17]
                if self.cuadro[num-16].combate(self.cuadro[num-15]) == self.cuadro[num-16].nombre:
                    self.cuadro[num+8] = self.cuadro[num-16]
                else:
                    self.cuadro[num+8] = self.cuadro[num-15]
                if self.cuadro[num-14].combate(self.cuadro[num-13]) == self.cuadro[num-14].nombre:
                    self.cuadro[num+9] = self.cuadro[num-14]
                else:
                    self.cuadro[num+9] = self.cuadro[num-13]
                if self.cuadro[num-12].combate(self.cuadro[num-11]) == self.cuadro[num-12].nombre:
                    self.cuadro[num+10] = self.cuadro[num-12]
                else:
                    self.cuadro[num+10] = self.cuadro[num-11]
                if self.cuadro[num-10].combate(self.cuadro[num-9]) == self.cuadro[num-10].nombre:
                    self.cuadro[num+11] = self.cuadro[num-10]
                else:
                    self.cuadro[num+11] = self.cuadro[num-9]
                if self.cuadro[num-8].combate(self.cuadro[num-7]) == self.cuadro[num-8].nombre:
                    self.cuadro[num+12] = self.cuadro[num-8]
                else:
                    self.cuadro[num+12] = self.cuadro[num-7]
                if self.cuadro[num-6].combate(self.cuadro[num-5]) == self.cuadro[num-6].nombre:
                    self.cuadro[num+13] = self.cuadro[num-6]
                else:
                    self.cuadro[num+13] = self.cuadro[num-5]
                if self.cuadro[num-4].combate(self.cuadro[num-3]) == self.cuadro[num-4].nombre:
                    self.cuadro[num+14] = self.cuadro[num-4]
                else:
                    self.cuadro[num+14] = self.cuadro[num-3]
                if self.cuadro[num-2].combate(self.cuadro[num-1]) == self.cuadro[num-2].nombre:
                    self.cuadro[num+15] = self.cuadro[num-2]
                else:
                    self.cuadro[num+15] = self.cuadro[num-1]
                num += 16
            elif dif == 63:  # treintaidosavos
                if self.cuadro[num-64].combate(self.cuadro[num-63]) == self.cuadro[num-64].nombre:
                    self.cuadro[num] = self.cuadro[num-64]
                else:
                    self.cuadro[num] = self.cuadro[num-63]
                if self.cuadro[num-62].combate(self.cuadro[num-61]) == self.cuadro[num-62].nombre:
                    self.cuadro[num+1] = self.cuadro[num-62]
                else:
                    self.cuadro[num+1] = self.cuadro[num-61]
                if self.cuadro[num-60].combate(self.cuadro[num-59]) == self.cuadro[num-60].nombre:
                    self.cuadro[num+2] = self.cuadro[num-60]
                else:
                    self.cuadro[num+2] = self.cuadro[num-59]
                if self.cuadro[num-58].combate(self.cuadro[num-57]) == self.cuadro[num-58].nombre:
                    self.cuadro[num+3] = self.cuadro[num-58]
                else:
                    self.cuadro[num+3] = self.cuadro[num-57]
                if self.cuadro[num-56].combate(self.cuadro[num-55]) == self.cuadro[num-56].nombre:
                    self.cuadro[num+4] = self.cuadro[num-56]
                else:
                    self.cuadro[num+4] = self.cuadro[num-55]
                if self.cuadro[num-54].combate(self.cuadro[num-53]) == self.cuadro[num-54].nombre:
                    self.cuadro[num+5] = self.cuadro[num-54]
                else:
                    self.cuadro[num+5] = self.cuadro[num-53]
                if self.cuadro[num-52].combate(self.cuadro[num-51]) == self.cuadro[num-52].nombre:
                    self.cuadro[num+6] = self.cuadro[num-52]
                else:
                    self.cuadro[num+6] = self.cuadro[num-51]
                if self.cuadro[num-50].combate(self.cuadro[num-49]) == self.cuadro[num-50].nombre:
                    self.cuadro[num+7] = self.cuadro[num-50]
                else:
                    self.cuadro[num+7] = self.cuadro[num-49]
                if self.cuadro[num-48].combate(self.cuadro[num-47]) == self.cuadro[num-48].nombre:
                    self.cuadro[num+8] = self.cuadro[num-48]
                else:
                    self.cuadro[num+8] = self.cuadro[num-47]
                if self.cuadro[num-46].combate(self.cuadro[num-45]) == self.cuadro[num-46].nombre:
                    self.cuadro[num+9] = self.cuadro[num-46]
                else:
                    self.cuadro[num+9] = self.cuadro[num-45]
                if self.cuadro[num-44].combate(self.cuadro[num-43]) == self.cuadro[num-44].nombre:
                    self.cuadro[num+10] = self.cuadro[num-44]
                else:
                    self.cuadro[num+10] = self.cuadro[num-43]
                if self.cuadro[num-42].combate(self.cuadro[num-41]) == self.cuadro[num-42].nombre:
                    self.cuadro[num+11] = self.cuadro[num-42]
                else:
                    self.cuadro[num+11] = self.cuadro[num-41]
                if self.cuadro[num-40].combate(self.cuadro[num-39]) == self.cuadro[num-40].nombre:
                    self.cuadro[num+12] = self.cuadro[num-40]
                else:
                    self.cuadro[num+12] = self.cuadro[num-39]
                if self.cuadro[num-38].combate(self.cuadro[num-37]) == self.cuadro[num-38].nombre:
                    self.cuadro[num+13] = self.cuadro[num-38]
                else:
                    self.cuadro[num+13] = self.cuadro[num-37]
                if self.cuadro[num-36].combate(self.cuadro[num-35]) == self.cuadro[num-36].nombre:
                    self.cuadro[num+14] = self.cuadro[num-36]
                else:
                    self.cuadro[num+14] = self.cuadro[num-35]
                if self.cuadro[num-34].combate(self.cuadro[num-33]) == self.cuadro[num-34].nombre:
                    self.cuadro[num+15] = self.cuadro[num-34]
                else:
                    self.cuadro[num+15] = self.cuadro[num-33]
                if self.cuadro[num-32].combate(self.cuadro[num-31]) == self.cuadro[num-32].nombre:
                    self.cuadro[num+16] = self.cuadro[num-32]
                else:
                    self.cuadro[num+16] = self.cuadro[num-31]
                if self.cuadro[num-30].combate(self.cuadro[num-29]) == self.cuadro[num-30].nombre:
                    self.cuadro[num+17] = self.cuadro[num-30]
                else:
                    self.cuadro[num+17] = self.cuadro[num-29]
                if self.cuadro[num-28].combate(self.cuadro[num-27]) == self.cuadro[num-28].nombre:
                    self.cuadro[num+18] = self.cuadro[num-28]
                else:
                    self.cuadro[num+18] = self.cuadro[num-27]
                if self.cuadro[num-26].combate(self.cuadro[num-25]) == self.cuadro[num-26].nombre:
                    self.cuadro[num+19] = self.cuadro[num-26]
                else:
                    self.cuadro[num+19] = self.cuadro[num-25]
                if self.cuadro[num-24].combate(self.cuadro[num-23]) == self.cuadro[num-24].nombre:
                    self.cuadro[num+20] = self.cuadro[num-24]
                else:
                    self.cuadro[num+20] = self.cuadro[num-23]
                if self.cuadro[num-22].combate(self.cuadro[num-21]) == self.cuadro[num-22].nombre:
                    self.cuadro[num+21] = self.cuadro[num-22]
                else:
                    self.cuadro[num+21] = self.cuadro[num-21]
                if self.cuadro[num-20].combate(self.cuadro[num-19]) == self.cuadro[num-20].nombre:
                    self.cuadro[num+22] = self.cuadro[num-20]
                else:
                    self.cuadro[num+22] = self.cuadro[num-19]
                if self.cuadro[num-18].combate(self.cuadro[num-17]) == self.cuadro[num-18].nombre:
                    self.cuadro[num+23] = self.cuadro[num-18]
                else:
                    self.cuadro[num+23] = self.cuadro[num-17]
                if self.cuadro[num-16].combate(self.cuadro[num-15]) == self.cuadro[num-16].nombre:
                    self.cuadro[num+24] = self.cuadro[num-16]
                else:
                    self.cuadro[num+24] = self.cuadro[num-15]
                if self.cuadro[num-14].combate(self.cuadro[num-13]) == self.cuadro[num-14].nombre:
                    self.cuadro[num+25] = self.cuadro[num-14]
                else:
                    self.cuadro[num+25] = self.cuadro[num-13]
                if self.cuadro[num-12].combate(self.cuadro[num-11]) == self.cuadro[num-12].nombre:
                    self.cuadro[num+26] = self.cuadro[num-12]
                else:
                    self.cuadro[num+26] = self.cuadro[num-11]
                if self.cuadro[num-10].combate(self.cuadro[num-9]) == self.cuadro[num-10].nombre:
                    self.cuadro[num+27] = self.cuadro[num-10]
                else:
                    self.cuadro[num+27] = self.cuadro[num-9]
                if self.cuadro[num-8].combate(self.cuadro[num-7]) == self.cuadro[num-8].nombre:
                    self.cuadro[num+28] = self.cuadro[num-8]
                else:
                    self.cuadro[num+28] = self.cuadro[num-7]
                if self.cuadro[num-6].combate(self.cuadro[num-5]) == self.cuadro[num-6].nombre:
                    self.cuadro[num+29] = self.cuadro[num-6]
                else:
                    self.cuadro[num+29] = self.cuadro[num-5]
                if self.cuadro[num-4].combate(self.cuadro[num-3]) == self.cuadro[num-4].nombre:
                    self.cuadro[num+30] = self.cuadro[num-4]
                else:
                    self.cuadro[num+30] = self.cuadro[num-3]
                if self.cuadro[num-2].combate(self.cuadro[num-1]) == self.cuadro[num-2].nombre:
                    self.cuadro[num+31] = self.cuadro[num-2]
                else:
                    self.cuadro[num+31] = self.cuadro[num-1]
                num += 32
            elif dif == 127:  # ronda1
                print()
                if self.cuadro[num-128].combate(self.cuadro[num-127]) == self.cuadro[num-128].nombre:
                    self.cuadro[num] = self.cuadro[num-128]
                else:
                    self.cuadro[num] = self.cuadro[num-127]
                if self.cuadro[num-126].combate(self.cuadro[num-125]) == self.cuadro[num-126].nombre:
                    self.cuadro[num+1] = self.cuadro[num-126]
                else:
                    self.cuadro[num+1] = self.cuadro[num-125]
                if self.cuadro[num-124].combate(self.cuadro[num-123]) == self.cuadro[num-124].nombre:
                    self.cuadro[num+2] = self.cuadro[num-124]
                else:
                    self.cuadro[num+2] = self.cuadro[num-123]
                if self.cuadro[num-122].combate(self.cuadro[num-121]) == self.cuadro[num-122].nombre:
                    self.cuadro[num+3] = self.cuadro[num-122]
                else:
                    self.cuadro[num+3] = self.cuadro[num-121]
                if self.cuadro[num-120].combate(self.cuadro[num-119]) == self.cuadro[num-120].nombre:
                    self.cuadro[num+4] = self.cuadro[num-120]
                else:
                    self.cuadro[num+4] = self.cuadro[num-119]
                if self.cuadro[num-118].combate(self.cuadro[num-117]) == self.cuadro[num-118].nombre:
                    self.cuadro[num+5] = self.cuadro[num-118]
                else:
                    self.cuadro[num+5] = self.cuadro[num-117]
                if self.cuadro[num-116].combate(self.cuadro[num-115]) == self.cuadro[num-116].nombre:
                    self.cuadro[num+6] = self.cuadro[num-116]
                else:
                    self.cuadro[num+6] = self.cuadro[num-115]
                if self.cuadro[num-114].combate(self.cuadro[num-113]) == self.cuadro[num-114].nombre:
                    self.cuadro[num+7] = self.cuadro[num-114]
                else:
                    self.cuadro[num+7] = self.cuadro[num-113]
                if self.cuadro[num-112].combate(self.cuadro[num-111]) == self.cuadro[num-112].nombre:
                    self.cuadro[num+8] = self.cuadro[num-112]
                else:
                    self.cuadro[num+8] = self.cuadro[num-111]
                if self.cuadro[num-110].combate(self.cuadro[num-109]) == self.cuadro[num-110].nombre:
                    self.cuadro[num+9] = self.cuadro[num-110]
                else:
                    self.cuadro[num+9] = self.cuadro[num-109]
                if self.cuadro[num-108].combate(self.cuadro[num-107]) == self.cuadro[num-108].nombre:
                    self.cuadro[num+10] = self.cuadro[num-108]
                else:
                    self.cuadro[num+10] = self.cuadro[num-107]
                if self.cuadro[num-106].combate(self.cuadro[num-105]) == self.cuadro[num-106].nombre:
                    self.cuadro[num+11] = self.cuadro[num-106]
                else:
                    self.cuadro[num+11] = self.cuadro[num-105]
                if self.cuadro[num-104].combate(self.cuadro[num-103]) == self.cuadro[num-104].nombre:
                    self.cuadro[num+12] = self.cuadro[num-104]
                else:
                    self.cuadro[num+12] = self.cuadro[num-103]
                if self.cuadro[num-102].combate(self.cuadro[num-101]) == self.cuadro[num-102].nombre:
                    self.cuadro[num+13] = self.cuadro[num-102]
                else:
                    self.cuadro[num+13] = self.cuadro[num-101]
                if self.cuadro[num-100].combate(self.cuadro[num-99]) == self.cuadro[num-100].nombre:
                    self.cuadro[num+14] = self.cuadro[num-100]
                else:
                    self.cuadro[num+14] = self.cuadro[num-99]
                if self.cuadro[num-98].combate(self.cuadro[num-97]) == self.cuadro[num-98].nombre:
                    self.cuadro[num+15] = self.cuadro[num-98]
                else:
                    self.cuadro[num+15] = self.cuadro[num-97]
                if self.cuadro[num-96].combate(self.cuadro[num-95]) == self.cuadro[num-96].nombre:
                    self.cuadro[num+16] = self.cuadro[num-96]
                else:
                    self.cuadro[num+16] = self.cuadro[num-95]
                if self.cuadro[num-94].combate(self.cuadro[num-93]) == self.cuadro[num-94].nombre:
                    self.cuadro[num+17] = self.cuadro[num-94]
                else:
                    self.cuadro[num+17] = self.cuadro[num-93]
                if self.cuadro[num-92].combate(self.cuadro[num-91]) == self.cuadro[num-92].nombre:
                    self.cuadro[num+18] = self.cuadro[num-92]
                else:
                    self.cuadro[num+18] = self.cuadro[num-91]
                if self.cuadro[num-90].combate(self.cuadro[num-89]) == self.cuadro[num-90].nombre:
                    self.cuadro[num+19] = self.cuadro[num-90]
                else:
                    self.cuadro[num+19] = self.cuadro[num-89]
                if self.cuadro[num-88].combate(self.cuadro[num-87]) == self.cuadro[num-88].nombre:
                    self.cuadro[num+20] = self.cuadro[num-88]
                else:
                    self.cuadro[num+20] = self.cuadro[num-87]
                if self.cuadro[num-86].combate(self.cuadro[num-85]) == self.cuadro[num-86].nombre:
                    self.cuadro[num+21] = self.cuadro[num-86]
                else:
                    self.cuadro[num+21] = self.cuadro[num-85]
                if self.cuadro[num-84].combate(self.cuadro[num-83]) == self.cuadro[num-84].nombre:
                    self.cuadro[num+22] = self.cuadro[num-84]
                else:
                    self.cuadro[num+22] = self.cuadro[num-83]
                if self.cuadro[num-82].combate(self.cuadro[num-81]) == self.cuadro[num-82].nombre:
                    self.cuadro[num+23] = self.cuadro[num-82]
                else:
                    self.cuadro[num+23] = self.cuadro[num-81]
                if self.cuadro[num-80].combate(self.cuadro[num-79]) == self.cuadro[num-80].nombre:
                    self.cuadro[num+24] = self.cuadro[num-80]
                else:
                    self.cuadro[num+24] = self.cuadro[num-79]
                if self.cuadro[num-78].combate(self.cuadro[num-77]) == self.cuadro[num-78].nombre:
                    self.cuadro[num+25] = self.cuadro[num-78]
                else:
                    self.cuadro[num+25] = self.cuadro[num-77]
                if self.cuadro[num-76].combate(self.cuadro[num-75]) == self.cuadro[num-76].nombre:
                    self.cuadro[num+26] = self.cuadro[num-76]
                else:
                    self.cuadro[num+26] = self.cuadro[num-75]
                if self.cuadro[num-74].combate(self.cuadro[num-73]) == self.cuadro[num-74].nombre:
                    self.cuadro[num+27] = self.cuadro[num-74]
                else:
                    self.cuadro[num+27] = self.cuadro[num-73]
                if self.cuadro[num-72].combate(self.cuadro[num-71]) == self.cuadro[num-72].nombre:
                    self.cuadro[num+28] = self.cuadro[num-72]
                else:
                    self.cuadro[num+28] = self.cuadro[num-71]
                if self.cuadro[num-70].combate(self.cuadro[num-69]) == self.cuadro[num-70].nombre:
                    self.cuadro[num+29] = self.cuadro[num-70]
                else:
                    self.cuadro[num+29] = self.cuadro[num-69]
                if self.cuadro[num-68].combate(self.cuadro[num-67]) == self.cuadro[num-68].nombre:
                    self.cuadro[num+30] = self.cuadro[num-68]
                else:
                    self.cuadro[num+30] = self.cuadro[num-67]
                if self.cuadro[num-66].combate(self.cuadro[num-65]) == self.cuadro[num-66].nombre:
                    self.cuadro[num+31] = self.cuadro[num-66]
                else:
                    self.cuadro[num+31] = self.cuadro[num-65]
                if self.cuadro[num-64].combate(self.cuadro[num-63]) == self.cuadro[num-64].nombre:
                    self.cuadro[num+32] = self.cuadro[num-64]
                else:
                    self.cuadro[num+32] = self.cuadro[num-63]
                if self.cuadro[num-62].combate(self.cuadro[num-61]) == self.cuadro[num-62].nombre:
                    self.cuadro[num+33] = self.cuadro[num-62]
                else:
                    self.cuadro[num+33] = self.cuadro[num-61]
                if self.cuadro[num-60].combate(self.cuadro[num-59]) == self.cuadro[num-60].nombre:
                    self.cuadro[num+34] = self.cuadro[num-60]
                else:
                    self.cuadro[num+34] = self.cuadro[num-59]
                if self.cuadro[num-58].combate(self.cuadro[num-57]) == self.cuadro[num-58].nombre:
                    self.cuadro[num+35] = self.cuadro[num-58]
                else:
                    self.cuadro[num+35] = self.cuadro[num-57]
                if self.cuadro[num-56].combate(self.cuadro[num-55]) == self.cuadro[num-56].nombre:
                    self.cuadro[num+36] = self.cuadro[num-56]
                else:
                    self.cuadro[num+36] = self.cuadro[num-55]
                if self.cuadro[num-54].combate(self.cuadro[num-53]) == self.cuadro[num-54].nombre:
                    self.cuadro[num+37] = self.cuadro[num-54]
                else:
                    self.cuadro[num+37] = self.cuadro[num-53]
                if self.cuadro[num-52].combate(self.cuadro[num-51]) == self.cuadro[num-52].nombre:
                    self.cuadro[num+38] = self.cuadro[num-52]
                else:
                    self.cuadro[num+38] = self.cuadro[num-51]
                if self.cuadro[num-50].combate(self.cuadro[num-49]) == self.cuadro[num-50].nombre:
                    self.cuadro[num+39] = self.cuadro[num-50]
                else:
                    self.cuadro[num+39] = self.cuadro[num-49]
                if self.cuadro[num-48].combate(self.cuadro[num-47]) == self.cuadro[num-48].nombre:
                    self.cuadro[num+40] = self.cuadro[num-48]
                else:
                    self.cuadro[num+40] = self.cuadro[num-47]
                if self.cuadro[num-46].combate(self.cuadro[num-45]) == self.cuadro[num-46].nombre:
                    self.cuadro[num+41] = self.cuadro[num-46]
                else:
                    self.cuadro[num+41] = self.cuadro[num-45]
                if self.cuadro[num-44].combate(self.cuadro[num-43]) == self.cuadro[num-44].nombre:
                    self.cuadro[num+42] = self.cuadro[num-44]
                else:
                    self.cuadro[num+42] = self.cuadro[num-43]
                if self.cuadro[num-42].combate(self.cuadro[num-41]) == self.cuadro[num-42].nombre:
                    self.cuadro[num+43] = self.cuadro[num-42]
                else:
                    self.cuadro[num+43] = self.cuadro[num-41]
                if self.cuadro[num-40].combate(self.cuadro[num-39]) == self.cuadro[num-40].nombre:
                    self.cuadro[num+44] = self.cuadro[num-40]
                else:
                    self.cuadro[num+44] = self.cuadro[num-39]
                if self.cuadro[num-38].combate(self.cuadro[num-37]) == self.cuadro[num-38].nombre:
                    self.cuadro[num+45] = self.cuadro[num-38]
                else:
                    self.cuadro[num+45] = self.cuadro[num-37]
                if self.cuadro[num-36].combate(self.cuadro[num-35]) == self.cuadro[num-36].nombre:
                    self.cuadro[num+46] = self.cuadro[num-36]
                else:
                    self.cuadro[num+46] = self.cuadro[num-35]
                if self.cuadro[num-34].combate(self.cuadro[num-33]) == self.cuadro[num-34].nombre:
                    self.cuadro[num+47] = self.cuadro[num-34]
                else:
                    self.cuadro[num+47] = self.cuadro[num-33]
                if self.cuadro[num-32].combate(self.cuadro[num-31]) == self.cuadro[num-32].nombre:
                    self.cuadro[num+48] = self.cuadro[num-32]
                else:
                    self.cuadro[num+48] = self.cuadro[num-31]
                if self.cuadro[num-30].combate(self.cuadro[num-29]) == self.cuadro[num-30].nombre:
                    self.cuadro[num+49] = self.cuadro[num-30]
                else:
                    self.cuadro[num+49] = self.cuadro[num-29]
                if self.cuadro[num-28].combate(self.cuadro[num-27]) == self.cuadro[num-28].nombre:
                    self.cuadro[num+50] = self.cuadro[num-28]
                else:
                    self.cuadro[num+50] = self.cuadro[num-27]
                if self.cuadro[num-26].combate(self.cuadro[num-25]) == self.cuadro[num-26].nombre:
                    self.cuadro[num+51] = self.cuadro[num-26]
                else:
                    self.cuadro[num+51] = self.cuadro[num-25]
                if self.cuadro[num-24].combate(self.cuadro[num-23]) == self.cuadro[num-24].nombre:
                    self.cuadro[num+52] = self.cuadro[num-24]
                else:
                    self.cuadro[num+52] = self.cuadro[num-23]
                if self.cuadro[num-22].combate(self.cuadro[num-21]) == self.cuadro[num-22].nombre:
                    self.cuadro[num+53] = self.cuadro[num-22]
                else:
                    self.cuadro[num+53] = self.cuadro[num-21]
                if self.cuadro[num-20].combate(self.cuadro[num-19]) == self.cuadro[num-20].nombre:
                    self.cuadro[num+54] = self.cuadro[num-20]
                else:
                    self.cuadro[num+54] = self.cuadro[num-19]
                if self.cuadro[num-18].combate(self.cuadro[num-17]) == self.cuadro[num-18].nombre:
                    self.cuadro[num+55] = self.cuadro[num-18]
                else:
                    self.cuadro[num+55] = self.cuadro[num-17]
                if self.cuadro[num-16].combate(self.cuadro[num-15]) == self.cuadro[num-16].nombre:
                    self.cuadro[num+56] = self.cuadro[num-16]
                else:
                    self.cuadro[num+56] = self.cuadro[num-15]
                if self.cuadro[num-14].combate(self.cuadro[num-13]) == self.cuadro[num-14].nombre:
                    self.cuadro[num+57] = self.cuadro[num-14]
                else:
                    self.cuadro[num+57] = self.cuadro[num-13]
                if self.cuadro[num-12].combate(self.cuadro[num-11]) == self.cuadro[num-12].nombre:
                    self.cuadro[num+58] = self.cuadro[num-12]
                else:
                    self.cuadro[num+58] = self.cuadro[num-11]
                if self.cuadro[num-10].combate(self.cuadro[num-9]) == self.cuadro[num-10].nombre:
                    self.cuadro[num+59] = self.cuadro[num-10]
                else:
                    self.cuadro[num+59] = self.cuadro[num-9]
                if self.cuadro[num-8].combate(self.cuadro[num-7]) == self.cuadro[num-8].nombre:
                    self.cuadro[num+60] = self.cuadro[num-8]
                else:
                    self.cuadro[num+60] = self.cuadro[num-7]
                if self.cuadro[num-6].combate(self.cuadro[num-5]) == self.cuadro[num-6].nombre:
                    self.cuadro[num+61] = self.cuadro[num-6]
                else:
                    self.cuadro[num+61] = self.cuadro[num-5]
                if self.cuadro[num-4].combate(self.cuadro[num-3]) == self.cuadro[num-4].nombre:
                    self.cuadro[num+62] = self.cuadro[num-4]
                else:
                    self.cuadro[num+62] = self.cuadro[num-3]
                if self.cuadro[num-2].combate(self.cuadro[num-1]) == self.cuadro[num-2].nombre:
                    self.cuadro[num+63] = self.cuadro[num-2]
                else:
                    self.cuadro[num+63] = self.cuadro[num-1]
                num += 64
            else:
                num = self.cuadro.__len__()
        print('El ganador del torneo es... ' + self.cuadro[num - 1].nombre + '!!!')


# main


pokemon1 = Pokemon('Articuno', 'Hielo', 120, 100)
pokemon2 = Pokemon('Zapdos', 'Electrico', 120, 120)
pokemon3 = Pokemon('Moltres', 'Fuego', 120, 150)
pokemon4 = Pokemon('Mewtwo', 'Psiquico', 300, 170)
pokemon5 = Pokemon('Raikou', 'Electrico', 170, 150)
pokemon6 = Pokemon('Entei', 'Fuego', 180, 100)
pokemon7 = Pokemon('Suicune', 'Agua', 180, 150)
pokemon8 = Pokemon('Lugia', 'Volador', 190, 170)
pokemon9 = Pokemon('Ho-Oh', 'Volador', 190, 180)
pokemon10 = Pokemon('Regirock', 'Roca', 120, 100)
pokemon11 = Pokemon('Regice', 'Hielo', 130, 70)
pokemon12 = Pokemon('Registeel', 'Acero', 130, 90)
pokemon13 = Pokemon('Latias', 'Dragon', 160, 70)
pokemon14 = Pokemon('Latios', 'Dragon', 170, 120)
pokemon15 = Pokemon('Kyogre', 'Agua', 240, 150)
pokemon16 = Pokemon('Groudon', 'Tierra', 240, 100)
pokemon17 = Pokemon('Rayquaza', 'Dragon', 170, 130)
pokemon18 = Pokemon('Uxie', 'Psiquico', 90, 60)
pokemon19 = Pokemon('Azelf', 'Psiquico', 120, 90)
pokemon20 = Pokemon('Mesprit', 'Psiquico', 70, 40)
pokemon21 = Pokemon('Dialga', 'Dragon', 180, 150)
pokemon22 = Pokemon('Palkia', 'Dragon', 180, 150)
pokemon23 = Pokemon('Heatran', 'Acero', 190, 130)
pokemon24 = Pokemon('Regigigas', 'Normal', 180, 160)
pokemon25 = Pokemon('Giratina', 'Fantasma', 180, 130)
pokemon26 = Pokemon('Cresselia', 'Psiquico', 130, 130)
pokemon27 = Pokemon('Cobalion', 'Lucha', 120, 80)
pokemon28 = Pokemon('Virizion', 'Lucha', 170, 50)
pokemon29 = Pokemon('Terrakion', 'Lucha', 140, 80)
pokemon30 = Pokemon('Keldeo', 'Lucha', 170, 110)
pokemon31 = Pokemon('Tornadus', 'Volador', 170, 100)
pokemon32 = Pokemon('Thundurus', 'Electrico', 180, 140)
pokemon33 = Pokemon('Landorus', 'Tierra', 180, 80)
pokemon34 = Pokemon('Reshiram', 'Fuego', 180, 150)
pokemon35 = Pokemon('Zekrom', 'Electrico', 180, 150)
pokemon36 = Pokemon('Kyurem', 'Hielo', 180, 130)
pokemon37 = Pokemon('Xerneas', 'Hada', 130, 100)
pokemon38 = Pokemon('Yveltal', 'Siniestro', 180, 100)
pokemon39 = Pokemon('Zygarde', 'Tierra', 200, 150)
pokemon40 = Pokemon('Codigo Cero', 'Normal', 110, 70)
pokemon41 = Pokemon('Silvally', 'Normal', 210, 120)
pokemon42 = Pokemon('Tapu Koko', 'Hada', 170, 130)
pokemon43 = Pokemon('Tapu Lele', 'Hada', 170, 40)
pokemon44 = Pokemon('Tapu Fini', 'Hada', 120, 100)
pokemon45 = Pokemon('Tapu Bulu', 'Hada', 180, 150)
pokemon46 = Pokemon('Solgaleo', 'Acero', 250, 230)
pokemon47 = Pokemon('Lunala', 'Fantasma', 250, 120)
pokemon48 = Pokemon('Nekrozma', 'Psiquico', 180, 180)
pokemon49 = Pokemon('Zacian', 'Hada', 120, 120)
pokemon50 = Pokemon('Zamacenta', 'Lucha', 120, 120)
pokemon51 = Pokemon('Eternatus', 'Veneno', 220, 120)
pokemon52 = Pokemon('Hoopa', 'Fantasma', 190, 160)
pokemon53 = Pokemon('Victini', 'Fuego', 190, 60)
pokemon54 = Pokemon('Meloetta', 'Psiquico', 110, 90)
pokemon55 = Pokemon('Genesect', 'Bicho', 170, 100)
pokemon56 = Pokemon('Deoxys', 'Psiquico', 120, 120)
pokemon57 = Pokemon('Arceus', 'Normal', 260, 150)
pokemon58 = Pokemon('Darkrai', 'Siniestro', 180, 130)
pokemon59 = Pokemon('Phione', 'Agua', 70, 30)
pokemon60 = Pokemon('Manaphy', 'Agua', 120, 60)
pokemon61 = Pokemon('Jirachi', 'Acero', 160, 100)
pokemon62 = Pokemon('Celebi', 'Psiquico', 180, 100)
pokemon63 = Pokemon('Mew', 'Psiquico', 180, 120)
pokemon64 = Pokemon('Melmetal', 'Acero', 220, 110)
pokemon65 = Pokemon('Shaymin', 'Planta', 110, 60)
pokemon66 = Pokemon('Diancie', 'Roca', 190, 100)
pokemon67 = Pokemon('Magearna', 'Acero', 160, 120)
pokemon68 = Pokemon('Zeraora', 'Electrico', 190, 160)
pokemon69 = Pokemon('Marshadow', 'Fantasma', 150, 120)
pokemon70 = Pokemon('Calyrex', 'Planta', 170, 100)
pokemon71 = Pokemon('Volcanion', 'Fuego', 180, 130)
pokemon72 = Pokemon('Kubfu', 'Lucha', 70, 60)
pokemon73 = Pokemon('Urshifu', 'Lucha', 220, 180)
pokemon74 = Pokemon('Spectrier', 'Fantasma', 100, 100)
pokemon75 = Pokemon('Glastrier', 'Hielo', 100, 100)
pokemon76 = Pokemon('Regieleki', 'Electrico', 180, 100)
pokemon77 = Pokemon('Regidrago', 'Dragon', 180, 100)
pokemon78 = Pokemon('Zarude', 'Siniestro', 120, 110)
pokemon79 = Pokemon('Venusaur', 'Planta', 180, 90)
pokemon80 = Pokemon('Blastoise', 'Agua', 240, 120)
pokemon81 = Pokemon('Charizard', 'Fuego', 280, 100)
pokemon82 = Pokemon('Serperior', 'Planta', 140, 80)
pokemon83 = Pokemon('Samurott', 'Agua', 140, 90)
pokemon84 = Pokemon('Emboar', 'Fuego', 180, 150)
pokemon85 = Pokemon('Chesnaught', 'Planta', 160, 90)
pokemon86 = Pokemon('Greninja', 'Agua', 230, 130)
pokemon87 = Pokemon('Delphox', 'Fuego', 170, 80)
pokemon88 = Pokemon('Meganium', 'Planta', 150, 110)
pokemon89 = Pokemon('Ferraligatr', 'Agua', 160, 130)
pokemon90 = Pokemon('Thyphlosion', 'Fuego', 160, 120)
pokemon91 = Pokemon('Sceptile', 'Planta', 230, 130)
pokemon92 = Pokemon('Swampert', 'Agua', 220, 130)
pokemon93 = Pokemon('Blaziken', 'Fuego', 210, 100)
pokemon94 = Pokemon('Torterra', 'Planta', 150, 80)
pokemon95 = Pokemon('Empoleon', 'Agua', 160, 130)
pokemon96 = Pokemon('Infernape', 'Fuego', 130, 120)
pokemon97 = Pokemon('Decidueye', 'Planta', 240, 90)
pokemon98 = Pokemon('Primarina', 'Agua', 250, 120)
pokemon99 = Pokemon('Incineroar', 'Fuego', 250, 130)
pokemon100 = Pokemon('Rillaboom', 'Planta', 170, 140)
pokemon101 = Pokemon('Inteleon', 'Agua', 160, 120)
pokemon102 = Pokemon('Cinderace', 'Fuego', 170, 160)

lista = [pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6, pokemon7, pokemon8, pokemon9, pokemon10, pokemon11,
         pokemon12, pokemon13, pokemon14, pokemon15, pokemon16, pokemon17, pokemon18, pokemon19, pokemon20, pokemon21,
         pokemon22, pokemon23, pokemon24, pokemon25, pokemon26, pokemon27, pokemon28, pokemon29, pokemon30, pokemon31,
         pokemon32, pokemon33, pokemon34, pokemon35, pokemon36, pokemon37, pokemon38, pokemon39, pokemon40, pokemon41,
         pokemon42, pokemon43, pokemon44, pokemon45, pokemon46, pokemon47, pokemon48, pokemon49, pokemon50, pokemon51,
         pokemon52, pokemon53, pokemon54, pokemon55, pokemon56, pokemon57, pokemon58, pokemon59, pokemon60, pokemon61,
         pokemon62, pokemon63, pokemon64, pokemon65, pokemon66, pokemon67, pokemon68, pokemon69, pokemon70, pokemon71,
         pokemon72, pokemon73, pokemon74, pokemon75, pokemon76, pokemon77, pokemon78, pokemon79, pokemon80, pokemon81,
         pokemon82, pokemon83, pokemon84, pokemon85, pokemon86, pokemon87, pokemon88, pokemon89, pokemon90, pokemon91,
         pokemon92, pokemon93, pokemon94, pokemon95, pokemon96, pokemon97, pokemon98, pokemon99, pokemon100, pokemon101,
         pokemon102]

t = Torneo(16)
t.comenzar(lista)
