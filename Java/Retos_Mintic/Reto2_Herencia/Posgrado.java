public class Posgrado extends Estudiante {
    public String modalidad;

    //Constructor
    public Posgrado(String nombre, int edad, String programa, String tipo_etnia, String modalidad) {
        super(nombre, edad, programa, tipo_etnia);
        this.modalidad = modalidad;
    }

    //Metodo toString
    public String toString() {
        return super.toString() + "," + modalidad;
    }

    
}
