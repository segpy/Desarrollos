import java.util.Scanner;

class Registro {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        boolean salir = false;
        arregloEstudiante = new Estudiante[10];
        
        do {
                Registro registro = new Registro();
                String texto = sc.nextLine();
                String[] division = texto.split("&");
                salir=registro.procesarComandos(division, salir);
                
        } while (salir==false);
        //cerrar el scanner
        sc.close();
    }
        
        private static Estudiante arregloEstudiante[];
        private static int cantidadEstudiantes=0;

    public boolean procesarComandos(String[] division, boolean salir){
        if (Integer.parseInt(division[0]) == 1) {
            agregarEstudiante(division);
            //System.out.println("agregarEstudiante");
        }else if (Integer.parseInt(division[0]) == 2) {
            listarEstudiantes();
            //System.out.println("listarEstudiantes");
        }else if (Integer.parseInt(division[0]) == 3) {
            //System.out.println("salir");
            salir=true;
        }
        return salir;
    }
    
    public void agregarEstudiante(String[] division){
        //Agrega los atributos del estudiante
        String estudiante =  division[1];
        String nombre = division[2];
        int edad = Integer.parseInt(division[3]);
        String programa = division[4];
        String etnia = division[5];
        if (estudiante.equals("Pregrado")) {
            int creditos = Integer.parseInt(division[6]);
            //Concepto de Polimorfismo: se crea un objeto de la clase Pregrado en el arreglo de tipo Estudiante, donde Estudiante es una clase padre de Pregrado.
            arregloEstudiante[cantidadEstudiantes] = new Pregrado(nombre, edad, programa, etnia, creditos);  
            cantidadEstudiantes++;
        } else if (estudiante.equals("Posgrado")) {
            String modalidad = division[6];
            arregloEstudiante[cantidadEstudiantes] = new Posgrado(nombre, edad, programa, etnia, modalidad);
            cantidadEstudiantes++;
        }
    }

    public void listarEstudiantes(){
        System.out.println("***Listado de estudiantes***");
        for (int i = 0; i < cantidadEstudiantes; i++) {
            if (arregloEstudiante[i] instanceof Pregrado) { //instanceof verifica si el objeto es una instancia de una clase
                System.out.println("\tEstudiante Pregrado");
                System.out.println("\tNombre: " + arregloEstudiante[i].nombre);
                System.out.println("\tEdad: " + arregloEstudiante[i].edad + " anios");
                System.out.println("\tPrograma: " + arregloEstudiante[i].programa);
                System.out.println("\tEtnia: " + arregloEstudiante[i].tipo_etnia);
                System.out.println("\tCreditos: " + ((Pregrado)arregloEstudiante[i]).cantidad_creditos);
            } else if (arregloEstudiante[i] instanceof Posgrado) {
                System.out.println("\tEstudiante Posgrado");
                System.out.println("\tNombre: " + arregloEstudiante[i].nombre);
                System.out.println("\tEdad: " + arregloEstudiante[i].edad + " anios");
                System.out.println("\tPrograma: " + arregloEstudiante[i].programa);
                System.out.println("\tEtnia: " + arregloEstudiante[i].tipo_etnia);
                System.out.println("\tModalidad: " + ((Posgrado)arregloEstudiante[i]).modalidad);
            }
        }
        
    }
    
}