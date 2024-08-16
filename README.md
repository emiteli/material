## create a new repository on the command line
* echo "# material" >> README.md

* git init
* git add README.md
* git commit -m "first commit"
* git branch -M main
* git remote add origin https://github.com/emiteli/material.git
* git push -u origin main

### …or push an existing repository from the command line
* git remote add origin https://github.com/emiteli/material.git
* git branch -M main
* git push -u origin main

====================================================================
Para Executar Totvs.wxs

Priemiro voce vai usar o comando cadle.exe para gerar o arquivo.wixobj
candle.exe totv.wxs

Depois quer gerar o arquivo voce faz seguinte comando
light.exe totv.wixobj -o setup.msi
