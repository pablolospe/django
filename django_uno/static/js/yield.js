function percentageYield() { 
    var precioCompra = document.getElementById('precioCompra').value;
    var precioVenta = document.getElementById('precioVenta').value;

    var precioCompra = parseFloat(precioCompra);
    var precioVenta = parseFloat(precioVenta);

    // Check if either input is empty or NaN
    if (isNaN(precioCompra) || isNaN(precioVenta) || precioVenta === 0 ) {
        document.getElementById('resultadoRendimiento').textContent = 'Por favor, complete ambos campos con valores numéricos.';
    } else {
        // Calculate the percentage yield
        var resultado = (((precioCompra / precioVenta) - 1)*100).toFixed(2);
        // Update the result element with the calculated yield
        document.getElementById('resultadoRendimiento').textContent = 'El rendimiento porcentual es: ' + (resultado) + '%';
   
    }

}

