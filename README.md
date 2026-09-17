# GDP Predictor - Предсказатель ВВП

Проект для предсказания ВВП (Валового Внутреннего Продукта) стран мира с использованием машинного обучения.

## О проекте
Этот проект использует линейную регрессию для предсказания значений ВВП на основе исторических данных. Модель обучается на датасете, содержащем данные по ВВП разных стран за несколько десятилетий.

## Данные
Проект использует датасет со следующими полями:
- `Country Name` - название страны
- `Country Code` - код страны (3 буквы)
- `Year` - год данных
- `Value` - значение ВВП в USD

## Структура проекта
```APL_lab4/
├── main.py # Главный скрипт для запуска приложения
├── logic.py # Логика ML модели и предсказаний
├── interface.py # Консольный интерфейс пользователя
├── files/
│ └── gdp_csv.csv # Файл с данными по ВВП
└── README.md # Этот файл
```


## Функциональность
### Основные возможности:
Предсказание ВВП для любой страны и года
- Проверка корректности вводимых данных
- Сравнение предсказаний с реальными значениями (если доступны)
- Визуализация качества модели через графики

### Интерфейс:
- Консольное меню с интуитивным управлением
- Автодополнение и проверка вводимых данных
- Красивое форматирование результатов
- Предупреждения при экстраполяции данных

### ML Модель
Используемые алгоритмы:
- Линейная регрессия из scikit-learn
- Target Encoding для категориальных признаков (коды стран)
- Логарифмическое преобразование для работы с экспоненциальным ростом ВВП

### Качество модели:
- ``*R² score*``: 0.9357 - отличный результат для экономических данных
- График оценки прогноза модели
<img width="900" height="800" alt="image" src="https://github.com/user-attachments/assets/25fb5945-807c-4ed6-95d1-079b9d0ba24e" />
Модель объясняет 93,57% дисперсии данных

## Использование
Пример работы:
```text
Model training...
R²: 0.9357
Available country codes:
['ARB' 'CSS' 'CEB' 'EAR' 'EAS' 'EAP' 'TEA' 'EMU' 'ECS' 'ECA' 'TEC' 'EUU'
 'FCS' 'HPC' 'HIC' 'IBD' 'IBT' 'IDB' 'IDX' 'IDA' 'LTE' 'LCN' 'LAC' 'TLA'
 'LDC' 'LMY' 'LIC' 'LMC' 'MEA' 'MNA' 'TMN' 'MIC' 'NAC' 'OED' 'OSS' 'PSS'
 'PST' 'PRE' 'SST' 'SAS' 'TSA' 'SSF' 'SSA' 'TSS' 'UMC' 'WLD' 'AFG' 'ALB'
 'DZA' 'ASM' 'AND' 'AGO' 'ATG' 'ARG' 'ARM' 'ABW' 'AUS' 'AUT' 'AZE' 'BHS'
 'BHR' 'BGD' 'BRB' 'BLR' 'BEL' 'BLZ' 'BEN' 'BMU' 'BTN' 'BOL' 'BIH' 'BWA'
 'BRA' 'BRN' 'BGR' 'BFA' 'BDI' 'CPV' 'KHM' 'CMR' 'CAN' 'CYM' 'CAF' 'TCD'
 'CHI' 'CHL' 'CHN' 'COL' 'COM' 'COD' 'COG' 'CRI' 'CIV' 'HRV' 'CUB' 'CYP'
 'CZE' 'DNK' 'DJI' 'DMA' 'DOM' 'ECU' 'EGY' 'SLV' 'GNQ' 'ERI' 'EST' 'ETH'
 'FRO' 'FJI' 'FIN' 'FRA' 'PYF' 'GAB' 'GMB' 'GEO' 'DEU' 'GHA' 'GRC' 'GRL'
 'GRD' 'GUM' 'GTM' 'GIN' 'GNB' 'GUY' 'HTI' 'HND' 'HKG' 'HUN' 'ISL' 'IND'
 'IDN' 'IRN' 'IRQ' 'IRL' 'IMN' 'ISR' 'ITA' 'JAM' 'JPN' 'JOR' 'KAZ' 'KEN'
 'KIR' 'KOR' 'XKX' 'KWT' 'KGZ' 'LAO' 'LVA' 'LBN' 'LSO' 'LBR' 'LBY' 'LIE'
 'LTU' 'LUX' 'MAC' 'MKD' 'MDG' 'MWI' 'MYS' 'MDV' 'MLI' 'MLT' 'MHL' 'MRT'
 'MUS' 'MEX' 'FSM' 'MDA' 'MCO' 'MNG' 'MNE' 'MAR' 'MOZ' 'MMR' 'NAM' 'NRU'
 'NPL' 'NLD' 'NCL' 'NZL' 'NIC' 'NER' 'NGA' 'MNP' 'NOR' 'OMN' 'PAK' 'PLW'
 'PAN' 'PNG' 'PRY' 'PER' 'PHL' 'POL' 'PRT' 'PRI' 'QAT' 'ROU' 'RUS' 'RWA'
 'WSM' 'SMR' 'STP' 'SAU' 'SEN' 'SRB' 'SYC' 'SLE' 'SGP' 'SVK' 'SVN' 'SLB'
 'SOM' 'ZAF' 'SSD' 'ESP' 'LKA' 'KNA' 'LCA' 'VCT' 'SDN' 'SUR' 'SWZ' 'SWE'
 'CHE' 'SYR' 'TJK' 'TZA' 'THA' 'TLS' 'TGO' 'TON' 'TTO' 'TUN' 'TUR' 'TKM'
 'TUV' 'UGA' 'UKR' 'ARE' 'GBR' 'USA' 'URY' 'UZB' 'VUT' 'VEN' 'VNM' 'VIR'
 'PSE' 'YEM' 'ZMB' 'ZWE']

Enter country code ('quit' to exit, 'graph' to view the model graph): USA
Enter year(1960-2016): 2001

Prediction for  USA in 2001 year:
9,846,982,559,429.10
Real value: 10,621,824,000,000.00 $
Prediction error: 7.29%
```

## Технические детали
Ключевые библиотеки:
- pandas - работа с данными
- numpy - математические операции
- scikit-learn - машинное обучение
- matplotlib - визуализация
- category_encoders - кодирование категориальных признаков
