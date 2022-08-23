package Herencia_Polimorfismo;



class Animal {
    private String nombre;
    private String sonido;
    private String tipo;
    public Animal(String nombre, String sonido, String tipo) {
        this.nombre = nombre;
        this.sonido = sonido;
        this.tipo = tipo;
    }
    public void hablar() {
        System.out.println("hola soy un " + this.tipo + " mi nombre es " + this.nombre + " y mi sonido es " + this.sonido);
    }
}
class Perro extends Animal {
    public Perro(String nombre, String sonido) {
        super(nombre, sonido, "perro");
    }
}
class Gato extends Animal {
    public Gato(String nombre, String sonido) {
        super(nombre, sonido, "gato");
    }
}
class Pajaro extends Animal {
    public Pajaro(String nombre, String sonido) {
        super(nombre, sonido, "pajaro");
    }
}

class Main{
    public static void main(String[] args) {
        // Polimorfismo: es el hecho de que una clase puede tener varios metodos con el mismo nombre y distintos tipos de parametros
        // Polimorfismo en objetos: crear un objeto de la clase padre y asignarle un objeto de la clase hija
        Animal perro = new Perro("Firulais", "guau");
        Animal gato = new Gato("Mimi", "miau");
        Animal pajaro = new Pajaro("Pio", "pio");
        perro.hablar();
        gato.hablar();
        pajaro.hablar();

    }
}
