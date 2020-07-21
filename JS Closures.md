# JS Clousures
Presenter: Salvador Elizararrás

Lenguaje funcional. 

ECMAScript o ES6 -> estandar de JS. Specification standardized by ECMA International.

## Scope
Global and local binding. 

## Shadow Variables
How a variable can be reference from different scopes.

## `var` vs `let` vs `consts`

`var` scope per function.

`let` scope per block.

`const` a let that cannot be change.

## `this` keyword and arrow functions
> `this` not like in Object Oriented Programming

Función anónima, cuando la función no tiene nombre.

Arrow funtion 
- función anónima
- intercatúa en el contexto _enclosing scope_ (el this del padre)
- another tool
- elegancia del código (código legible)
- cosas funcionales (what is this)
- es importante tener una buena justificación para utilizar un arrow functions
- A una arrow function le da el this o el contexto la función que tenga sobre ella, sin embargo si no tiene una función tiene un objeto entonces el this es un objeto vació porque no hay función que proveea algo.
- esta función padre no tiene que tener un nombre específico, más sí tiene que tener el nombre de `function`.

## Closure

Funciones que pueden manejar las funciones como valores y pueden referenciar local bindings de afuera.

``` 
function discount(percentage){
    return (total) => total - (total * percentage) / 100.0;
}

let studentTotal = discount(10);
let saleTotal = discount(50);

console.info(studentTotal(100)); // 90
console.info(saleTotal(100)); //50
```

> __Función pura__ que no tiene side effects sobre sus paramétros

