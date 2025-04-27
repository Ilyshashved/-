import numpy as np

class Amplitudes:

    # Функция которая выделяет часть сигнала сжатия челюстных мышц
    def main_signal(self,array):
        return array[5000:-5000] #часть сигнала со сжатием ,без состояния покоя

    # Функция которая вощвращает массив с амплитудами ,промежуток определяет  segment_size
    def array_amplitudes (self,array, segment_size) : # Определение массива амплитуд всего сигнала, seg_size определяет кол-во индексов
        amplitudes = []  # Массив для хранения амплитуд
        # Проходим по массиву с шагом segment_size
        for i in range(0, len(array), segment_size):
            # Определяем сегмент массива
            segment = array[i:i + segment_size]

            max_value = max(segment)
            min_value = min(segment)
            amplitude = max_value - min_value
            amplitudes.append(amplitude)  # Добавляем амплитуду в массив
        return amplitudes


    # Определение Среднего Значения и Стандартного Отклонения
    # Среднее значение (математическое ожидание) — это сумма всех значений, деленная на количество значений. Оно дает представление о "центре" данных.
    # Стандартное отклонение — это мера разброса значений вокруг среднего. Оно показывает, насколько сильно значения отклоняются от среднего. Чем больше стандартное отклонение, тем больше разброс.
    def averange_mediana_SKO (self,amplitudes):
        mean = np.mean(amplitudes) # Вычисляем среднее ариифметическое значение
        std_dev = np.std(amplitudes) # Вычисляем стандартное отклонение
        averange_amplitude = mean + std_dev # сркдняя амплитуда
        print(f"средняя амплитуда: {mean}\nСКО: {std_dev}\nСредняя амплитуда: {averange_amplitude}")

    # Определение среднего медианного значения
    def averange_amplitude_mediana(self,amplitudes):
        sorted_amplitudes = np.sort(amplitudes)
        N = len(sorted_amplitudes)
        if N % 2 == 0:
            median_amplitude = (sorted_amplitudes[N//2 - 1] + sorted_amplitudes[N//2]) / 2
        else:
            median_amplitude = sorted_amplitudes[N//2]

        print("Медианная амплитуда:", median_amplitude)

    # Амплитуда от пика до пика — разница между максимальным и минимальным значениями
    def difference_max_min(self,array):
        maximum = max(array)
        print(f"Максимальная амплитуда положительной часмти сигнала: {maximum}")
        minimum = min(array)
        print(f"Минимальная амплитуда отрицательной части сигнала: {minimum}")
        difference = maximum + abs(minimum)
        print(f"Амплитуда от пика до пика: {difference}")     

    # Момент начала и окончания мышечной активности — на основе пороговых значений или алгоритмов пороговой фильтрации
    def start_end_compression(self,array):
        std_dev = np.std(array) #пороговое значение
        start = None
        end = None
        for i in range(len(array)):
            if (array[i] > std_dev and array[i+1] > std_dev):
                start = i
                break

        for i in range(len(array)-1, -1, -1):
            if (array[i] > std_dev and array[i+1] > std_dev):
                end = i
                break
        print(f"Начало сжатия: {start}\nКонец сжатия: {end}")
        print(f"Пороговое значение равное средне квадратичному отклонению: {std_dev}")


