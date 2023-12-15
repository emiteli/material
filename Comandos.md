### Caminho de arquivos

Sempre que precisamos localizar um arquivo para efetuar qualquer operação (ler, gravar, remover, criar, etc.) Devemos saber onde no sistema operacional esse arquivo se encontra resumindo devemos conhecer em que ponto do sistema de arquivos ele se encontra. Isto é feito através da especicação de um caminho antes do nome do arquivo. Este caminho, chamado de path, pode ser indicado de duas maneiras:

Absoluto – O caminho absoluto sempre começa com uma barra (“/”). Este caminho da a
localização do arquivo desde o diretório raiz do sistema. O sistema operacional, começa pela
raiz e vai seguindo os diretórios indicados até o último.

Relativo – A procura de um arquivo através de um caminho relativo começa no próprio
diretório atual da sessão.

## Comandos básicos

A linha de comando do sistema operacional Unix permite a realização de inúmeras tarefas através de seus comandos, de manipulação de arquivos a verificação do tráfego em rede etc… Para exibir uma descrição detalhada de cada comando abra uma console e digite man comando, para ver o manual do comando em questão.

### Comandos de manipulação de diretório
Comandos | Legenda
-------------------------------------------------------------------------------------
* mkdir	 | cria um diretório vazio exemplo: mkdir docs
* rmdir	 | exclui um diretorio (se estiver vazio)
* rm -rf | exclui um diretório e todo o seu conteúdo (cuidado com este comando)
* cd	   | entra num diretório (exemplo: cd docs) ou retorna para HOME
* cd /	 | muda para o diretório raiz
* cd ~	 | vai direto para o diretório home do usuário logado.
* cd –	 | volta ao último diretório acessado
* pwd	   | exibe o local do diretório atual
* ls	   | lista o conteúdo do diretório
* ls -alh| mostra o conteúdo detalhado do diretório
* ls -a	 | Exibe os arquivos “ocultos” do determinado diretório.
* ls -ltr| mostra os arquivos no formado longo(l) em ordem inversa(r) de data (t)
* df	   | mostra a utilização dos sistemas de arquivos montados
* du -msh| mostra o tamanho do diretório em Megabytes
* whereis| mostra onde se encontra determinado arquivo (binários) exemplo: whereis samba
## Comandos Úteis
Comandos | Legenda
-------------------------------------
* startx   | Carrega o modo gráfico
* clear	   | Limpa a tela
* exit     | Logoff
* reboot	 | einiciar máquina
* halt	   | Desliga máquina
* dir      | Mostra arquivos
* cd	     | Volta a pasta raiz
* cd ..	   |Volta ao diretório anterior
* mouseconfig|	Configura mouse
* ifconfig | Mostra endereço da placa de rede
* hostname | Mostra o nome da máquina
* history	 | Mostra os últimos 1000 comandos digitados
* kbdconfig| Configura teclado
* who	     | Quem está na rede
* pwd	     | Local onde você está
* sax	     | Configuração multimídia em modo texto
* sax2	   | Configuração multimídia em modo gráfico
* man      | nome do comando	Help
* useradd  | nome do usuário	Adiciona usuário
* passwd   | nome do usuário	Adiciona senha ao usuário
* userdel  | nome do usuário	Remove usuário
* userdel -r| nome do usuário	Remove usuário e sua pasta
* groupadd | nome do grupo	Adiciona grupo
* adduser  | nome do usuário -g nome do grupo	Cria e adiciona usuário ao grupo
* groupdel | nome do grupo	Remove grupo
* ls -la	Mostra pastas e subpastas com as permissões
* lspci -v | more	Mostra os drivers das placas
* ps -df	 | Mostra processos em andamento
* df -h	   | Mostra tamanho do disco raiz
* uname -a |Mostra informações sobre o kernel da máquina
* netstat -ln	|Mostra portas escutando possíveis conexões
* rcxdm restart|	Reinicia servidor gráfico
* cat /etc/hosts|	Mostra nomes e IPs das máquinas na rede
* cat /etc/passwd|	Mostra usuários
* cat /etc/group|	Mostra grupos
* chkconfig | more	Estado dos serviços iniciados com o sistema
* chkconfig nome_serviço|	Verifica estado do serviço
* chkconfig nome_serviço| on ou off	Iniciar ou não o serviço junto com o sistema
* ls " |tee saida.txt"| O comando tee permite que a saída de um comando seja gravada em um arquivo ao mesmo tempo em que é exibida na tela.
