Version  0.0.1

# Calculator #

* Framework - FastAPI


### Описание ###

####От себя
  Не совсем понятно, для чего нужны квадратные скобки, но с помощью них можно реализовать, приоритет арифметических операции.
  
  В * - 6 * 2 → -11.98 должна быть ошибка или -12
  

###/calc

Принимает в качестве входного значения арифметическое выражение и выдаёт либо ответ, либо ошибку.
Обобщённый вид арифметического выражения: [операция1](число)[(операция2)(число)]*, где:
* операция1: плюс или минус: + -

* операция2: плюс, минус, умножение, деление: + - * /

* число: положительное вещественное число (decimal), имеющее ноль и более знаков после запятой

* круглые скобки: обязательный элемент

* квадратные скобки: необязательный элемент

* звёздочка (*): ноль и более повторений
пробелы игнорируются

####Примеры выражений и результат расчёта (информация по расчёту: см. ниже):
* +100.1 → 100.1
* 0 → 0
* -7 / 34.2 → -0.205
* - 6 * 2 → -11.98
* 2 / 1 → 2
* 5 + - 4 → ошибка
* *1 + 7 → ошибка
* 4 / 3 + → ошибка
####Замечания по расчёту:
* арифметический приоритет операций игнорируется – все операции выполняются слева направо, то есть
выражение 5 - 4 * 2 считается как (5 - 4) * 2, результат: 2
* количество значащих цифр после запятой: до 3 включительно, незначащих нули должны быть обрезаны
* округление математическое: 1.1234 → 1.123, 1.1235 → 1.124

###/history

Конечная точка возвращает последние 30 (по умолчанию) запросов к сервису в формате json (массив), где каждый
запрос/ответ имеет вид:
* Успешно рассчитанный: {"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}
* Запрос с ошибкой: {"request": "5 + - 4", "response": "", "status": "fail"}

Пример ответа для двух запросов: [{"request": "0.01 - 6 * 2", "response": "-11.980", "status": "success"}, {"request": "5
+ - 4", "response": "", "status": "fail"}]


Дополнительные параметры запроса (могут использоваться совместно):
* limit (int) - ограничить количество выводимых запросов; при значениях меньше 1 и больше 30,
возвращается ошибка;
* status (str) - отфильтровать успешные запросы или запросы с ошибкой; допустимые значения: success, fail.
При других значениях возвращается ошибка.

## 2 Игра "Крестики-нолики"
Реализовать программу, играющую в игру Крестики-нолики на поле 3*3
Общие требования

Один запуск программы - одна игра.

Компьютер играет сам с собой за двух игроков. В конце игры выводится история ходов обоих "игроков" и результат

("Ничья", "Выиграл игрок 1", "Выиграл игрок 2")

####Будет плюсом
Возможность задать произвольный размер поля, например 4*20.

Возможность задать количество подряд идущих крестиков/ноликов для победы, например 5 для поля 20*20.

Использование осмысленного алгоритма или иного способа игры компьютера, отличного от случайного
проставления крестиков/ноликов.


### Руководство ###

* Запуск через Serverless Containers
* http://0.0.0.0:8000/docs

### Контакты ###

* 
  Artem Dobrokhvalov
  https://github.com/ADobrokhvalov

* [Описание работы с README](https://bitbucket.org/tutorials/markdowndemo)
