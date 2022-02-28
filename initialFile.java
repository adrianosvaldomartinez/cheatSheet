
public class initialFile {
    


    public static void main(String[] args) {

        // este es un metodo estatico
        System.out.println(helper1.helperString1() );

        //este es un metodo no estatico, hay que inicializar
        // no es obvio que va a si estamos asignandole el valor de un new helper2, su tipo tipo va a ser una objeto de este tipo?
        helper2 helper2instance = new helper2();
        System.out.println(helper2instance.helperString2() );

    }
}
