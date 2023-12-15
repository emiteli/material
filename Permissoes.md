###Introdução
As permissões são um dos aspectos mais importantes do Linux (na verdade, de todos os sistemas baseados em Unix). Elas são usadas para vários fins, mas servem principalmente para proteger o sistema e os arquivos dos usuários. Manipular permissões é uma atividade interessante, mas complexa ao mesmo tempo. Mas tal complexidade não deve ser interpretada como dificuldade e sim como possibilidade de lidar com uma grande variedade de configurações, o que permite criar vários tipos de proteção a arquivos e diretórios. Como você deve saber, somente o super-usuário (root) tem ações irrestritas no sistema, justamente por ser o usuário responsável pela configuração, administração e manutenção do Linux. Cabe a ele, por exemplo, determinar o que cada usuário pode executar criar, modificar, etc. Naturalmente, a forma usada para especificar o que cada usuário do sistema pode fazer é a determinação de permissões. Sendo assim, neste artigo você verá como configurar permissões de arquivos e diretórios, assim como modificá-las.
 **As permissões** são usadas para definir quem pode acessar determinados arquivos ou diretórios, assim mantendo segurança e organização em seu sistema e sua rede.  Então, respire fundo e vamos lá… 🙂

Cada arquivo ou pasta possuem 3 permissões.
(Usuário Dono) (Grupo Dono) (outros) onde:

* Usuário dono: é o proprietário do arquivo;
* Grupo Dono: é um grupo, que pode conter vários usuários;
* Outros: se encaixam os outros usuários em geral.

Para ver a permissão de um arquivo digite no prompt:
$ ls -l
O comando “ls -l” faz uma listagem longa e detalhada no diretório atual.
As permissões vão aparecer assim:

* (r) Leitura
* (w) Escrita
* (x) Execução
Como as permissões são divididas em 3, irá aparecer assim:
(_ _ _) (_ _ _) (_ _ _), ou seja, (rwx)(rwx)(rwx)
Caso não haja todas as permissões, poderá aparecer incompleto:

rwxrw_ _ _x, ou seja, neste exemplo:

Dono do arquivo tem permissão de:

* Ler, Escrever e executar (rwx);
* Grupo tem permissão de Ler e Escrever (rw_);
* Outros têm permissão apenas de executar. (_ _ x);

Existem dois modos de definir uma permissão, através do modo Octal e modo Textual.
Textual usamos letras antes das permissões (chmod é o comando para modificar permissões de arquivos):
$ chmod u+rw, g+w, o-rwx teste.txt
Onde:

* U – representa usuário;
* G – representa grupo;
* O – representa outros.
Vejamos então “ugo” ok*

Agora vejam o modo Octal.
O modo Octal tem a mesma função de definir permissões, só que em números.
Vejamos então:
$ chmod 620 teste.txt

(comando) (permissão) (arquivo)
Tipo de permissão Octal:

* 4 – Indica permissão de leitura;
* 2 – Permissão de escrita;
* 1 – Indica permissão de execução;
* 0 – Indica sem permissões.

Agora é simples, é só somar e ditar as permissões, exemplo:
* 4 + 2 + 1 = 7 (permissão de rwx)
* 4 + 2 = 6 (permissão rw)
* 4 = (permissão r)

Exemplo: A permissão 610 indica que o arquivo tem permissão:
* 6 para dono do arquivo
* 1 para grupo e
* 0 para outros ou seja
dono= (rw_) Grupo=(_ _ x) outros=(_ _ _)

Percebam que quando é feita a listagem longa “ls -l”, o primeiro caractere não é uma permissão.
Surge algo como:
drwxr—— usuário users Feb 12   2009 Desktop
drwxr—— usuário users Feb 12   2009 Documentos
drwxr-xr-x usuário users Feb 12   2009 bin
drwxr-xr-x usuário users Feb 12   2009 public_html

Perceba que o primeiro caracter “d” indica o tipo do arquivo, neste caso “d” indica que é um diretório.

Permissões de Acesso Especiais

Agora que você ja conhece um pouco de permissões acesse o Guia Foca para saber sobre permissões de acesso especial.

http://focalinux.cipsga.org.br/guia/iniciante/ch-perm.htm#s-perm-especiaiss
