//importar la clase scanner
import java.util.Scanner;
public class Notas {
    public static int[] crea_arreglo_nEnteros(Scanner sc, int n){
        int[] x = new int[n];
        for( int i=0; i<n; i++ ){
            System.out.println("Componente "+i+"- esima?");
            x[i] = sc.nextInt();
        }
        return x;
    }
    public static void lee_posicion_arreglo(int[] x){
        int n = x.length;
        for( int i=0; i<n; i++ ){
        System.out.println("x["+i+"]="+x[i]);
        }
    }
        
    public static void main(String[] args) throws Exception {
        //Arreglo de enteros
        double[] x = new double[]{1.0, 2.0, 3.0, 4.0, 5.0};
        int[] y = new int[5];
        y=crea_arreglo_nEnteros(new Scanner(System.in), 5);
        lee_posicion_arreglo(y);
        System.out.println(x.length);

    }
}

