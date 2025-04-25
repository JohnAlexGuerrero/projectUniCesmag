DESCRIPTION_PROMPT = '''
 
    
'''

CATEGORIZATION_PROMPT = '''
Eres un experto desarrollador de software y tienes la tarea de crear el documento tecnico de tu software,
Esta clasificación facilita su identificación, comparación y selección según las necesidades del usuario o desarrollador. 
tu tarea es redactar la seccion de categorizacion de software; para redactar esta seccion, se debe tener encuenta
la siguiente información:
        
    Nombre del software: {0}
    Tipo de licencia: (propietaria, libre, freeware, etc.) {1}
    Clasificación o tipo de software: (de sistema, de aplicación, de programación, etc.) {2}
    sector en donde el software, tiene su aplicación: {3}
    Categoria general: {4}, la cual sirve, para clasificar el software, dentro de un conjunto de softwares. 
    Público objetivo: {5}
    
    resultado:
    La categorizacion del software debe ser un texto claro, conciso y persuasivo que incluya:

    Un titular llamativo que capte la atención del lector.
    Una breve explicación del tipo de licencia que otorga el software.
    Una descripción del tipo de software, al que pertenece y los beneficios que aportan al usuario.
    Una descripcion del sector, en donde el software tiene su aplicación. 
    categoria general que permita identificar la clasificacion del software
    
'''