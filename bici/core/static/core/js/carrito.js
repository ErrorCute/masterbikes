let carrito = [];

// función para agregar un producto al carrito
function agregarProducto(nombreProducto,precioproducto) {
	// crear objeto producto
	let producto = {
		nombre: nombreProducto,
		precio: precioproducto// precio aleatorio entre 1 y 100
	};

	// agregar producto al arreglo carrito
	carrito.push(producto);

	// actualizar lista de productos en el carrito
	actualizarCarrito();
}

// función para actualizar la lista de productos en el carrito
function actualizarCarrito() {
	let listaCarrito = document.getElementById("listaCarrito");
	let total = 0;

	// borrar lista actual
	listaCarrito.innerHTML = "";

	// agregar nuevos elementos a la lista
	for (let i = 0; i < carrito.length; i++) {
		let producto = carrito[i];
		let item = document.createElement("li");
		item.innerText = producto.nombre + " - $" + producto.precio;
		listaCarrito.appendChild(item);

		// actualizar total
		total += producto.precio;
	}

	// actualizar total en la página
	document.getElementById("total").innerText = total;
}
