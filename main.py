from Utils.BSC import *
from Utils.GilbertElliot import *
from Utils.Hamming import *
from Utils.HelperFunctions import *
from Utils.Convolutional import *
from Utils.ReedSolomon import *
def main():

    """Kod Hamminga przykład"""
    """
    slowo = "gramy"
    slowocoded = Hamming.ZakodujSlowoHamming(slowo)
    slowodecoded = Hamming.DekodujSlowoHamming(slowocoded,True)

    print(slowo)
    print(slowocoded)
    print(slowodecoded)
    """



    """Kod splotowy przykład"""
    """Kod splotowy przy naszych ustawieniach pozwala naprawić 2 błędy jeżeli sie pojawią w bitpacku"""
    """
    slowo = "Widzowie robimy razem historie" 
    slowocoded = ConvolutionalCoder.Zakoduj(slowo)
    slowoDecoded = ConvolutionalCoder.Dekoduj(slowocoded,10,True)

    print(slowo)
    print(slowocoded)
    print(slowoDecoded)
    """



    """Kod Reeda Solomona przykład"""
    """
    slowo = "gramy"
    symbole = 10
    slowokoded = ReedSolomon.ZakodujReedSolomon(slowo,symbole)
    slowodekoded = ReedSolomon.DekodujReedSolomon(slowokoded,symbole,True)
    print(slowo)
    print(slowokoded)
    print(slowodekoded)
    """


    """Kodowanie Hamminga z kanalem o modelu BSC"""
    """Kod hamminga pozwala nam naprawic 1 blad, a jezeli jest wiecej to lipa"""
    """Kod hamminga w naszym przypadku nie stworzy tablicy tylko wyprintuje gdzie byly bledy (sory)"""
    """Bitpacki i pozycje liczymy od 1 nie od zera"""
    """bitpack to podtablica bitów w naszej wiadomosci"""
    """errorlista pokazuje w ktorych miejscach byl blad (tam gdzie 1 to jest blad"""
    """
    slowo = "gramy"
    slowoCoded = Hamming.ZakodujSlowoHamming(slowo)
    print(slowoCoded)
    slowoCodedAndNoise,errorLista = bsc_channel_transmission(slowoCoded,0.05)
    print(slowoCodedAndNoise)
    print(errorLista)
    slowodecoded = Hamming.DekodujSlowoHamming(slowoCodedAndNoise,True)
    """

    """Kodowanie Hamminga z kanałem o modelu GilbertElliot"""
    """
    slowo = "gramy"
    print(slowo)
    slowoCoded = Hamming.ZakodujSlowoHamming(slowo)
    print(slowoCoded)
    channel = GilbertElliottChannel(0.1,0.9,0.05,0.3)
    slowoCodedAndNoise,errorList = channel.transmit(slowoCoded)
    print(slowoCodedAndNoise)
    print(errorList)
    slowodecoded = Hamming.DekodujSlowoHamming(slowoCodedAndNoise,True)
    print(slowodecoded)
    """

    """Kodowanie Splotowe z kanałem BSC"""
    """
    slowo = "Widzowie tworzymy razem historie"
    slowoCoded = ConvolutionalCoder.Zakoduj(slowo)
    print(slowoCoded)
    slowoCodedAndNoise, errorLista = bsc_channel_transmission(slowoCoded, 0.05)
    slowoDecoded = ConvolutionalCoder.Dekoduj(slowoCodedAndNoise,10, True)
    print(slowoDecoded)
    print(errorLista)
    """

    "Kodowanie Splotowe z kanałem GilbertElliot"
    """
    slowo = "gramy"
    print(slowo)
    slowoCoded = ConvolutionalCoder.Zakoduj(slowo)
    print(slowoCoded)
    channel = GilbertElliottChannel(0.1, 0.9, 0.05, 0.3)
    slowoCodedAndNoise, errorList = channel.transmit(slowoCoded)
    print(slowoCodedAndNoise)
    print(errorList)
    slowodecoded = ConvolutionalCoder.Dekoduj(slowoCodedAndNoise, 10,True)
    print(slowodecoded)
    """

    """Kodowanie Reed Solomon z kanałem BSC"""
    """Uwaga czerwony tekst nie oznacza że nie działa tylko że jest zbyt dużo błędów i trzeba wyslac jeszcze raz, to też nie jest perfekcyjny algorytm!"""
    """
    slowo = "gramy"
    symbole = 10
    slowokoded = ReedSolomon.ZakodujReedSolomon(slowo, symbole)
    print(slowokoded)

    slowokodedandnoise = ReedSolomon.symulacja_bsc(slowokoded,0.02)
    print(f"{slowokodedandnoise}")
    slowodekoded = ReedSolomon.DekodujReedSolomon(slowokodedandnoise, symbole, True)
    print(slowo)

    print(slowodekoded)
    """

    """Kodowanie reed solomon z kanałem gilbert elliot"""
    """
    slowo = "gramy"
    symbole = 10
    slowokoded = ReedSolomon.ZakodujReedSolomon(slowo, symbole)
    print(slowokoded)

    slowokodedandnoise = ReedSolomon.symulacja_gilbert_elliot(slowokoded, 0.01,0.9,0.01,0.1)
    print(f"{slowokodedandnoise}")
    slowodekoded = ReedSolomon.DekodujReedSolomon(slowokodedandnoise, symbole, True)
    print(slowo)

    print(slowodekoded)
    """




if __name__ == '__main__':
    main()

