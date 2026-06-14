estudiantes = []
cola_consultas = []

def buscarPorLegajo(legajo):
    for est in estudiantes:
        if est["legajo"] == legajo:
            return est
    return None

def calcularPromedio(calificaciones):
    if len(calificaciones) == 0:
        return 0
    return sum(calificaciones) / len(calificaciones)

def pedir_legajo(mensaje="Ingrese legajo: "):
    """Solicita un legajo numérico entero positivo al usuario."""
    while True:
        entrada = input(mensaje).strip()
        if entrada.isdigit() and int(entrada) > 0:
            return int(entrada)
        print("El legajo debe ser un número entero positivo.")

def pedir_calificacion():
    """Solicita una calificación válida (0-10) al usuario."""
    while True:
        entrada = input("  Ingrese calificación (0 a 10): ").strip()
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            print("La calificación debe estar entre 0 y 10.")
        except ValueError:
            print("Ingrese un numero valido.")


def mostrar_estudiante(est):
    """Imprime los datos completos de un estudiante."""
    cant = len(est["calificaciones"])
    print(f"Nombre  : {est['nombre']}")
    print(f"Legajo  : {est['legajo']}")
    print(f"Notas   : {est['calificaciones']}  ({cant} calificación/es)")
    print(f"Promedio: {est['promedio']:.2f}")

#  Opcion 1
def registrar_estudiante():
    print("\n── Registrar nuevo estudiante ──")
    nombre = input("  Nombre completo: ").strip()
    if nombre == "":
        print("  ⚠  El nombre no puede estar vacío.")
        return

    legajo = pedir_legajo()

    if buscarPorLegajo(legajo) is not None:
        print(f"  ⚠  El legajo {legajo} ya está registrado.")
        return

    nuevo = {
        "nombre": nombre,
        "legajo": legajo,
        "calificaciones": [],
        "promedio": 0
    }
    estudiantes.append(nuevo)
    print(f"  ✔  Estudiante '{nombre}' (legajo {legajo}) registrado correctamente.")

#  Opcion 2
def registrar_calificacion():
    print("\n── Registrar calificación ──")
    if len(estudiantes) == 0:
        print("  ⚠  No hay estudiantes registrados.")
        return

    print("  Estudiantes registrados:")
    for est in estudiantes:
        print(f"    Legajo {est['legajo']} – {est['nombre']}")

    legajo = pedir_legajo()
    est = buscarPorLegajo(legajo)
    if est is None:
        print(f"  ⚠  No existe ningún estudiante con legajo {legajo}.")
        return

    nota = pedir_calificacion()
    est["calificaciones"].append(nota)
    est["promedio"] = calcularPromedio(est["calificaciones"])
    print(f"  ✔  Calificación {nota} agregada a {est['nombre']}. "
          f"Nuevo promedio: {est['promedio']:.2f}")

#  Opcion 3
def agregar_a_cola():
    print("\n── Agregar a cola de consultas ──")
    legajo = pedir_legajo()
    est = buscarPorLegajo(legajo)
    if est is None:
        print(f"  ⚠  No existe ningún estudiante con legajo {legajo}.")
        return
    # Permitir agregarlo aunque ya esté en cola (puede tener varias consultas)
    cola_consultas.append(legajo)
    pos = len(cola_consultas)
    print(f"  ✔  {est['nombre']} agregado a la cola. Posición actual: {pos}")

#  Opcion 4
def atender_consulta():
    print("\n── Atender siguiente consulta ──")
    if len(cola_consultas) == 0:
        print("  ℹ  La cola de consultas está vacía.")
        return

    legajo_atendido = cola_consultas.pop(0)        # FIFO: se saca del frente
    est = buscarPorLegajo(legajo_atendido)
    print(f"  ✔  Atendiendo consulta de:")
    mostrar_estudiante(est)
    print(f"  Quedan {len(cola_consultas)} estudiante/s en espera.")

# Opcion 5
def ver_estudiantes():
    print("\n── Listado de estudiantes (mayor a menor promedio) ──")
    if len(estudiantes) == 0:
        print("  ℹ  No hay estudiantes registrados.")
        return

    # Ordenar por promedio de mayor a menor (sin modificar la lista original)
    ordenados = sorted(estudiantes, key=lambda e: e["promedio"], reverse=True)

    print(f"  {'#':<4} {'Nombre':<25} {'Legajo':<10} {'Notas':<6} {'Promedio'}")
    print(f"  {'-'*60}")
    for i, est in enumerate(ordenados, start=1):
        cant = len(est["calificaciones"])
        print(f"  {i:<4} {est['nombre']:<25} {est['legajo']:<10} "
              f"{cant:<6} {est['promedio']:.2f}")

# Opcion 6
def verEstadisticas():
    print("\n── Estadísticas generales ──")
    total = len(estudiantes)
    print(f"  Total de estudiantes registrados : {total}")
    print(f"  Estudiantes en cola de consultas : {len(cola_consultas)}")

    if total == 0:
        print("  ℹ  Sin estudiantes, no hay estadísticas adicionales.")
        return

    promedios = [est["promedio"] for est in estudiantes]
    promedio_general = calcularPromedio(promedios)
    print(f"  Promedio general de la materia   : {promedio_general:.2f}")

    # Estudiante con mejor y peor promedio
    mejor = max(estudiantes, key=lambda e: e["promedio"])
    peor  = min(estudiantes, key=lambda e: e["promedio"])
    print(f"  Mejor promedio : {mejor['nombre']} (legajo {mejor['legajo']}) "
          f"– {mejor['promedio']:.2f}")
    print(f"  Peor promedio  : {peor['nombre']} (legajo {peor['legajo']}) "
          f"– {peor['promedio']:.2f}")
    
# Menu
def mostrar_menu():
    print("SISTEMA DE GESTION DE ESTUDIANTES\n")
    print("1. Registrar nuevo estudiante")
    print("2. Registrar calificacion de un estudiante")
    print("3. Agregar estudiante a la cola de consultas")
    print("4. Atender siguiente consulta")
    print("5. Ver todos los estudiantes y sus promedios")
    print("6. Ver estadisticas generales")
    print("7. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("  Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            registrar_calificacion()
        elif opcion == "3":
            agregar_a_cola()
        elif opcion == "4":
            atender_consulta()
        elif opcion == "5":
            ver_estudiantes()
        elif opcion == "6":
            verEstadisticas()
        elif opcion == "7":
            print("\nChau\n")
            break
        else:
            print("Opcion no contemplada, ingrese una opcion valida")
    main()