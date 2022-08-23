public class Interfaces {
    public static void main(String[] args) {
        Clase c = new Clase();
        c.metodo();
    }
    
}

interface Interfaz{
    public void metodo();
}

class Clase implements Interfaz{
    public void metodo(){
        System.out.println("metodo de la clase");
    }
}
