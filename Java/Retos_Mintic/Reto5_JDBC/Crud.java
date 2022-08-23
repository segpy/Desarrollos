/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.principal;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

/**
 *
 * @author Usuario
 */
public class Crud {
    public static void leerAll(Connection x) throws SQLException{
        Scanner sc = new Scanner(System.in);
        System.out.println("** De qué tabla quieres saber sus datos **"
                + "\n 1 Clientes"
                + "\n 2 Bicicletas"
                + "\n 3 Motocicletas"
                + "\n 4 Proveedores"
                + "\n 5 Intenciones"
                + "\n * Volver");
        System.out.print(">>");
        String op = sc.nextLine();
        if(op.equals("*")){
            Principal.salir1 = false;
        }
        byte opcion = Byte.parseByte(op);
        String sql = "SELECT * FROM ";
        Statement st = x.createStatement();

        switch (opcion) {
            case 1:
                String sqlC = sql + "clientes";
                ResultSet r = st.executeQuery(sqlC);
                while(r.next()){
                    System.out.println(r.getString(1) + " " + r.getString(2) + " " + r.getString(3) + " " + r.getString(4) + " " + r.getLong(5)
                            + " " + r.getInt(6) + " " + r.getDate(7));
                }
                break;
            case 2:
                String sqlB = sql + "bicicletas";
                ResultSet rB = st.executeQuery(sqlB);
                while(rB.next()){
                    System.out.println(rB.getString(1) + " " + rB.getLong(2) + " " + rB.getInt(3));
                }
                break;
            case 3:
                String sqlM = sql + "motocicletas";
                ResultSet rM = st.executeQuery(sqlM);
                while(rM.next()){
                    System.out.println(rM.getString(1) + " " + rM.getInt(2) + " " + rM.getString(3) + " " + rM.getString(4));
                }
                break;
            case 4:
                String sqlP = sql + "proveedor";
                ResultSet rP = st.executeQuery(sqlP);
                while(rP.next()){
                    System.out.println(rP.getString(1) + " " + rP.getString(2) + " " + rP.getLong(3));
                }
                break;
            case 5:
                String sqlI = sql + "intenciones";
                ResultSet rI = st.executeQuery(sqlI);
                while(rI.next()){
                    System.out.println(rI.getInt(1) + " " + rI.getString(2) + " " + rI.getString(3) + " " + rI.getDate(4)
                            + "" + rI.getTime(5));

                }
                break;
            default:
                throw new AssertionError();
        }

    }

