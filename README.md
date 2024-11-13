WareHouse Management System

Цели данного кода заключаются в следующем: 

1. Фильтрация товаров: Основная цель кода – предоставить возможность пользователям находить товары на складе, соответствующие заданным критериям. Это может быть полезно для складского учета, логистики или управления запасами. 
2. Удобство использования: Код прост в использовании и гибок для изменения параметров фильтрации. Пользователь может задать различные диапазоны значений для веса, высоты, ширины и объема, чтобы найти нужные товары. 
3. Автоматизация процесса поиска: Автоматизированный процесс фильтрации товаров значительно упрощает работу сотрудников склада или менеджеров, позволяя быстро находить необходимые позиции без ручного перебора всех товаров. 
4. Повышение точности: Использование точных критериев фильтрации помогает избежать ошибок при поиске нужных товаров, особенно когда ассортимент велик и разнообразен. Таким образом, данный код направлен на оптимизацию процессов поиска и управления товарами на складе.

Установка

Для запуска скрипта вам потребуется установленная  PyCharm . Скопируйте файлы проекта и запустите их локально.

Использование

1. Откройте файл code.py.
2. Задайте критерии фильтрации в словаре criteria. Например:
   

       criteria = {
   
         'weight_min': 9,
     
         'weight_max': 16,
     
         'height_min': 19,
     
         'height_max': 26,
     
         'width_min': 29,
     
         'width_max': 36,
     
         'volume_min': 5000,
     
         'volume_max': 9000,
   
       }

3. Запустите скрипт командой:
      
         python code.py

4. Результаты будут выведены в консоль.


      Пример вывода результатов фильтрации:
   

      Товар A: Вес 10, Высота 20, Ширина 30, Объем 6000
      Товар B: Вес 15, Высота 25, Ширина 35, Объем 8750
