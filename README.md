# Fluxo avançado com SZ.Chat
Esse material é para orientar pessoas a utilizar o módulo de RPA no SZ.Chat a fim de fazer suas próprias integrações e automatizar processos no fluxo do atendimento.

# Pré-requisitos
Toda integração requer a documentação das APIs a serem integradas, sem essas informações não é possível realizar nenhuma integração.

# Cenário
Imagine que um cliente queira fazer o seguinte fluxo<br>

Cliente entra no Chat e quer abrir um chamado, porém só é permitido abrir o chamado caso o cliente esteja em dia com seus pagamentos.

* Consultar no CRM via CNPJ a situação do cliente
* Se o cliente estiver em dia, ele pode entrar com a abertura do chamado no ServiceDesk
* Se o cliente estiver com débitos, o sistema mostra a lista de débitos e nega a abertura de chamados.
* Mostrar a soma de debitos também

# Documentação das APIs de integração

Dados para testes 
* 99.999.999/0001-99 - CNPJ sem débitos
* 99.999.999/0002-99 - CNPJ com débitos
* token tokendeexemplo

### CRM

**Endpoint de consulta** https://edison-research.uc.r.appspot.com/sample/crm/consulta<br>
**Método** POST<br>
**Authenticação** token no header<br>
**Requisição JSON**
```json
{
	"cnpj": "99.999.999/0001-99|OBRIGATORIO"
}
```
**Retorno bem sucedido**
```json
{
    "Cidade": "Santa Fé",
    "Estado": "SP",
    "Logradouro": "Av. das americas, 2000",
    "Name": "Empresa de modelo 1",
    "cnpj": "99.999.999/0001-99",
    "debitos": [],
    "status": "OK"
}
```
**Retorno mal sucedido**
```json
{
    "Cidade": "Santa falta de pagamento",
    "Estado": "SP",
    "Logradouro": "Av. europa, 1000",
    "Name": "Empresa de modelo 2",
    "cnpj": "99.999.999/0002-99",
    "debitos": [
        {
            "ano": "2020",
            "mes": "Abril",
            "valor": 10000
        },
        {
            "ano": "2020",
            "mes": "Janeiro",
            "valor": 20000
        }
    ],
    "status": "pendente"
}
```
### SERVICE DESK

**Endpoint de consulta** https://edison-research.uc.r.appspot.com/sample/servicedesk/ticket<br>
**Método** POST<br>
**Authenticação** token no header<br>
**Requisição JSON**
```json
{
    "cnpj": "99.999.999/0001-99|OBRIGATORIO",
    "Problem": "OBRIGATORIO"
}
```
**Retorno**
```json
{
    "date": "14/05/2020",
    "id": 29008,
    "status": "Ticket criado",
    "ticketTitle": "não consigo me logar"
}
```
