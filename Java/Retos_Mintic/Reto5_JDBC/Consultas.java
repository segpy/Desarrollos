/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.principal;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.Scanner;

/**
 *
 * @author Usuario
 */
public class Consultas {

    public static void menuConsultas(Connection x) throws SQLException {
        Scanner sc = new Scanner(System.in);
        System.out.println("** Que consulta desea ver **"
                + "\n 1 Consulta: Fabricantes bicicletas y motocicletas"
                + "\n 2 Consulta: Bicicletas con año de fabricacion mayor que 2019"
                + "\n 3 Consulta: Fabricantes de moto con proveedor Auteco"
                + "\n 4 Consulta: Busqueda de intenciones con el usuario lucky"
                + "\n 5 Consulta: Datos del usuario de la tabla clientes que tiene la intencion de busqueda 'Yeti'"
                + "\n 6 Consulta: Cantidad de bicicletas con año de construccion mayor que 2019"
                + "\n * Volver");
        System.out.print(">>");
        String op = sc.nextLine();
        if(op.equals("*")){
            Principal.salir1=false;
        }else{
            byte option = Byte.parseByte(op);
            switch (option){
                case 1:
                    consulta1(x);
                    break;
                case 2:
                    consulta2(x);
                    break;
                case 3:
                    consulta3(x);
                    break;
                case 4:
                    consulta4(x);
                    break;
                case 5:
                    consulta5(x);
                    break;
                case 6:
                    consulta6(x);
                    break;
            }
        }
    }

    public static void consulta1(Connection x) throws SQLException{
        System.out.println("Consulta 1");
        System.out.println("____________");
        String sql = "select bicicletas.nombreF_Bici as fabricantes from bicicletas union select motocicletas.nombreF_Moto from motocicletas order by fabricantes";
        Statement st = x.createStatement();
        ResultSet r =  st.executeQuery(sql);
        while(r.next()){
            System.out.println(r.getString(1));
        }
    }

    public static void consulta2(Connection x) throws SQLException{
        System.out.println("Consulta 2");
        System.out.println("____________");
        String sql = "select * from bicicletas where año_const >= 2019 order by nombreF_Bici";
        Statement st = x.createStatement();
        ResultSet r =  st.executeQuery(sql);
        while(r.next()){
            System.out.println(r.getString(1) + " " + r.getLong(2) + " " + r.getInt(3));
        }
    }

    public static void consulta3(Connection x) throws SQLException{
        System.out.println("Consulta 3");
        System.out.println("____________");
        String sql = "select nombreF_moto from motocicletas where proveedor_mot = 'Auteco'";
        Statement st = x.createStatement();
        ResultSet r =  st.executeQuery(sql);
        while(r.next()){
            System.out.println(r.getString(1));
        }
    }

    public static void consulta4(Connection x) throws SQLException{
        System.out.println("Consulta 4");
        System.out.println("____________");
        String sql = "select busqueda from intenciones where user = 'lucky' order by busqueda";
        Statement st = x.createStatement();
        ResultSet r =  st.executeQuery(sql);
        while(r.next()){
            System.out.println(r.getString(1));
        }
    }

    public static void consulta5(Connection x) throws SQLException{
        System.out.println("Consulta 5");
        System.out.println("____________");
        String sql = "select clientes.username, clientes.nombres, clientes.apellidos from clientes inner join intenciones on clientes.username = intenciones.user where busqueda = 'Yeti'";
        Statement st = x.createStatement();
        ResultSet r =  st.executeQuery(sql);
        while(r.next()){
            System.out.println(r.getString(1) + " " + r.getString(2) + " " + r.getString(3));
        }
    }

    public static void consulta6(Connection x) throws SQLException{
        System.out.println("Consulta 6");
        System.out.println("____________");
        String sql = "select count(año_const) from bicicletas where año_const>=2019;";
        Statement st = x.createStatement();
        ResultSet r =  st.executeQuery(sql);
        while(r.next()){
            System.out.println(r.getInt(1));
        }
    }
}

