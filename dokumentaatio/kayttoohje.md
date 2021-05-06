# Käyttöohje

Lataa ohjelman suoritukseen tarvittava koodi täältä [release](https://github.com/mikaelvilen/ot-harjoitustyo/releases). Valitse viimeisin Release (tag viikko7).

## Ohjeet asennukseen

1. ```bash
    poetry install
   ``` 
    Asentaa tarvittavat riippuvuudet

2. ```bash
    poetry run invoke build
   ```
    Alustaa tietokannan

3. ```bash
    poetry run invoke start
   ```
    Avaa pelisovelluksen

## Pelin pelaaminen

Peli on muunnos tunnetusta Pong videopelistä. Pelaaja liikuttaa mailaa nuolinäppäimillä ylös tai alas ja pyrkii selviämään pelissä mahdollisimman pitkään. Pallon nopeus kasvaa pelin edetessä. Pelin alussa näytetään huipputulokset, jos pelin jälkeen olet saanut paremman tuloksen, kysytään kirjoittamaan nimi, ja tuloksesi tallennetaan tietokantaan ja näytetään ruudulla.