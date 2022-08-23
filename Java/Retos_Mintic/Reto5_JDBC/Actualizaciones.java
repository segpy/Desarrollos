/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.principal;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

/**
 *
 * @author Usuario
 */
public class Actualizaciones {

    public static void menuActualizaciones(Connection x) throws SQLException {
        Scanner sc = new Scanner(System.in);
        System.out.println("** Que actualizacion desea ver **"
                + "\n 1 Actualizacion: año bicicletas"
                + "\n 2 Actualizacion: celular clientes"
                + "\n 3 Eliminar: busqueda intenciones"
                + "\n * Volver");
        System.out.print(">>");
        String op = sc.nextLine();
        if(op.equals("*")){
            Principal.salir1=false;
        }else{
            Byte opcion = Byte.parseByte(op);
            switch (opcion){
                case 1:
                    System.out.println("Actualizacion 1");
                    System.out.println("____________");
                    actualizacion1(x);
                    break;
                case 2:
                    System.out.println("Actualizacion 2");
                    System.out.println("____________");
                    update2(x);
                    break;
                case 3:
                    System.out.println("Actualizacion 3");
                    System.out.println("____________");
                    delete1(x);
                    break;
            }
        }
    }

    public static void actualizacion1(Connection x) throws SQLException{
        String sql = "UPDATE bicicletas SET año_const = ? where nombreF_Bici = ?";
        PreparedStatement st = x.prepareStatement(sql);
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el año de fabricación: ");
        int year = sc.nextInt();
        System.out.print("Ingrese el nombre de fabricante: ");
        String nFab = sc.next();
        st.setInt(1, year);
        st.setString(2, nFab);
        st.executeUpdate();

    }

    public static void update2(Connection x) throws SQLException{
        String sql = "UPDATE clientes SET celular = ? where username = ?";
        PreparedStatement st = x.prepareStatement(sql);
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el número de teléfono nuevo: ");
        long tel = sc.nextLong();
        System.out.print("Ingrese el usuario: ");
        String user = sc.next();
        st.setLong(1, tel);
        st.setString(2, user);
        st.executeUpdate();
    }

    public static void delete1(Connection x) throws SQLException{
        String sql = "DELETE FROM intenciones where user = ? and busqueda = ?";
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese usuario: ");
        String user = sc.nextLine();
        System.out.print("Ingrese al marca: ");
        String bus = sc.nextLine();
        PreparedStatement st = x.prepareStatement(sql);
        st.setString(1, user);
        st.setString(2, bus);
        int ex = st.executeUpdate();
        if(ex > 0){
            System.out.println("** Borrado **");
        }
    }

}

