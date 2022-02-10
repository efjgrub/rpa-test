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

# Fluxograma do projeto

![image alt >](Fluxo-Exemplo.png)

# Documentação das APIs de integração

Dados para testes 
* **99.999.999/0001-99** - CNPJ sem débitos
* **99.999.999/0002-99** - CNPJ com débitos
* token **tokendeexemplo**

### CRM

**Endpoint de consulta** https://learn-rpa-dot-edison-research.uc.r.appspot.com/sample/crm/consulta<br>
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
    "cnpj": "99.999.999/0001-99",
    "Name": "Company sample 1",
    "Address": " 767 5th Ave",
    "City": "New York",
    "Estate": "NY",
    "d": [],
    "status": "OK"
}
```
**Retorno mal sucedido**
```json
{
    "cnpj": "99.999.999/0002-99",
    "Name": "Company sample 2",
    "Address": " 242 W 41st St",
    "City": "New York",
    "Estate": "NY",
    "d": [
        {
            "year": "2020",
            "mouth": "April",
            "value": 10000
        },
        {
            "year": "2020",
            "mouth": "Janaury",
            "value": 20000
        }
    ],
    "status": "debt"
}
```
### SERVICE DESK

**Endpoint de consulta** https://learn-rpa-dot-edison-research.uc.r.appspot.com/sample/servicedesk/ticket<br>
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
# Exemplo do fluxo construído

![image alt >](Sugestao-De-Fluxo.png)

# Scripts de exemplo
```javascript
// Iterar com Array 1
() => {
    let saldo = 0;
    data = JSON.parse(VAR_ENTRADA);
      data.pendencias.forEach(el => {
         saldo = saldo + el.valor;
      });
  
    return saldo;
  };

// Iterar com Array 2
() => {
  var v = JSON.parse(pendencias);
  var val = 0;
  for (var i = 0; i < v.length; i++){
    var obj = v[i];
    val = val + obj['valor'];
  }
  return val;
};

// tamanho de Array
obj = JSON.parse(json);
Object.size(obj.clients[0].pop_problem_list)

// Pontuando valores
var numero = 10000;

return (numero.toLocaleString()); 
```
