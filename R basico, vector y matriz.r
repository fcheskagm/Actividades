# Le solicitamos al usuario que ingrese los numeros de un vector separados "," para que los sume 
entrada_vector <- readline(prompt = "Ingresa un vector de números (separados por comas): ")
mi_vector <- as.numeric(strsplit(entrada_vector, ",")[[1]])

# Mostramos elvector y luego calculamos la suma y la mostramos
cat("El vector ingresado es:", mi_vector, "\n")
suma <- sum(mi_vector)
cat("La suma es:", suma, "\n")

# Ahora le solicitamos al usuario que ingrese 4 numeros separados "," para una matriz 2x2 
entrada_matriz <- readline(prompt = "Ingresa 4 numeros para crear una matriz 2x2 (separados por comas): ")
mi_matriz <- matrix(as.numeric(strsplit(entrada_matriz, ",")[[1]]), nrow = 2, ncol = 2)

# Y dos numeros para el vector de terminos independientes, para resolver el sistema y mostrarlo
entrada_vector <- readline(prompt = "Ingresa 2 numeros para crear un vector (separados por comas): ")
mi_vector <- as.numeric(strsplit(entrada_vector, ",")[[1]])
cat("La matriz ingresada es:\n")
print(mi_matriz)
solucion <- solve(mi_matriz, b = mi_vector)
cat("La solución es x =", solucion[1], "y =", solucion[2], "\n")