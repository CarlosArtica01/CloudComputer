Enlace para visualización de estructura de programa de supermercado

https://drive.google.com/drive/folders/19cpg1nx4ZkS7b_1AP4HFNdM1mmqBgvdV?usp=drive_link


1. ¿Qué hace `st.session_state`?

Es la memoria persistente de la aplicación, en Streamlit cada vez que interactuamos con un botón o se escribe algo, el script se vuelve a ejecutar desde arriba hasta abajo. Sin `st.session_state`, todas las variables se resetearían a su valor inicial.

2. ¿Qué hace `calcular_subtotal()`?

Es la lógica de negocio de mi aplicación. Esta función realiza tres tareas en un solo paso:

1. Procesamiento: Toma los valores de `precio` y `cantidad` para realizar la operación aritmética ().
2. Estructuración: Empaqueta los datos del producto actual en un formato de diccionario (clave-valor).
3. Actualización: Inyecta ese nuevo registro dentro del DataFrame que tenemos guardado en la sesión para que la tabla crezca.

3. ¿Por qué se usa `st.form()`?

Se usa para optimizar el rendimiento y la experiencia de usuario, por defecto, Streamlit es reactivo cuando cambiaamos una letra en un campo de texto, el script intenta ejecutarse de nuevo.

4. ¿Qué se muestra con `st.dataframe()`?

Es el componente de visualización de datos, es el objeto de Pandas que está en la sesión y lo renderiza en el navegador como una tabla interactiva. A diferencia de una tabla estática, `st.dataframe()` permite al usuario ordenar las columnas, buscar datos o ampliar la vista, lo que le da un aspecto mucho más profesional y de dashboard a la aplicación