    public static void agregarAll(Connection x) throws SQLException{
        Scanner sc = new Scanner(System.in);
        System.out.println("** A qué tabla quieres agregar datos **"
                + "\n 1 Clientes"
                + "\n 2 Bicicletas"
                + "\n 3 Motocicletas"
                + "\n 4 Proveedores"
                + "\n 5 Intenciones"
                + "\n * Volver");
        System.out.print(">>");
        String op = sc.nextLine();
        if(op.equals("*")){
            Principal.salir1 = false;
        }
        byte opcion = Byte.parseByte(op);
        String sql = "INSERT INTO ";
        switch (opcion) {
            case 1:
                String sqlC = sql + "clientes VALUES (?, ?, ?, ?, ?, ?, ?)";
                PreparedStatement st = x.prepareStatement(sqlC);
                System.out.print("Ingrese el usuario: ");
                String user = sc.next();
                System.out.print("Ingrese el nombre: ");
                String nom = sc.next();
                System.out.print("Ingrese el apellido: ");
                String apl = sc.next();
                System.out.print("Ingrese el email: ");
                String email = sc.next();
                System.out.print("Ingrese el cel: ");
                long cel = sc.nextLong();
                System.out.print("Ingrese la contraseña(entero): ");
                int passw = sc.nextInt();
                System.out.print("Ingrede al fecha(yyyy-mm-dd): ");
                String fecha = sc.next();
                st.setString(1, user);
                st.setString(2, nom);
                st.setString(3, apl);
                st.setString(4, email);
                st.setLong(5, cel);
                st.setInt(6, passw);
                st.setString(7, fecha);
                int ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            case 2:
                String sqlB = sql + "bicicletas VALUES (?, ?, ?)";
                st = x.prepareStatement(sqlB);
                System.out.print("Inserte el nombre de fabricante: ");
                String nomFab = sc.next();
                System.out.print("Inserte el precio: ");
                long priceU = sc.nextLong();
                System.out.print("Inserte el año de fabricación: ");
                int year = sc.nextInt();
                st.setString(1, nomFab);
                st.setLong(2, priceU);
                st.setInt(3, year);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");

                }
                break;
            case 3:
                String sqlM = sql + "motocicletas VALUES (?, ?, ?, ?)";
                st = x.prepareStatement(sqlM);
                System.out.print("Inserte el nombre de fabricante: ");
                nomFab = sc.next();
                System.out.print("Inserte el precio: ");
                int priceM = sc.nextInt();
                sc.nextLine();
                System.out.print("Inserte la autonomía: ");
                String auto = sc.nextLine();
                System.out.print("Inserte el nombre de proveedor: ");
                String nomProv = sc.next();
                st.setString(1, nomFab);
                st.setInt(2, priceM);
                st.setString(3, auto);
                st.setString(4, nomProv);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            case 4:
                String sqlP = sql + "proveedor values (?, ?, ?)";
                st = x.prepareStatement(sqlP);
                System.out.print("Inserte el nombre del proveedor: ");
                nomProv = sc.nextLine();
                System.out.print("Ingrese la dirección: ");
                String direc = sc.nextLine();
                System.out.print("Ingrese el telefono: ");
                long tel = sc.nextLong();
                st.setString(1, nomProv);
                st.setString(2, direc);
                st.setLong(3, tel);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            case 5:
                String sqlI = sql + "intenciones (user, busqueda, fecha, hora) values (?, ?, ?, ?)";
                st = x.prepareStatement(sqlI);
                System.out.print("Ingrese el usuario: ");
                user = sc.next();
                System.out.print("Ingrese el producto de interés: ");
                String busqueda = sc.next();
                System.out.print("Ingrese la fecha(yyyy-mm-dd): ");
                fecha = sc.next();
                System.out.print("Ingrese la hora(00:00:00): ");
                String hora = sc.next();
                st.setString(1, user);
                st.setString(2, busqueda);
                st.setString(3, fecha);
                st.setString(4, hora);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            default:
                throw new AssertionError();
        }
    }

    public static void eliminarAll(Connection x) throws SQLException{
        Scanner sc = new Scanner(System.in);
        String sql = "DELETE FROM ";
        System.out.println("** De qué tabla quieres eliminar un registro **"
                + "\n 1 Clientes"
                + "\n 2 Bicicletas"
                + "\n 3 Motocicletas"
                + "\n 4 Proveedores"
                + "\n 5 Intenciones"
                + "\n * Volver");
        System.out.print(">>");
        String op = sc.nextLine();
        if(op.equals("*")){
            Principal.salir1 = false;
        }
        byte opcion = Byte.parseByte(op);
        PreparedStatement st = null;
        switch (opcion) {
            case 1:
                String sqlC = sql + "clientes WHERE username = ?";
                System.out.print("Ingrese el user que desea eliminar: ");
                String user = sc.nextLine();
                st = x.prepareStatement(sqlC);
                st.setString(1, user);
                int ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Eliminación exitosa **");
                }
                break;
            case 2:
                String sqlB = sql + "bicicletas WHERE nombreF_Bici = ?";
                System.out.print("Ingrese el nombre de la bicicleta que desea eliminar: ");
                String bici = sc.nextLine();
                st = x.prepareStatement(sqlB);
                st.setString(1, bici);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Eliminación exitosa **");
                }
                break;
            case 3:
                String sqlM = sql + "motocicletas WHERE nombreF_moto = ?";
                System.out.print("Ingrese el nombre de la motocicleta que desea eliminar: ");
                String moto = sc.nextLine();
                st = x.prepareStatement(sqlM);
                st.setString(1, moto);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Eliminación exitosa **");
                }
                break;
            case 4:
                String sqlP = sql + "proveedor WHERE nombre_prov = ?";
                System.out.print("Ingrese el nombre del proveedor que desea eliminar: ");
                String prov = sc.nextLine();
                st = x.prepareStatement(sqlP);
                st.setString(1, prov);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Eliminación exitosa **");
                }
                break;
            case 5:
                String sqlI = sql + "intenciones WHERE user = ? AND busqueda = ?";
                System.out.print("Ingrese el usuario de la intención a eliminar: ");
                user = sc.nextLine();
                System.out.print("Ingrese el nombre de la bici/moto que buscó el usuario: ");
                String bus = sc.nextLine();
                st = x.prepareStatement(sqlI);
                st.setString(1, user);
                st.setString(2, bus);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Eliminación exitosa **");
                }
                break;
            default:
                throw new AssertionError();
        }

    }

    public static void actualizarAll(Connection x) throws SQLException{
        Scanner sc = new Scanner(System.in);
        System.out.println("** De qué tabla desea actualizar un registro **"
                + "\n 1 Clientes"
                + "\n 2 Bicicletas"
                + "\n 3 Motocicletas"
                + "\n 4 Proveedores"
                + "\n 5 Intenciones"
                + "\n * Volver");
        System.out.print(">>");
        String op = sc.nextLine();
        if(op.equals("*")){
            Principal.salir1 = false;
        }
        byte opcion = Byte.parseByte(op);
        String sql = "UPDATE ";
        PreparedStatement st = null;
        switch (opcion) {
            case 1:
                System.out.print("Ingrese el usuario cuyo registro desea modificar: ");
                String user = sc.next();
                String sqlC = sql + "clientes SET nombres = ?, apellidos = ?, email = ?, celular = ?, password = ?, nacimiento = ? WHERE username = '" + user + "'";
                st = x.prepareStatement(sqlC);
                System.out.print("Ingrese el nuevo nombre: ");
                String nom = sc.next();
                System.out.print("Ingrese el nuevo apellido: ");
                String apl = sc.next();
                System.out.print("Ingrese el nuevo email: ");
                String email = sc.next();
                System.out.print("Ingrese el nuevo cel: ");
                long cel = sc.nextLong();
                System.out.print("Ingrese la nueva contraseña(entero): ");
                int passw = sc.nextInt();
                System.out.print("Ingrede la nueva fecha(yyyy-mm-dd): ");
                String fecha = sc.next();
                st.setString(1, nom);
                st.setString(2, apl);
                st.setString(3, email);
                st.setLong(4, cel);
                st.setInt(5, passw);
                st.setString(6, fecha);
                int ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            case 2:
                System.out.print("Inserte el nombre de fabricante a modificar: ");
                String nomFab = sc.next();
                String sqlB = sql + "bicicletas SET precio_U = ?, año_const = ? WHERE nombreF_Bici = '" + nomFab + "'";
                st = x.prepareStatement(sqlB);
                System.out.print("Inserte el nuevo precio: ");
                long priceU = sc.nextLong();
                System.out.print("Inserte el nuevo año de fabricación: ");
                int year = sc.nextInt();
                st.setLong(1, priceU);
                st.setInt(2, year);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            case 3:
                System.out.print("Inserte el nombre de fabricante a modificar: ");
                nomFab = sc.next();
                String sqlM = sql + "motocicletas SET precio_U = ?, duracion_bat = ?, proveedor_mot = ? WHERE nombreF_moto = '" + nomFab + "'";
                st = x.prepareStatement(sqlM);
                System.out.print("Inserte el nuevo precio: ");
                int priceM = sc.nextInt();
                sc.nextLine();
                System.out.print("Inserte la nueva autonomía: ");
                String auto = sc.nextLine();
                System.out.print("Inserte el nuevo nombre de proveedor: ");
                String nomProv = sc.next();
                st.setInt(1, priceM);
                st.setString(2, auto);
                st.setString(3, nomProv);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            case 4:
                System.out.print("Inserte el nombre del proveedor a modificar: ");
                nomProv = sc.nextLine();
                String sqlP = sql + "proveedor SET direccion = ?, telefono = ? WHERE nombre_prov = '" + nomProv + "'";
                st = x.prepareStatement(sqlP);
                System.out.print("Ingrese la nueva dirección: ");
                String direc = sc.nextLine();
                System.out.print("Ingrese el nuevo telefono: ");
                long tel = sc.nextLong();
                st.setString(1, direc);
                st.setLong(2, tel);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            case 5:
                System.out.print("Ingrese el id a modificar: ");
                user = sc.next();
                String sqlI = sql + "intenciones SET busqueda = ?, fecha = ?, hora = ? WHERE id_intencion = '" + user + "'";
                st = x.prepareStatement(sqlI);
                System.out.print("Ingrese el nuevo producto de interés: ");
                String busqueda = sc.next();
                System.out.print("Ingrese la nueva fecha(yyyy-mm-dd): ");
                fecha = sc.next();
                System.out.print("Ingrese la nueva hora(00:00:00): ");
                String hora = sc.next();
                st.setString(1, busqueda);
                st.setString(2, fecha);
                st.setString(3, hora);
                ex = st.executeUpdate();
                if(ex > 0){
                    System.out.println("** Registro exitoso **");
                }
                break;
            default:
                throw new AssertionError();

        }
    }

}


