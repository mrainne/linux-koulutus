# Harjoitus 1 - Versionhallinta Gitissä ja GitHubissa
Alkuperäiset harjoitukset löytyvät osoitteesta (https://github.com/PT-Jaloit/DevOps-Lab). Alkuperäiset ohjeet toimivat Windows ympäristössä ja niissä käytetään VSCodea. Tämä ohje on kirjoitettu linux ympäristöön ja komentorivin käyttäjälle. 

## Esivalmistelu
GitHubiin rekisteröityminen (Sign up): (https://github.com/join)
Gitin asennus linuxiin: (https://git-scm.com/download/linux)
Asennuksen jälkeen on hyvä konfiguroida gitiin omat henkilötiedot eli nimi ja sähköpostiosoite:
` $ git config --global user.name "Oma Nimi" `
` $ git config --global user.email oma@nimi.com `

Lisätietoa ja ohjeita muihin konfiguraatioihin löytyy täältä (https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)

## Versionhallintajärjestelmä haroitukset
### Luodaan uusi repo GitHubiin
1. GitHub: Uuden repon luominen voidaan aloittaa esimerkiksi seuraavalla tavalla: sivun ylälaidassa olevaa GitHub -logoa klikkaamalla päästään sivulle, jonka vasemmassa laidassa on palsta jonka yläreunassa on teksti Repositories ja vihreä nappi (New). Uuden repon luominen aloitetaan klikkaamalla kyseistä nappia.
![Capture](/Excercise%201/Screencapture/uusi_repo.png?raw=true)
2. Luodaan tyhjä repo ja lisätään siihen README -tiedosto.
![Capture](/Excercise%201/Screencapture/create_new_page.png?raw=true)
Kohtaan Repository name kirjoitetaan luotavan repon nimi. Valitaan julkisuus (Public) ja lisätään README tiedosto (Add a README file). Kun halutut valinnat on tehty luodaan repo painalla alalaidassa olevaa vihreää nappia (Create repository).

1. GitHub: Create new empty github repository (__Create also README file__)
![Capture](/Excercise%201/Screencapture/CreateRepo.png?raw=true)
2. GitHub: Clone or Download repository -> Get URL
![Capture](/Excercise%201/Screencapture/CloneRepoURL.png?raw=true)
3. Computer: Create working directory for project
4. Visual Studio Code: File -> Open Folder
![Capture](/Excercise%201/Screencapture/VSCode_OpenFolder.png?raw=true)
5. Visual Studio Code: Terminal -> New Terminal -> git clone (__Copy Github repository URL Here__)
![Capture](/Excercise%201/Screencapture/VSCode_GitClone.png?raw=true)

### Edit Readme.md
1. Visual Studio Code: Open README.md
2. Visual Studio Code: Edit README.md
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
3. Visual Studio Code: Add Changes
4. Visual Studio Code: Commit changes
5. Visual Studio Code: Push changes to Github
6. GitHub: Check changes

### Create new branch
1. GitHub: Create new branch: Development
2. Visual Studio Code: Pull changes
3. Visual Studio Code: Change branch
4. Visual Studio Code: Change README.md file
5. Visual Studio Code: Add changes, Commit changes
6. Visual Studio Code: Push changes
7. GitHub: Confirm changes

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
