public class Pregrado extends Estudiante {
    public int cantidad_creditos;

    //Constructor
    public Pregrado(String nombre, int edad, String programa, String tipo_etnia, int cantidad_creditos) {
        super(nombre, edad, programa, tipo_etnia);
        this.cantidad_creditos = cantidad_creditos;
    }

    //Metodo toString
    public String toString() {
        return super.toString() + "," + cantidad_creditos;
    }
    

    
}
