/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.principal;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.Scanner;

/**
 *
 * @author Usuario
 */
public class Principal {

    static boolean salir1 = true;

    public static void main(String[] args) throws SQLException {

        Connection conn = conectar();
        Scanner sc = new Scanner(System.in);
        boolean seguir = true;
        while(seguir) {
            System.out.println("************     CRUD    ************"
                    + "\n ** Que operación desea hacer **"
                    + "\n 1 Create - Insertar datos"
                    + "\n 2 Retrieve - Leer datos"
                    + "\n 3 Update - Actualizar datos"
                    + "\n 4 Delete - Eliminar datos \n"
                    + "\n *****    RETO 4   *****"
                    + "\n 5 Actualizaciones - Consultas"
                    + "\n * Salir");
            System.out.print(">>");
            String op = sc.nextLine();
            if (op.equals("*")) {
                seguir = false;
                //System.exit(0);
            } else {
                byte opcion = Byte.parseByte(op);
                switch (opcion) {
                    case 1:
                        salir1 = true;
                        while (salir1) {
                            try {
                                Crud.agregarAll(conn);
                                System.out.println("Desea insertar más datos?: y/n");
                                if (sc.next().equals("n")) {
                                    salir1 = false;
                                    sc.nextLine();
                                }else{
                                    sc.nextLine();
                                }
                            } catch (Exception e) {
                            }
                        }
                        break;
                    case 2:
                        salir1 = true;
                        while (salir1) {
                            try {
                                Crud.leerAll(conn);
                                System.out.println("Desea leer más datos?: y/n");
                                if (sc.next().equals("n")) {
                                    salir1 = false;
                                    sc.nextLine();
                                }else{
                                    sc.nextLine();
                                }
                            } catch (Exception e) {
                            }
                        }
                        break;
                    case 3:
                        salir1 = true;
                        while (salir1) {
                            try {
                                Crud.actualizarAll(conn);
                                System.out.println("Desea actualizar más datos?: y/n");
                                if (sc.next().equals("n")) {
                                    salir1 = false;
                                    sc.nextLine();
                                }else{
                                    sc.nextLine();
                                }
                            } catch (Exception e) {
                            }
                        }
                        break;
                    case 4:
                        salir1 = true;
                        while (salir1) {
                            try {
                                Crud.eliminarAll(conn);
                                System.out.println("Desea eliminar más datos?: y/n");
                                if (sc.next().equals("n")) {
                                    salir1 = false;
                                    sc.nextLine();
                                }else{
                                    sc.nextLine();
                                }
                            } catch (Exception e) {
                            }
                        }
                        break;
                    case 5:
                        salir1 = true;
                        while (salir1) {
                            System.out.println("** Que operación desea hacer **"
                                    + "\n 1 Actualizaciones"
                                    + "\n 2 Consultas"
                                    + "\n * Volver");
                            System.out.print(">>");
                            op = sc.nextLine();
                            if (op.equals("*")){
                                salir1=false;
                            }else {
                                opcion = Byte.parseByte(op);
                                switch (opcion){
                                    case 1:
                                        Actualizaciones.menuActualizaciones(conn);
                                        break;
                                    case 2:
                                        Consultas.menuConsultas(conn);
                                        break;
                                }
                            }
                        }
                        break;
                    default:
                        System.out.println("** Opción inválida **");
                }

            }
        }


    }

    public static Connection conectar(){
        String dbURL = "jdbc:mysql://localhost:3306/reto4";
        String user = "root";
        String password = "123456789";
        Connection con = null;
        try {
            con = DriverManager.getConnection(dbURL, user, password);
            if(con != null){
                System.out.println("* Conectado *");
                System.out.println("-----------------");
            }
        } catch (SQLException e) {
            System.out.println("Error: " + e.getErrorCode() + " " + e.getMessage());
        }
        return con;
    }


}

