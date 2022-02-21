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
