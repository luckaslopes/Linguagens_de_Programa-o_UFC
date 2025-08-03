function porValor(x) {
    x += 10;
}

function porReferencia(obj) {
    obj.valor += 10;
}

let a = 5;
let b = { valor: 5 };

porValor(a);
porReferencia(b);

console.log("Valor após porValor:", a);       // 5
console.log("Valor após porReferencia:", b.valor);  // 15
