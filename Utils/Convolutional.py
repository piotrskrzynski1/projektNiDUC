import numpy as np
from commpy.channelcoding.convcode import Trellis, conv_encode, viterbi_decode

from Utils.HelperFunctions import SlowoNaTablice, Zlacz8BitoweArrayeNaSlowo


class ConvolutionalCoder:
    # Generator trellis dla kodu splotowego (2,1,3)
    trellis = Trellis(np.array([3]), np.array([[7, 5]]))  # Generatory (7 i 5 w oktalnej)

    @staticmethod
    def __Encode(data_bits):
        """
        Statyczna metoda do kodowania danych splotowych.
        :param data_bits: Tablica 8 elementów do zakodowania (1D numpy array)
        :return: Zakodowana tablica bitów
        """
        if len(data_bits) != 8:
            raise ValueError("Tablica wejściowa musi mieć dokładnie 8 elementów.")

        # Kodowanie splotowe
        encoded_bits = conv_encode(data_bits, ConvolutionalCoder.trellis)
        return encoded_bits.tolist()

    @staticmethod
    def __Decode(encoded_bits,tbDepth):
        """
        Statyczna metoda do dekodowania zakodowanych danych splotowych przy użyciu algorytmu Viterbiego.
        :param encoded_bits: Zakodowana tablica bitów (1D numpy array)
        :return: Odkodowana tablica bitów
        """
        # Konwersja listy na NumPy array, ponieważ viterbi_decode wymaga NumPy array
        encoded_bits_np = np.array(encoded_bits)
        # Dekodowanie przy użyciu algorytmu Viterbiego
        decoded_bits = viterbi_decode(encoded_bits_np, ConvolutionalCoder.trellis, tb_depth=tbDepth)
        decoded_bits = decoded_bits[:8]
        return decoded_bits.tolist()
    @staticmethod
    def Zakoduj(slowo):
        tablicatemp = SlowoNaTablice(slowo)
        codedslowo = []
        for slowko in tablicatemp:
            codedslowo.append(ConvolutionalCoder.__Encode(slowko))
        return codedslowo
    @staticmethod
    def Dekoduj(zakodowaneSlowo,tbDepth,jakoSlowo):
        decodedslowo = []

        for slowko in zakodowaneSlowo:
            decodedslowo.append(ConvolutionalCoder.__Decode(slowko,tbDepth))
        if (jakoSlowo):
            print(decodedslowo)
            slowoCale = Zlacz8BitoweArrayeNaSlowo(decodedslowo)
            return slowoCale
        else:
            return decodedslowo