import java.util.*;

public class Obra {
    int dato;
    //Constructor
    public Obra(int dato) {
        this.dato = dato;
    }
    //Metodo numero 1
    public ArrayList<Integer> clases(ArrayList<Integer> clase){
        ArrayList<Integer> lista = new ArrayList<>();
        //Metodo for 1
        System.out.println("Metodo for 1");
        for(Integer i : clase){
            System.out.println(i);
            if(!lista.contains(i)){
                lista.add(i);
            }
        }
        System.out.println("Lista metodo 1: " + lista);
        lista.clear();
        //Metodo for 2
        System.out.println("Metodo for 2");
        for(int i = 0; i<clase.size(); i++){
            System.out.println(i);
            if(lista.contains(clase.get(i))){
                
            }else{
                lista.add(clase.get(i));
            }
        }
        System.out.println("Lista metodo 2: ");
        return lista;
    }
    //Metodo numero 2
    public ArrayList<Integer> meFaltanDeLaClase (ArrayList<Integer> clase, ArrayList<Integer> clase2, Integer clase3){
        ArrayList<Integer> lista = new ArrayList<>();
        for(int i=0; i<clase.size(); i++){
            if(clase2.get(clase.get(i))==clase3){
                lista.add(clase.get(i));
            }
        }
        return lista;
    }
    //Metodo numero 3
    public ArrayList<Integer> noTengo (ArrayList<Integer> clase, ArrayList<Integer> clase2){
        ArrayList<Integer> lista = new ArrayList<>();
        for(int i=0; i<clase.size(); i++){
            if(!clase2.contains(clase.get(i))){
                lista.add(clase.get(i));
            }
        }
        return lista;
    }
    //Metodo numero 4
    public int puedoCambiar (ArrayList<Integer> clase, ArrayList<Integer> clase2){
        int lista = 0;
        for(int i=0; i<clase2.size(); i++){
            if(!clase.contains(clase2.get(i))){
                lista++;
            }
        }
        return lista;
    }
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        //Prueba metodo 1
        System.out.println("Prueba metodo 1");
        ArrayList<Integer> clase = new ArrayList<Integer>(Arrays.asList(1,2,5,5,5,1,2,5,5,5));
        Obra obra = new Obra(1);
        System.out.println(obra.clases(clase));
        //Prueba metodo 2
        System.out.println("Prueba metodo 2");
        clase = new ArrayList<Integer>(Arrays.asList(1,3,6,8));
        ArrayList<Integer> clase2 = new ArrayList<Integer>(Arrays.asList(1,2,5,5,5,1,2,5,5,5));
        Integer clase3 = 5;
        System.out.println(obra.meFaltanDeLaClase(clase, clase2, clase3));
        //Prueba metodo 3
        System.out.println("Prueba metodo 3");
        clase = new ArrayList<Integer>(Arrays.asList(3,5,7,10,15,16));
        clase2 = new ArrayList<Integer>(Arrays.asList(4,10,5,8));
        System.out.println(obra.noTengo(clase, clase2));
        //Prueba metodo 4
        System.out.println("Prueba metodo 4");
        clase = new ArrayList<Integer>(Arrays.asList(49, 40, 26, 9, 14, 25, 18, 11, 39, 23, 19, 41, 38, 44, 42, 27, 28));
        clase2 = new ArrayList<Integer>(Arrays.asList(5, 13, 35, 48, 43, 0, 7, 30, 27, 2, 1, 40, 14, 28, 8, 10, 36, 49, 39, 23));
        System.out.println(obra.puedoCambiar(clase, clase2));
    }
}
