# CodeCrackCTF

## CTF av Luca Bihoi
  
## Vad CTF uppgiften går ut på
  
Denna CTF uppgiften går ut på att visa sina kunskaper om hackning genom att kunna knäcka denna kedja av uppgifter där man visar att man kan använda sig utav många olika hacknings verktyg så som: nMap, linux, networking, 
sql injections, log in bruteforcing, shh, hashcat, encryption/decryption.

## Uppgiften i sig
  
Som sagt ska man visa att man har kunskap om att kunna använda alla nämnda verktyg för att kunna ta sig igenom. Det börjar med att man måste använda sig utav Nmap för att läsa igenom nätverket för att kunna hitta IP ddressen av den virtuela maskinen som man ska komma 
in på. Efter det ska man använda sig utav hashcat och bruteforcing där man använder sig utav angiva listor av lösenord och försöker logga in på den virtuela maskinen. När man väl är inne på maskinen ska man leta igenom filerna för att hitta en specifik folder som är 
crypterad. Man ska sedan descrypta foldern så att man får tillgång till filena på insidan. Det som är i folder är en application. När man väl kommit in i foldern ska man alltså starta web applicationen och därefter leta efter svagheter i den. Svagheten som man kommer 
hitta är att applicationen skickar in data till en sql databas men gör det på ett osäkert sätt. Man ska då anvönda sig utav sql injections för att få ut data ifrån databasen och i datan man får ut ligger också flaggan med formatet 210s{…}​.

## Svårighetsgrad

Svårighetes graden ligger på 1 alltså svår till nästan omöjlig. Detta är inte pågrund utav att uppgiften i sig är extremt svår utan mer att det är väldigt osannoligt att någon kommer att ha erfarenheten för att se vad nästa steg är och hur man läser steget med korrekt 
hacking verktyg.
