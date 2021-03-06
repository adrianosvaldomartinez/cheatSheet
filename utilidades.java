// las clases las propiedades y los metodos pueden ser estaticos
// en este archivo se ejemplifica propiedades y metodos estaticos

// si no quiero instanciar nuevas clases para usar los metodos, estos metodos tiene que ser estaticos
//  Static methods are often used to create utility functions for an application,
//  whereas static properties are useful for caches, fixed-configuration, 
// or any other data you don't need to be replicated across instances.

// obvaimente en estos metodos no puedo usar this, poruqe no se crea una nueva clase

// una variable no definida retorna null
class utilidades {

    // metodos y propiedades estaticos que se pueden llamar sin instanciar clase
    // static properties and methods
    static String nombre;
    static String getNombre() {
        return nombre;
    }
    static void setNombre (String _nombre){
        nombre = _nombre;
    }

    // metodos y propiedades de la clase, tenemos que instanciar para llamar
    // instancie property and metods
    String apellido;
    String getApellido(){
        return this.apellido;
    }
    void setApellido(String _apellido){
        this.apellido = _apellido;
    }

    
    public static void main (String[] args) {

        System.out.println("Hello, World.");
       System.out.println(utilidades.getNombre());
       utilidades.setNombre("David de metodos y propiedades estaticas");
       System.out.println(utilidades.getNombre());
    //    Porque funciona sin si siquiera llamar a la clase estatica?
       System.out.println(getNombre());
        // Instancio la clase
        utilidades utilitiesI = new utilidades();
        utilitiesI.setApellido("Martinez de metodos y propiedades de instancia");
        System.out.println(utilitiesI.getApellido());
 
    }
}