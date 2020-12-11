# Harjoitus 1 - Versionhallinta Gitissä ja GitHubissa
Alkuperäiset harjoitukset löytyvät osoitteesta (https://github.com/PT-Jaloit/DevOps-Lab). Alkuperäiset ohjeet toimivat Windows ympäristössä ja niissä käytetään VSCodea. Tämä ohje on kirjoitettu linux ympäristöön ja komentorivin käyttäjälle. 

## Esivalmistelu
GitHubiin rekisteröityminen (Sign up): (https://github.com/join)
Gitin asennus linuxiin: (https://git-scm.com/download/linux)
Asennuksen jälkeen on hyvä konfiguroida gitiin omat henkilötiedot eli nimi ja sähköpostiosoite:

` git config --global user.name "Oma Nimi" `

` git config --global user.email oma@nimi.com `

Lisätietoa ja ohjeita muihin konfiguraatioihin löytyy täältä (https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

## Versionhallintajärjestelmä haroitukset
### Luodaan uusi repo GitHubiin
1. GitHub: Uuden repon luominen voidaan aloittaa esimerkiksi seuraavalla tavalla: sivun ylälaidassa olevaa GitHub -logoa klikkaamalla päästään sivulle, jonka vasemmassa laidassa on palsta jonka yläreunassa on teksti Repositories ja vihreä nappi (New). Uuden repon luominen aloitetaan klikkaamalla kyseistä nappia.
![Capture](/Excercise%201/Screencapture/uusi_repo.png?raw=true)
2. GitHub: Luodaan tyhjä repo ja lisätään siihen README -tiedosto.
![Capture](/Excercise%201/Screencapture/create_new_page.png?raw=true)
Kohtaan Repository name kirjoitetaan luotavan repon nimi. Valitaan julkisuus (Public) ja lisätään README tiedosto (Add a README file). Kun halutut valinnat on tehty luodaan repo painalla alalaidassa olevaa vihreää nappia (Create repository).
3. GitHub: Repon URLin kopiointi
Osoite, jolla repoon viitataan löytyy repon sivulta. Osoitetta tarvitaan esimerkiksi repon kloonaamiseen omalle koneelle. Kopiointi onnistuu kuvan osoittamasta paikasta.
![Capture](/Excercise%201/Screencapture/osoitteen_kopiointi.png?raw=true)
4.< Tietokone: Luodaan projektille ns. työhakemisto (working directory) ja siirrytään sinne. Tämä ei ole välttämätöntä, mutta voi olla että jotkin kehitystyökalut vaativat tätä. 

` mkdir <projektin_nimi> `

` cd <projektin_nimi> `

5. Tietokone: Klooanataan GitHub repo omalle koneelle:

` git clone <kohdassa_3_kopioitu_repositoryn_osoite> `

Kloonaus luo uuden hakemiston, jolla on sama nimi kuin GitHubin repolla. Tässä harjoituksessa luotu tiedosto on siis DevOps-Exc1. Siirrytään hakemistoon `cd`-komennolla.

### README.md tiedoston editointi
1. Tietokone: Avataan tiedosto README.md tekstieditorilla
2. Tietokone: Tehdään tiedostoon seuraavat muutokset, tallennetaan ja suljetaan tiedosto.
```
* Bullet point
1. Luettelo
2. Luettelo 2

_Italic_

__Bold__

*Italic*

**Bold**

# Otsikko
## 2-tason otsikko
### 3-Tason otsikko
(www.google.fi) URL-osoite
```
3. Tietokone: lisätään muutokset `git add README.md`
4. Tietokone: tehdään commit `git commit -m "<commit-viesti>"`
(Kohdat 3. ja 4. voidaan yhdistää komentoon: `git commit -a -m "<commit-viesti>")
5. Tietokone: työnnetään muutokset GitHubiin `git push`, jos kone pyytää käyttäjätunnusta ja salasanaa, niihin syötetään GitHubin käyttäjätunnus ja salasana.
6. GitHub: Tehdyt muutokset pitäisi nyt näkyä myös GitHubin README.md -tiedostossa.

### Uuden haaran luominen
1. GitHub: Luodaan uusi haara: Development
Klikataan kuvan mukaista nappia ja kirjoitetaan tekstikenttään uuden haaran nimi (esim. Development) ja painetaan enteriä. Kannattaa painaa mieleen uuden haaran tarkka kirjoitusasu, sillä on merkitystä myöhemmässä vaiheessa.
![Capture](/Excercise%201/Screencapture/uuden_haaran_luonti.png?raw=true)
2. Tietokone: haetaan GitHubiin tehdyt muutokset paikalliseen repoon komennolla`git pull` (huomataan, että git kertoo uuden haaran olemassaolosta).
3. Tietokone: Vaihdetaan uuteen haaraan komennolla `git checkout <haaran_nimi>`, haaran nimi on tässä vaiheessa oltava sama kuin kohdassa 1. Ellei se ole, tulee kohdassa 6. virheilmoituksia ongelmista, kun paikallisessa versiossa on haara, jota ei löydy GitHubista.  
4. Tietokonen: Tehdään jotain muutoksia README.md -tiedostoon.
5. Tietokone: Lisätään ja commitoidaan muutokset `git add .` ja `git commit -m "commit_viesti". Käyttämällä `git add .` ei tarvitse erikseen kirjoittaa kaikkien lisättävien tiedostojen nimiä, mikä säästää aikaa, jos lisättävänä on useita tiedostoja. Komento `git add -A` tekee saman asian. 
6. Tietokone: Työnnetään muutokset Githubiin `git push`
7. GitHub: Ellei tekemäsi muutos näy GitHubissa sivun uudelleen lataamisen jälkeen klikkaa samaa nappulaa kuin 1. kohdassa ja valitse sieltä haara (branch), johon teit muutoksia. 

### Merge Branches
1. GitHub: Chose Pull request tab
2. GitHub: New pull request
3. GitHub: Base-> master
4. GitHub: Compare-> development
5. GitHub: Check changes and chose -> Create new pull request
6. GitHub: Merge changes

### Copy example project code to github
1. GitHub: (https://github.com/shapeshed/express_example)
2. GitHub: Clone or Download -> Download ZIP
3. Computer: Copy contents of ZIP file to your Project
4. Visual Studio Code: Make sure that you are working with development, change branch to development
5. Visual Studio Code: Add changes
6. Visual Studio Code: Commit changes
7. Visual Studio Code: Push changes to GitHub
8. GitHub: Confirm changes
