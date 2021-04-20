# Pong

Pong-tyylinen yhden pelaajan videopeli

## Dokumentaatio

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Pelin testaaminen komentoriviltä

1. ```bash
    poetry install
   ``` 
    Asentaa tarvittavat riippuvuudet

2. ```bash
    poetry run invoke start
   ```
    Avaa pelisovelluksen

3. ```bash
    poetry run invoke test
   ```
    Ajaa sovelluksen testit

4. ```bash
    poetry run invoke coverage-report
   ```
    Kerää testien haarautumakattavuuden ja luo index.html raportin htmlcov hakemistoon

5. ```bash
    poetry run invoke lint
   ```
    Pylinter