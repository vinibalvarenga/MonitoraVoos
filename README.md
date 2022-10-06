# MonitoraVoos

O seguinte projeto diz respeito ao desenvolvimento de um sistema de monitoramento de voos de aviões.

## Grupo 6

Nome      | NUSP
--------- | ------
Dênio Araujo de Almeida   | 10309013
Vinícius Barros Alvarenga | 11257564
Yuri de Sene Alvizi       | 11260398

### Pré-requisitos

* Python 3.6+

## Passo a passo da instalação

1. Abra um terminal powershell (instruções para Windows).

2. Clone o repositório do grupo. No terminal, digite o comando:

```
  git clone https://github.com/vinibalvarenga/MonitoraVoos.git
```

3. Entre na pasta **MonitoraVoos**:

```
  cd MonitoraVoos
```

4. Crie um ambiente virtual chamado **env** usando:

```
  python -m venv env
```

5. Ative o ambiente usando o comando:

```
  .\env\scripts\Activate.ps1
```

6. Instale as dependências:

```
pip install -r requirements.txt
```

### Executar o projeto

1. Ainda no mesmo terminal, digite o comando:

```
  python manage.py runserver
```

2. Abra um navegador web e abra a seguinte página: <http://localhost:8000/FIRST>.

### Mapeamento O-R

O projeto do monitoramento dos voos se baseia no seguinte mapeamento:

![alt text for screen readers](/MonitoraVoos/docs/img/ModeloOR.png "Mapeamento O-R do projeto")