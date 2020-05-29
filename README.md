# Gestor-de-Gastos
<p>Este sistema tem como objetivo gerenciar os próprios gastos e recebimentos de uma forma prática, podendo ser utilizado direto no pen-drive. É inteiramente criptografado, desde o nome das pastas até o conteúdo dos arquivos.</p>
  
<h2>Como instalar?</h2>
<p>É necessário colocar o arquivo Instalador.py na mesma pasta que a pasta PyFiles. Após isso, deve-se executar o instalador, que irá fazer a instalação, gerando um executável.</p>

<h2>Como funciona?</h2>
<p>Dentro da pasta PyFiles tem o Controle_Gastos.Py e o Classes.txt. Este último arquivo contém código python, sendo que conforme o Instalador.py é executado, o seu conteúdo é alterado e o nome do arquivo mudado para Classes.py. Com isso, garante-se que uma nova chave criptográfica seja criada e colocada diretamente no código fonte (cada programa possui a sua própria chave).</p>
<p>Após a renomeação do arquivo, é verificado se o PyInstaller está instalado na máquina (biblioteca que permite gerar executável a partir de um .py), e caso não esteja, o programa permite que seja feita a instalação. Por fim, é gerado o executável e uma limpeza é feita, deixando na pasta apenas o arquivo executável e a chave criptográfica (que precisa ser guardada em um local seguro).</p>

<h2>Requisitos mínimos</h2>
<ul>
  <li>Ter o pip instalado na máquina</li>
  <li>Ter permissão para criação, edição e visualização de arquivos</li>
  <li>Sistema operacional Windows</li>
</ul>

<h2>Opções dentro do programa</h2>
<ul>
  <li>Adicionar tipos de despesa</li>
  <li>Adicionar formas de pagamento</li>
  <li>Adicionar despesas</li>
  <li>Adicionar despesas parceladas</li>
  <li>Adicionar recebimentos</li>
  <li>Fazer consultas de todos os ítens acima</li>
  <li>Fazer exclusão de despesas e recebimentos</li>
</ul>
