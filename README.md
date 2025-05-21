
# 🧪 Exemplo de Teste de Carga em Java com Locust

## 📌 Visão Geral

Este projeto demonstra uma configuração de teste de carga baseada em Java, utilizando o **Locust** para simular tráfego de usuários e avaliar o desempenho de uma aplicação sob diferentes condições de carga. O projeto integra um banco de dados **MySQL** para armazenar e gerenciar dados de teste ou resultados.

É destinado a desenvolvedores e engenheiros de QA que desejam implementar testes de carga em um ambiente Java com o Locust.

---

## ✅ Pré-requisitos

- **Python**: Versão 3.8 ou superior (necessário para o Locust)
- **Java**: Versão 17 ou superior (se o projeto incluir componentes Java)
- **Maven**: Para gerenciamento de dependências e construção do projeto (se aplicável)
- **Docker**: Para executar o container MySQL
- **MySQL**: Versão 8.0 ou superior (via Docker)
- **Locust**: Última versão estável (instalada via pip)

---

## ⚙️ Instruções de Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/Tiago-Santosz/teste-de-carga-java-exemplo.git
cd teste-de-carga-java-exemplo
```

### 2. Configurar o Container MySQL

```bash
docker run -d --name mysql-container \
  -p 3306:3306 \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=testdb \
  mysql:8.0
```

Verifique se o container está ativo:

```bash
docker ps
```

### 3. Configurar o Ambiente do Locust

Instale o Locust com pip:

```bash
pip install locust
```

### 4. Configurar a Aplicação

Atualize as configurações no `application.properties`:

```properties
spring.datasource.url=jdbc:mysql://localhost:3306/testdb
spring.datasource.username=root
spring.datasource.password=root
```

### 5. Construir o Projeto Java (se aplicável)

```bash
mvn clean install
```

---

## 🚀 Executar os Testes de Carga com Locust

1. Navegue até o diretório onde está o `locustfile.py`
2. Execute o Locust com:

```bash
locust -f locustfile.py
```

3. Acesse a interface web do Locust:

```
http://localhost:8089
```

4. Informe:
   - Número de usuários simulados (por exemplo, 10)
   - Taxa de spawn (usuários por segundo, por exemplo, 1)
   - Host da aplicação (por exemplo, http://localhost:8080)

5. Inicie o teste e acompanhe os resultados na interface.

---

## 🗂 Estrutura do Projeto

```
.
├── locustfile.py           # Script principal com cenários de carga
├── src/
│   └── main/java           # Código-fonte Java (se aplicável)
├── docker/                 # Arquivos Docker (se houver)
├── results/                # Resultados dos testes (opcional)
└── README.md
```

---

## 🧠 Uso

- Execute o Locust para simular usuários conforme definido no `locustfile.py`.
- Monitore o MySQL para acompanhar o impacto dos testes.
- Visualize os resultados em tempo real via interface web do Locust.
- Exporte resultados, se necessário, para análise posterior.

