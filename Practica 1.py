class FS3:
    
    def __init__(self):
        self.los_uwu = LosUwU()
        self.toyota_legacy = ToyotaLegacy()
        self.pinguinos_galacticos = PinguinosGalacticos()
        self.los_tres_mosqueteros = LosTresMosqueteros()
        self.web_heroes = WebHeroes()
        self.los_polystation = LosPolystation()

    def __str__(self):
        return ("\nClase FS3\n"
                "\nLos =^UwU^=:\n" + str(self.los_uwu) + "\n" +
                "\nToyota Legacy:\n" + str(self.toyota_legacy) + "\n" +
                "\nPingüinos galácticos:\n" + str(self.pinguinos_galacticos) + "\n" +
                "\nLos 3 mosqueteros:\n" + str(self.los_tres_mosqueteros) + "\n" +
                "\nWebHeroes:\n" + str(self.web_heroes) + "\n" +
                "\nLos polystation:\n" + str(self.los_polystation))


class EquipoMateria:
    def __init__(self, nombre_integrante1, nombre_integrante2="", nombre_integrante3=""):
        self.nombre_integrante1 = nombre_integrante1
        self.nombre_integrante2 = nombre_integrante2
        self.nombre_integrante3 = nombre_integrante3

    def __str__(self):
        integrantes = [self.nombre_integrante1, self.nombre_integrante2, self.nombre_integrante3]
        integrantes = [integrante for integrante in integrantes if integrante]
        return "\n".join(integrantes)
        
class LosUwU(EquipoMateria):
    def __init__(self):
        super().__init__("- Leonardo Alberto González Carmona",
                         "- Norma Graciela Mendoza Ruiz",
                         "- Jonathan Durán Mendoza")


class ToyotaLegacy(EquipoMateria):
    def __init__(self):
        super().__init__("- Israel Chacón Rojo",
                         "- Dilan Mauricio García Hernández",
                         "- Jesús Elías Sierra Ruiz")


class PinguinosGalacticos(EquipoMateria):
    def __init__(self):
        super().__init__("- Yahir Antonio Monje Ochoa",
                         "- Yesica Cristina Rodríguez Rentería",
                         "-")


class LosTresMosqueteros(EquipoMateria):
    def __init__(self):
        super().__init__("- Ana Cristina Valenzuela Ruiz",
                         "- Dania Denisse Benavides Figueroa",
                         "- Erick Lozano Duarte")


class WebHeroes(EquipoMateria):
    def __init__(self):
        super().__init__("- Jesus Manuel Arellano Merendon",
                         "- Axel Felipe Reyes Valadez",
                         "- Luis Daniel Delgado Enriquez")


class LosPolystation(EquipoMateria):
    def __init__(self):
        super().__init__("- Erick Fernando Siqueiros Zuñiga",
                         "- Paulina Ixchel Arreguin Ruiz",
                         "-")


fs3 = FS3()
print(fs3)