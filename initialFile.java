
import java.util.ArrayList;

public class initialFile {
    


    public static void main(String[] args) {

        // este es un metodo estatico
        System.out.println(helper1.helperString1() );

        //este es un metodo no estatico, hay que inicializar
        // no es obvio que va a si estamos asignandole el valor de un new helper2, su tipo tipo va a ser una objeto de este tipo?
        helper2 helper2instance = new helper2();
        System.out.println(helper2instance.helperString2() );
        utilidades.setNombre("adam");
        System.out.println(utilidades.getNombre() );
        

        ArrayList<Integer> listaEdades = new ArrayList<Integer>();

        listaEdades.add(1000);
        listaEdades.add(2000);
        System.out.println(listaEdades );

    }
}
