## Sistema de Arquivos

O **Sistema de Arquivos** é uma estrutura lógica que possibilita o armazenamento e recuperação de arquivos. No Unix, arquivos são contidos em diretórios (ou pastas), conectados em uma árvore que se inicia no diretório raiz (designado por `/`). Mesmo arquivos em dispositivos de armazenamento diferentes (discos rígidos, disquetes, CDs, DVDs, sistemas de arquivos em rede) precisam ser conectados à árvore para que seu conteúdo seja acessado. Cada dispositivo de armazenamento possui sua própria árvore de diretórios.

O processo de conectar a árvore de diretórios de um dispositivo de armazenamento à árvore de diretórios raiz é chamado de *montar dispositivo de armazenamento* (montagem) e é realizado por meio do comando `mount`. A montagem associa o dispositivo a um subdiretório.

## Estrutura de Diretórios

A árvore de diretórios do Unix é dividida em várias ramificações menores e pode variar de uma versão para outra. Os diretórios mais comuns são os seguintes:

- **/**: Diretório raiz – este é o diretório principal do sistema. Dentro dele estão todos os diretórios do sistema.

- **/bin**: Contém arquivos, programas do sistema, que são usados com frequência pelos usuários.

- **/boot**: Contém arquivos necessários para a inicialização do sistema.

- **/dev**: Contém arquivos usados para acessar dispositivos (periféricos) existentes no computador.

- **/etc**: Arquivos de configuração de seu computador local.

- **/home**: Diretórios contendo os arquivos dos usuários.

- **/lib**: Bibliotecas compartilhadas pelos programas do sistema e módulos do núcleo.

- **/mnt**: Diretório de montagem de dispositivos.

  - **/mnt/cdrom**: Subdiretório onde são montados os CDs. Após a montagem, o conteúdo do CD se encontrará dentro deste diretório.

  - **/mnt/floppy**: Subdiretório onde são montados os disquetes. Após a montagem, o conteúdo do disquete se encontrará dentro deste diretório.

- **/proc**: Sistema de arquivos do núcleo *Kernel*. São arquivos utilizados pelo kernel do sistema e são utilizados por diversos programas e dispositivos.

- **/root**: Diretório do usuário root.

- **/sbin**: Diretório de programas usados pelo superusuário (root) para administração e controle do funcionamento do sistema.

- **/tmp**: Diretório para armazenamento de arquivos temporários criados por programas.

- **/usr**: Contém a maior parte de seus programas. Normalmente acessível somente como leitura.

- **/var**: Contém a maior parte dos arquivos que são gravados com frequência pelos programas do sistema.

