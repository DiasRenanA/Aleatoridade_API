import random
class Aleatoridade():
    def Dois_ou_Um(self,nomes : list[str]) -> dict:
        random.shuffle(nomes)
        Dupla1 = [nomes[0],nomes[1]]
        Dupla2 = [nomes[2],nomes[3]]
        Resultado = {
            "Dupla 1" : Dupla1,
            "Dupla 2" : Dupla2
        }
        return Resultado


if __name__=="__main__":

    print(Aleatoridade().Dois_ou_Um(['Renan','Eduardo','Caio','Wender']))