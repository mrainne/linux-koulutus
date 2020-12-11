# Harjoitus 1 - Versionhallinta Gitissä ja GitHubissa
Alkuperäiset harjoitukset löytyvät osoitteesta (https://github.com/PT-Jaloit/DevOps-Lab). Alkuperäiset ohjeet toimivat Windows ympäristössä ja niissä käytetään VSCodea. Tämä ohje on kirjoitettu linux ympäristöön ja komentorivin käyttäjälle. 
Ohjeessa käydään yksityiskohtaisesti läpi muutama helppo tehtävä askel askeleelta ja se on kirjoitettu osana oppimisprosessia. Ajatuksena on käydä tehtävät läpialusta loppuun ja pyrkiä välttämään ongelmatilanteita.

Merkinnät:
Github – osatehtävä suoritetaan GitHubissa
Tietokone – osatehtävä suoritetaan komentorivillä

## Esivalmistelu
GitHubiin rekisteröityminen (Sign up): (https://github.com/join)
Gitin asennus linuxiin: (https://git-scm.com/download/linux)
Asennuksen jälkeen on hyvä konfiguroida gitiin omat henkilötiedot eli nimi ja sähköpostiosoite:

` git config --global user.name "Oma Nimi" `

` git config --global user.email oma@nimi.com `

Lisätietoa ja ohjeita muihin konfiguraatioihin löytyy täältä (https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

## Versionhallintajärjestelmä harjoitukset
### Luodaan uusi repo GitHubiin
1. GitHub: Uuden repon luominen voidaan aloittaa esimerkiksi seuraavalla tavalla: sivun ylälaidassa olevaa GitHub -logoa klikkaamalla päästään sivulle, jonka vasemmassa laidassa on palsta jonka yläreunassa on teksti Repositories ja vihreä nappi (New). Uuden repon luominen aloitetaan klikkaamalla kyseistä nappia.

![Capture](/Excercise%201/Screencapture/uusi_repo.png?raw=true)

2. GitHub: Luodaan tyhjä repo ja lisätään siihen README -tiedosto.
![Capture](/Excercise%201/Screencapture/create_new_page.png?raw=true)

Kohtaan Repository name kirjoitetaan luotavan repon nimi. Valitaan julkisuus (Public) ja lisätään README tiedosto (Add a README file). Kun halutut valinnat on tehty luodaan repo painalla alalaidassa olevaa vihreää nappia (Create repository).
3. GitHub: Repon URLin kopiointi
Osoite, jolla repoon viitataan löytyy repon sivulta. Osoitetta tarvitaan esimerkiksi repon kloonaamiseen omalle koneelle. Kopiointi onnistuu kuvan osoittamasta paikasta.

![Capture](/Excercise%201/Screencapture/osoitteen_kopiointi.png?raw=true)

4. Tietokone: Luodaan projektille ns. työhakemisto (working directory) ja siirrytään sinne. Tämä ei ole välttämätöntä, mutta voi olla että jotkin kehitystyökalut vaativat tätä. 

` mkdir <projektin_nimi> `

` cd <projektin_nimi> `

Tästä lähtien kaikki komennot suoritetaan tässä hakemistossa ellei toisin mainita.

5. Tietokone: Kloonataan GitHub repo omalle koneelle:

` git clone <kohdassa_3_kopioitu_repositoryn_osoite> `

Kloonaus luo uuden hakemiston, jolla on sama nimi kuin GitHubin repolla. Tässä harjoituksessa luotu hakemisto on siis DevOps-Exc1. Siirrytään hakemistoon `cd`-komennolla.

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

### Haarojen liittäminen yhdeksi
1. GitHub: Uuden pull requestin luominen voidaan aloittaa painamalla sivun yläreunassa olevasta palkista löytyvää Compare and pull request nappia

![Capture](/Excercise%201/Screencapture/pull_request1.png?raw=true)

2. GitHub: tarkasta että yläreunan nappuloissa Base-> mihin haaraan liitosta tehdään (tässä main, mutta voidaan valita myös muita haaroja)  
3. GitHub: Compare-> mitä haaraa ollaan liittämässä
4. GitHub: Isompaan tekstikenttään voi kirjoitella lisätietoa muutoksista. Sivun alalaidassa (ei kuvassa) näkyy mitä muutoksia ollaan liittämässä. Kun ollaan tyytyväisiä pull requestiin voidaan painaa tekstikentän alapuolella olevaa nappia  (Create new pull request). Napin oikeassa laidassa olevasta pienestä valkoisesta kolmiosta avautuu valikko, mistä voi valita ettei pull requestista luodaan ainoastaan luonnos (draft) jota voidaan vielä täydentää ennen varsinaisen pull requestin tekemistä.

![Capture](/Excercise%201/Screencapture/pull_request2.png?raw=true)

5. GitHub: Vahvista muutosten liittäminen. Muutokset eivät aiheuta konflikteja alkuperäisen haaran kanssa, joten haarat voidaan liittää yhteen painamalla vihreää nappia (Merge pull request).

![Capture](/Excercise%201/Screencapture/merge_pr.png?raw=true)

GitHub haluaa kuitenkin vielä varmistaa, että ollaan varmoja siitä että haarat liitetään yhteen. Liitos tehdään lopullisesti painamalla Confirm merge -napista. Se sulkee pull requestin ja liitetyn haaran voi halutessaan poistaa Delete branch -napista. (Tätä ei kannata tehdä vielä, koska samaa haaraa käytetään vielä seuraavassa tehtävässä.)

![Capture](/Excercise%201/Screencapture/confirm_merge.png?raw=true)

### Esimerkkiprojektin koodin kopiointi
1. GitHub: Mene osoitteeseen (https://github.com/shapeshed/express_example)
2. GitHub: Valitse Code -nappulan valikosta Download ZIP.

![Capture](/Excercise%201/Screencapture/download_zip.png?raw=true)

3. Tietokone: Zip-paketin voi kopioida projektihakemistoon ja purkaa sitten tai sen voi purkaa suoraan projektihakemistoon. Paketin purkaminen onnistuu esimerkiksi näin:

`unzip /<polku_hakemistoon_jossa_paketti_sijaitsee>/express_example-master.zip`

Komennolla `ls` voidaan varmistaa, että hakemistoon on ilmestynyt hakemisto nimeltä express_example-master

4. Tietokone: Varmistetaan, että työskennellään oikeassa projektin haarassa antamalla komento `git checkout <edellisissä_tehtävissä_käytetty_haara>`. Jos haara on tuhottu edellisessä tehtävässä se kannattaa käydä luomassa uudestaan (ks. Uuden haaran luominen kohdat 1-3).
5. Tietokone: Lisää muutokset `git add -A`
6. Tietokone: Tee commit `git commit -m "commit_viesti"`
7. Tietokone: Työnnä muutokset GitHubiin `git push`
8. GitHub: express_example-master kansio pitäisi nyt näkyä siinä kehityshaarassa, johon se on lisätty. 


Kun näistä on selvinnyt, voi testailla, mitä tapahtuu, jos GitHub-repoa luodessa tekeekin yksityisen (Private) repon. Tai mitä tapahtuu jos `git checkout` komennossa kirjoittaa haaran väärin. Komennolla `git status` voi seurata tiedostojen tilan muutoksia komentojen välillä. 

Commit-viestien merkitykseen ja siihen millainen on hyvä viesti voi tutustua täällä: (https://medium.com/better-programming/how-to-write-good-commit-messages-and-why-is-it-important-18ac406ce33a)

Pull requestien merkitystä avataan tarkemmin täällä: (https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests)
