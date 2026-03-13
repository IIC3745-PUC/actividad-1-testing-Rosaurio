[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AG7uuOyW)

# Declaración breve de uso de IA

## Registro de uso

**Herramienta:** ChatGPT
**Modelo:** GPT-5.3
**Parte de la actividad en la que se uso:** Código
**Prompt:** 
```text
Uno de los prompts que use fue: raise PricingError("qty must be > 0") Como hago un assert si quiero llegar a este resultado?
```
**Evaluación de la respuesta:** Muy buena
**Justificación:** Me ayudó mucho a entender cómo plantear todas las pruebas en las que se quería evaluar una respuesta de error
**¿Requirió trabajo adicional?:** Sí
**Trabajo adicional realizado:** En este caso me explicó cómo usar el asser cuando se quiere evaluar una respuesta de error pero luego tuve que ir aplicándolo a todos los test en los que fuera necesario

## Reflexión final sobre el uso de IA

**Describa brevemente cómo aportó la herramienta de IA al desarrollo de esta actividad:**
Cómo ya mencioné, me explicó cómo usar un tipo específico de assert que me dió una base para ir replicándolo en todos los casos en los que fuera necesario. También me ayudó con cómo generar una respuesta para métodos de mocks, cómo usar assert cuando se evalúa un "if not ok" y cómo evaluar mocks que no retornan nada. Sé que muchas de estas cosas están en la documentación de unittest.mock, sin embargo usar ChatGPT para dudas específicas me ayudó a ahorrar mucho tiempo. Finalmente, también me ayudó con errores que no ví a primera vista.

**Indique cuáles fueron las principales limitaciones de la herramienta en este caso:**
No se me ocurren limitaciones específicas que haya visto en este caso. Tal vez me gustaría que además de dar una respuesta específica diera documentación al respecto, pero tal vez si se la hubiera pedido directamente me la habría dado.

**Explique qué parte del trabajo final considera que corresponde principalmente a su propio aporte intelectual:**
ChatGPT me ayudó con el primer test que evalúa error de pricing service pero el resto los hice todos sola. Los de checkout me costaron un poco más porque no sabía bien cómo definir resultados para mocks usando return_value, específicamente cuando el resultado debía ser ok=False. Para estas últimas cosas también me ayudó ChatGPT. Para los tests de checkout diría que ChatGPT me ayudó con una linea de código por test en promedio y para los de pricing me ayudó con dos lineas de código en total. Todo el resto diría que es aporte mío.