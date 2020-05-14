
// Iterar com Array 
() => {
    let saldo = 0;
    data = JSON.parse(VAR_ENTRADA);
      data.debitos.forEach(el => {
         saldo = saldo + el.valor;
      });
  
    return saldo;
  };


// tamanho de Array
obj = JSON.parse(json);
Object.size(obj.clients[0].pop_problem_list)
