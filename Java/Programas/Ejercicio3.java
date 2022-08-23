package ejercicio3.src.ejercicio3;

import java.util.Scanner;
public class Ejercicio3 {
    private Scanner teclado;
    private String[] nombres;
    private int[] cc;
    private double[] R1;
    private double[] R2;
    private double[] R3;
    private double[] R4;
    private double[] R5;
    private double[] eng;
    private double[] skill;
    
    public void cargar() {
        teclado=new Scanner(System.in);
        
        System.out.print("Cantidad de estudiantes:");
        int cant;
        cant = teclado.nextInt();
        nombres=new String[cant];
        cc = new int[cant];
        R1 = new double[cant];
        R2 = new double[cant];
        R3 = new double[cant];
        R4 = new double[cant];
        R5 = new double[cant];
        eng = new double[cant];
        skill = new double[cant];
        
        for(int f=0;f<nombres.length;f++) {
            System.out.print("Ingrese nombre:");
            nombres[f] = teclado.next();
            System.out.print("Ingrese cc:");
            cc[f] = teclado.nextInt();
            System.out.print("Ingrese nota R1:");
            R1[f] = teclado.nextDouble();
            System.out.print("Ingrese nota R2:");
            R2[f] = teclado.nextDouble();
            System.out.print("Ingrese nota R3:");
            R3[f] = teclado.nextDouble();
            System.out.print("Ingrese nota R4:");
            R4[f] = teclado.nextDouble();
            System.out.print("Ingrese nota R5:");
            R5[f] = teclado.nextDouble();
            System.out.print("Ingrese nota ingles:");
            eng[f] = teclado.nextDouble();
            System.out.print("Ingrese nota habilidades:");
            skill[f] = teclado.nextDouble();
            System.out.println();
        }
    }    
    
    public void definitiva() {
        double acumulado = 0,promedioGlobal;
        
    	for(int f=0;f<nombres.length;f++) {
         
            double notaFinal = (((R1[f])*0.1)+((R2[f])*0.1)+((R3[f])*0.2)+
                    (R4[f]*0.2)+(R5[f]*0.2)+(eng[f]*0.1)+(skill[f]*0.1));
            System.out.print("Nota final del estudiante" + f +":"+ notaFinal);
            System.out.println();
            
            acumulado += notaFinal;   
    	}
        promedioGlobal = acumulado / nombres.length;
        
        if (nombres.length == 1){
            System.out.println();
        } 
        else{
            System.out.println();
            System.out.println("El promedio de los estudiantes:"+ promedioGlobal);  
        }
       /* double Estadistica1 = promedioGlobal;
        System.out.print("Estadistica 1:" + Estadistica1 + " ");
        
        double Estadistica2 = ((R1/4) + ((R2/4)+10));
        System.out.print("Estadistica 2:" + Estadistica2 + " ");
        
        double Estadistica3 = (((((R4)+(R5))*.30))-(Estadistica1/5));
        System.out.println("Estadistica 3:" + Estadistica3);*/
    }
    
      
    public static void main(String[] args) {
        Ejercicio3 pv=new Ejercicio3();
        pv.cargar();
        pv.definitiva();
        
    }
    
}
