#from import_arr import first_array
from Amplitude_functions import Amplitudes

import matplotlib.pyplot as plt 
import matplotlib
import numpy as np

def convert_to_microvolts(array):
    arr_for_grafic = []
    for i in array:
        i = i * 1000000
        arr_for_grafic.append(i)

    arr_for_grafic = np.array(arr_for_grafic)  # Преобразуем в массив NumPy для удобства
    arr_for_grafic = arr_for_grafic[:25000]  # Оставляем только до 75,000 
    return arr_for_grafic


def amplitudes_functions(arr_for_grafic):
    amp = Amplitudes()

    main_sig = amp.main_signal(arr_for_grafic)
    amplitudes_for_SKO = amp.array_amplitudes(arr_for_grafic,10)
    amplitudes_for_Mediana = amp.array_amplitudes(main_sig,10)

    amp.averange_mediana_SKO(amplitudes_for_SKO)
    amp.averange_amplitude_mediana(amplitudes_for_Mediana)
    amp.difference_max_min(arr_for_grafic)
    amp.start_end_compression(arr_for_grafic)

def grafic(array):
    plt.figure(figsize=(35,10))
    plt.title('График сжатия челюстной мышцы')  # Устанавливает заголовок графика
    plt.xlabel('Время снятия сигнала')  # Устанавливает метку для оси X
    plt.ylabel('Амплитуда')  # Устанавливает метку для оси Y
    plt.grid()
    plt.plot(array)
    plt.show()



def main_amplitude_info(first_array):
    matplotlib.use('TkAgg') ##backend
    print(f"Backend of project is: {matplotlib.get_backend()}")
    array = convert_to_microvolts(first_array)
    amplitudes_functions(array)
    grafic(array)

