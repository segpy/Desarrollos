public class Estudiante {
    public String nombre;
    public int edad;
    public String programa;
    public String tipo_etnia;

    //Constructor
    public Estudiante(String nombre, int edad, String programa, String tipo_etnia) {
        this.nombre = nombre;
        this.edad = edad;
        this.programa = programa;
        this.tipo_etnia = tipo_etnia;
    }

    //Metodo toString
    @Override
    public String toString() {
        return nombre + "," + edad + "," + programa + "," + tipo_etnia;
    }
}
