# Työsuunnitelma

Asennetaan VMWare Workstation 16 Prolla kaksi CentOS 8 serveriä (Server01, Server02) ja yksi CentOS 8 työasema (wks1), käyttäen verkosta ladattua asennuspakettia.

## Server01
Asennus:
* asennuksessa asetetaan kiinteä ip 172.19.20.10
* lisätään jo asennusvaiheessa toinen 20GB levy jaettuja kansioita varten 

Muut toimenpiteet:
* asennetaan ja konfiguroidaan dnsmasq
* luodaan käyttäjät (2 kpl) ja osastojen käyttäjäryhmät
* luodaan osastokohtaiset hakemistot ja määritellään niiden käyttöoikeudet
* asenneteaan ja konfiguroidaan `nfs`
* asennetaan backup-ohjelma (`rsync`) ja konfiguroidaan päivittäiset varmistukset (jälkimmäinen tehdään kun Server02 on asennettu ja valmisteltu)
* ssh-konfigurointi käyttämään pelkkiä avaimia (wks1 asennuksen ja avainten generoinnin ja testaamisen jälkeen), estetään kirjautuminen pelkällä salasanalla
* varmistetaan tietojen palautus backupeista

## Server02
Asennus:
* asennuksessa asetetaan kiinteä ip: 172.19.20.11
* lisätään asennuksen jälkeen toinen levy (30GB), partitioidaan ja mountataan levy käsin ja määritellään mounttaus koneen käynnistyksen yhteydessä.

Muut toimenpiteet:
* Server01 varmistukset tallennetaan edellä luodulle partitiolle, joka on mountattu hakemistoon `/backups` 
* muut tarvittavat konfiguraatiot varmistuksiin ja varmistusten palauttamiseen.

## wks1
Asennus:
* verkkoasetuksissa DHCP

Muut toimenpiteet:
* luodaan käyttäjät (luodaan asennusvaiheessa yksi ei-root käyttäjä ja toinen käyttäjä asennuksen)
* luodaan osastojen käyttäjäryhmät ja liitetään käyttäjät oikeisiin ryhmiin
* generoidaan käyttäjille ssh-avaimet ja kopioidaan ne palvelimelle
* asennetaan `nfs`
* luodaan mount pointit jaetuille kansioille ja mountataan kansiot
* luodaan käyttäjien kotihakemistoihin linkitys jaettuihin hakemistoihin


