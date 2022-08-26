public class prueba {
    public static void main(String[] args) {
        System.out.println(metodoRaro());
    }
    public static String metodoRaro() {
        String[] letras = {"C", "O", "L", "O", "M", "B", "I", "A"};
        int n = letras.length;
        int izq = 0, der = 0, aux = 0;
        String salida = "";
        for (int i = 0; i < n; i++) {
            if (aux > n){
                break;
            }
            der = aux + 1;
            while (der >= izq){
                if (der == izq){
                    salida += letras[aux];
                    aux += izq;
                }
                der--;
            }
            izq++;
        }
        return salida;
    }
}
