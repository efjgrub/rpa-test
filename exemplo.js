
// Iterar com Array 1
() => {
    let saldo = 0;
    data = JSON.parse(VAR_ENTRADA);
      data.d.forEach(el => {
         saldo = saldo + el.valor;
      });
  
    return saldo;
  };

// Iterar com Array 2
() => {
  var v = JSON.parse(debitos);
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
