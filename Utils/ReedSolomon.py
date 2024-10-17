from reedsolo import RSCodec
from Utils.HelperFunctions import SlowoNaTablice, Zlacz8BitoweArrayeNaSlowo
import random  # Importujemy random tylko raz na początku

class ReedSolomon:
    @staticmethod
    def __RS_encode(data, n_sym=10):
        """
        Funkcja kodująca dane (lista liczb całkowitych) za pomocą kodu Reeda-Solomona.
        data: lista liczb całkowitych (symboli), które chcemy zakodować
        n_sym: liczba nadmiarowych symboli dodanych do danych (tzw. error-correcting symbols)
        """
        rsc = RSCodec(n_sym)
        # Zamiana listy liczb na bajty
        byte_data = bytes(data)
        # Kodowanie danych
        encoded_data = rsc.encode(byte_data)
        # Zamiana wyniku zakodowanego z powrotem na listę liczb
        return list(encoded_data)

    @staticmethod
    def __RS_decode(received, n_sym=10):
        """
        Funkcja dekodująca dane (lista liczb całkowitych), naprawiająca ewentualne błędy.
        received: lista liczb całkowitych (symboli), które mogą zawierać błędy
        n_sym: liczba nadmiarowych symboli (zgodna z używaną podczas kodowania)
        """
        rsc = RSCodec(n_sym)
        # Zamiana listy liczb na bajty
        byte_data = bytes(received)
        # Próba dekodowania danych i naprawy błędów
        try:
            decoded_data = rsc.decode(byte_data)
            # Zwrócenie tylko odkodowanej części (pierwszy element listy zwróconej przez decode)
            return list(decoded_data[0])  # Zwraca tylko odkodowane dane
        except Exception as e:
            print(f"Nie udało się naprawić błędów: {e}")
            return None

    @staticmethod
    def ZakodujReedSolomon(slowo, symbole):
        slowoTab = SlowoNaTablice(slowo)
        slowokoded = []
        for slowoTemp in slowoTab:
            slowokoded.append(ReedSolomon.__RS_encode(slowoTemp, symbole))
        return slowokoded

    @staticmethod
    def DekodujReedSolomon(slowoKodowane, symbole, jakoSlowo):
        slowodekoded = []
        for slowoTemp in slowoKodowane:
            slowodekoded.append(ReedSolomon.__RS_decode(slowoTemp, symbole))
        if(jakoSlowo):
            slowo = Zlacz8BitoweArrayeNaSlowo(slowodekoded)
            return slowo
        else:
            return slowodekoded

    @staticmethod
    def symulacja_bsc(lista, szansa_odwrocenia):
        """
        Funkcja symulująca kanał BSC (Binary Symmetric Channel).
        Dla każdej liczby w liście i jej bitów, odwraca bit z podaną szansą.

        lista: lista z listami liczb całkowitych (bajty)
        szansa_odwrocenia: prawdopodobieństwo odwrócenia bitu (0.0 do 1.0)
        """
        nowa_lista = []

        for podlista in lista:
            nowa_podlista = []
            for liczba in podlista:
                # Dla każdej liczby (zakładamy, że to 8-bitowy bajt)
                nowa_liczba = 0
                for i in range(8):  # Sprawdzamy każdy bit
                    bit = (liczba >> i) & 1  # Wydobywamy i-ty bit
                    if random.random() < szansa_odwrocenia:
                        # Jeśli losowy wynik jest mniejszy niż szansa, odwracamy bit
                        bit = 1 - bit
                    nowa_liczba |= (bit << i)  # Ustawiamy bit w odpowiedniej pozycji
                nowa_podlista.append(nowa_liczba)
            nowa_lista.append(nowa_podlista)

        return nowa_lista

    @staticmethod
    def symulacja_gilbert_elliot(lista, p_good_to_bad, p_bad_to_good, p_error_good, p_error_bad):
        """
        Funkcja symulująca kanał Gilbert-Elliot.
        Kanał przełącza się między dwoma stanami: dobrym i złym.
        W każdym stanie istnieje różne prawdopodobieństwo wystąpienia błędu.

        lista: lista z listami liczb całkowitych (bajty)
        p_good_to_bad: prawdopodobieństwo przejścia z dobrego stanu do złego
        p_bad_to_good: prawdopodobieństwo przejścia ze złego stanu do dobrego
        p_error_good: prawdopodobieństwo wystąpienia błędu w dobrym stanie
        p_error_bad: prawdopodobieństwo wystąpienia błędu w złym stanie
        """
        nowa_lista = []
        stan = "good"  # Zaczynamy w dobrym stanie

        for podlista in lista:
            nowa_podlista = []
            for liczba in podlista:
                nowa_liczba = 0
                for i in range(8):  # Sprawdzamy każdy bit
                    bit = (liczba >> i) & 1  # Wydobywamy i-ty bit
                    # Decydujemy, czy zmieniamy stan
                    if stan == "good" and random.random() < p_good_to_bad:
                        stan = "bad"
                    elif stan == "bad" and random.random() < p_bad_to_good:
                        stan = "good"

                    # Prawdopodobieństwo błędu zależy od aktualnego stanu
                    if stan == "good":
                        if random.random() < p_error_good:
                            bit = 1 - bit  # Odwracamy bit w dobrym stanie z małą szansą
                    elif stan == "bad":
                        if random.random() < p_error_bad:
                            bit = 1 - bit  # Odwracamy bit w złym stanie z większą szansą

                    nowa_liczba |= (bit << i)  # Ustawiamy bit w odpowiedniej pozycji
                nowa_podlista.append(nowa_liczba)
            nowa_lista.append(nowa_podlista)

        return nowa_lista