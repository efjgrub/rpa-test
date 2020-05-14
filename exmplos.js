
// Iterar com Array 
() => {
    let saldo = 0;
    data = JSON.parse(VAR_ENTRADA);
      data.debitos.forEach(el => {
         saldo = saldo + el.valor;
      });
  
    return saldo;
  };