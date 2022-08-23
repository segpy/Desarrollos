/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
//package Cuadrado_validado;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Cuadrado_validado {
    public static void main(String[] ar) {
        try (Scanner teclado = new Scanner(System.in)) {
            int num;
            boolean continua;
            do {
                try {
                    continua = false;
                    System.out.print("Ingrese un valor entero:");
                    num = teclado.nextInt();
                    int cuadrado = num * num;
                    System.out.print("El cuadrado de " + num + " es " + cuadrado);
                } catch (InputMismatchException ex) {
                    System.out.println("Debe ingresar obligatoriamente un número entero.");
                    teclado.next();
                    continua = true;
                }
            } while (continua);
        }
    }
}