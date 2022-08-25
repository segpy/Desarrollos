//importar la clase scanner
import java.util.Scanner;
public class Reto1_Condicionales
 {
    public String esfera_f(int t){
        String esfera =  "";
        if (t <= 20){
            esfera = "uno";
        }else if (t <= 30){
            esfera = "dos";
        }else if (t <= 50){
            esfera = "tres";
        }else {
            esfera = "cuatro";
        }
        return esfera;
    }
    public static void main(String[] args) throws Exception {
        
        int d_goku = 0;
        int d_esfera = 0;
        int t = 0;
        try (//Recibir como entrada d_goku
        Scanner teclado = new Scanner(System.in)) {
            System.out.print("Ingrese el valor de d_goku: ");
            d_goku = teclado.nextInt();
        }
        d_esfera = 2*d_goku+4;
        t = (d_goku+d_esfera)/5;
        //Imprimir los 3 valores en una sola linea
        System.out.println(d_goku +" "+ d_esfera +" "+ t);
        //Crear objeto de la clase Reto1
        Reto1_Condicionales app = new Reto1_Condicionales();
        //Imprimir el valor de la esfera
        System.out.println("La esfera es: " + app.esfera_f(t));
        

    }
    
}
