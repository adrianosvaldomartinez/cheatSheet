let nombre;

let listado = {
  nombre: nombre,
};

console.log(listado.nombre);
listado.nombre = "luis";
console.log(listado.nombre);
console.log(nombre);

class Rectangle {
  // el constructor asigna los parametros que le pasemos a una isntancia de la clase, dentro de la misma
  constructor(height, width) {
    this.height = height;
    this.width = width;
  }
  // Getter
  get area() {
    return this.calcArea();
  }
  // Method
  calcArea() {
    return this.height * this.width;
  }
}

const square = new Rectangle(10, 10);

console.log(square.area); // 100

// for of esta pensado para iterearse sobre colecciones, no devuelve nada
// supuestamente e smas moderno que for each
let listaAlumnos = ["luis", "alberto", "jose"];

for (alumno of listaAlumnos) {
  console.log(alumno);
}

// for each esta pensado para iterearse sobre colecciones, no devuelve nada

let listaAlumnitos = ["luisito", "albertito", "josesito"];

listaAlumnitos.forEach((element) => {
  console.log(element);
});

// map ejecuta una iteracion sobre los elementso de una lista y devuelve un valor
listaAnimales = ["leon", "tigre"];

listaAnimalitos = listaAnimales.map(function (elem) {
  return elem + "cito";
});

console.log(listaAnimalitos);
