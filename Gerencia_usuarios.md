# Administração de Usuários

O Unix e o Linux são sistemas operacionais multiusuários, tornando essencial o cadastro de todos os usuários com permissões de acesso diferenciadas. É possível também cadastrá-los em grupos para facilitar o gerenciamento. A criação e administração de contas de usuários no sistema são exclusivas do superusuário (root). Essa é uma tarefa que demanda responsabilidade e deve ser acompanhada com muita atenção.

## Verificando informações do usuário

Todo usuário possui um número chamado User ID (UID) com o qual o sistema Unix/Linux o identifica no sistema. Além do UID, os usuários possuem o Group ID (GID). Toda vez que um processo é ativado, são atribuídos ao processo um UID e um GID. Esses IDs são chamados de identificação efetiva do processo.

### Sintaxe
```bash
id [ opção ] [ nome ]
Exemplos de uso:

	Sem parâmetros, pegando as informações do usuário atual.
leandrors@linuxlemenet:~$ id

uid=1000(leandrors) gid=100(users) proups=16(dialout),33(video),100(users)

	Sem parâmetros, pegando as informações do usuário bin.
leandrors@linuxlemenet:~$ id bin

uid=1(bin) gid=1(bin) groups=1(bin)

	Pegando somente o user id do usuário atual.
leandrors@linuxlemenet:~$ id -u

1000

###Tornando-se outro usuário – Comando su

Permite o usuário mudar sua identidade para outro usuário sem fazer o logout. Útil para executar um programa ou comando como superusuário sem ter que abandonar a seção atual.

Sintaxe: su [-] [usuário]

Onde:

-quando informado, indica para iniciar as configurações do usuário que se está acessando
usuário é o nome do usuário que deseja usar para acessar o sistema. Se não digitado, é assumido o usuário root.
Será pedida a senha do superusuário para autenticação. Digite exit quando desejar retornar a identificação de usuário anterior.
Exemplos de uso:

Vamos primeiramente identificar qual usuário está logado no momento com o coamndo whomai.

leandrors@linuxlemenet:~$ whoami
leandrors

leandrors@linuxlemenet:~$ su

Password:

leandrors@linuxlemenet:~$ whoami

root

###O comando sudo

O comando sudo oferece outra abordagem para permitir que usuários tenham acesso administrativo. Quando um usuário confiável precede um comando administrativo com sudo, o sistema pede que o usuário entre a sua própria senha. Então, após a autenticação, e assumindo que seja permitido, o comando administrativo é executado como se o usuário fosse o root.

Sintaxe: sudo <comando>

No exemplo acima, <comando> seria substituído por um comando normalmente reservado apenas ao usuário root, como, por exemplo, mount.
Importante: Usuários do comando sudo devem tomar cuidado extra para fazer o logout antes de deixarem suas máquinas, já que é possível usar o comando novamente sem precisar indicar a senha, por um período de cinco minutos. Esta configuração pode ser alterada através do arquivo de configuração /etc/sudoers.
Somente os usuários listados no arquivo de configuração /etc/sudoers podem usar o comando sudo e o comando é executado no shell do usuário, e não em um shell do root.
Cada autenticação bem-sucedida é registrada no arquivo /var/log/messages e os comandos submetidos são registrados com o nome do usuário no arquivo /var/log/secure.
Outra vantagem do comando sudo é que um administrador pode permitir que usuários acessem diferentes comandos específicos de acordo com suas necessidades. Administradores que queiram editar o arquivo de configuração do sudo, o /etc/sudoers, devem usar o comando visudo.
Digite visudo e adicione uma linha similar na seguinte na seção de especificação de privilégios do usuário:

leandrors ALL=(ALL) ALL

Este exemplo estabelece que o usuário leandrors pode usar o sudo em qualquer máquina e executar qualquer comando.
O exemplo abaixo ilustra a granularidade possível ao configurar o sudo:

%users localhost=/sbin/shutdown -h now

Este exemplo estabelece que qualquer usuário pode submeter o comando /sbin/shutdown -h now desde que o faça pelo console.
A página man do sudoers tem uma lista detalhada das opções para este arquivo.

###Arquivo passwd e group

O arquivo /etc/passwd é o banco de dados de usuários que podem logar no sistema. Tem um formato de vários campos, separados pelo caracter : ( dois pontos ) e sempre na mesma ordem:

-nome de login do usuário
-senha (criptografada, evidentemenete)
-id do usuário (identificação única, semelhante a um número de carteira de identidade)
-grupo primário deste usuário (o usuário poderá participar de vários grupos)
-nome completo (nome normal, sem ser o login)
-diretório home deste usuário
-shell inicial
-Um exemplo mostra como são estes valores na prática:

leandrors:x:1000:1000:Leandro R. Silva,,,:/home/leandrors:/bin/bash

Quando estamos utilizando shadow password (um pacote que evita o acesso de hackers ao conteúdo das senhas, mesmo criptografadas, para dificultar a tentativa de quebra de senha), o segundo campo é substituído por um * e a senha é armazenada em outro arquivo (/etc/shadow), normalmente inacessível.

O arquivo /etc/group define os grupos aos quais os usuários pertencem. Seu conteúdo são linhas da forma: group_name:passwd:GID:user_list onde group_name _e o nome do grupo.
Um usuário pode pertencer a qualquer número de grupos, e herdará todas as permissões de acesso a arquivos desses grupos. Opcionalmente um grupo pode ter uma senha (campo passwd).
O GID (group id) é um código, como o user id (no arquivo /etc/passwd), mas relativo ao grupo.
Finalmente, user list é a lista (separada por vírgulas) de todos os usuários que pertencem a este grupo.

###Adicionando grupos – comando groupadd

Para facilitar a administração do sistema, pode-se usar o conceito de grupos de usuários com perfis semelhantes. Por exemplo, definir grupos conforme os departamentos de uma empresa.

Sintaxe: groupadd [opções] grupo

Este comando irá alterar os arquivos:

-/etc/group – informações de grupos.
-/etc/gshadow- informações de grupos armazenadas de forma segura (senhas de grupo).
Exemplos de utilização:

 -Criando o grupo vendas
leandrors@linuxlemenet:~$ sudo groupadd vendas
leandrors@linuxlemenet:~$ tail -4 /etc/group
polkituser:x:126:
web200801:x:1001:
bsi200801:x:1002:
vendas:x:1003:

-Criando o grupos alunos com GID 2424
leandrors@linuxlemenet:~$ sudo groupadd -g 2424 alunos
leandrors@linuxlemenet:~$ tail -4 /etc/group
web200801:x:1001:
bsi200801:x:1002:
vendas:x:1003:
alunos:x:2424:

-Criando o grupo teste sem informar o GID (observe que o sistema pega o último GID utilizado e soma 1)
leandrors@linuxlemenet:~$ sudo groupadd teste
leandrors@linuxlemenet:~$ tail -4 /etc/group
bsi200801:x:1002:
vendas:x:1003:
alunos:x:2424:
teste:x:2425:

###Eliminando gupos – Comando groupdel

O comando groupdel permite que se eliminem grupos do sistema. Somente o superusuário poderá utilizar este comando.

Sintaxe: groupdel grupo

Exemplo de utilização:
leandrors@linuxlemenet:~$ sudo groupdel alunos
leandrors@linuxlemenet:~$ sudo groupdel vendas
leandrors@linuxlemenet:~$ sudo groupdel teste
leandrors@linuxlemenet:~$ tail -4 /etc/group
mlocate:x:125:
polkituser:x:126:
web200801:x:1001:
bsi200801:x:1002:
