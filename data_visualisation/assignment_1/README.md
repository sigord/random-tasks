# Тестовое задание

## Дано:

файлы с данными по отработанным часам по сотрудникам подрядчиков в разрезе дат за разные месяцы для разных подразделений (одно подразделение - один файл).

## Необходимо:

Подготовить дашборд, отображающий:

1. Общее кол-во сотрудников из выбранного подразделения, за выбранный период по всем подрядчикам. Динамика по дням.  
2. Соотношение долей работающих сотрудников (в процентах) разных подразделений за выбранный период.
3. Общее количество сотрудников, которые работали в выбранный день.
P.S. для решения задачи нужно использовать одно подключение.

## Результат

[Дашборд](https://datalens.yandex/kpv889zmml9ca)

Предобработанные данные находятся в папке *preprocessed_data*

Для предобработки данных предлагается выполнить следующие действия.

1. Установить anaconda
2. ```conda env create --file environment.yml```
3. ```conda activate pandas_env```
4. ```python data_preprocessing.py```
