function showProducts() {
    fetch('/products/')
        .then(response => response.json())
        .then(products => {
            let productListHTML = '<h2>Products List</h2><ul>';
            products.forEach(product => {
                productListHTML += `<li>ID: ${product.id}</li>
                    <li>Precio : ${product.price}</li>
                    <li>Cantidad : ${product.amount}</li>
                    <li>Categoria : ${product.category}</li>
                    <li>Descripcion :${product.description}</li>
                    <li>
                    <button onclick="showProductDetail(${product.id})">Detalle</button>
                   -
                    <button onclick="showUpdateForm(${product.id})">Actualizar</button>
                    -
                    <button onclick="deleteProduct(${product.id})">Eliminar</button>
                    </li>
                    <hr>`;
            });
            productListHTML += '</ul>';
            document.getElementById('content').innerHTML = productListHTML;
        });
}

function showProductDetail(id) {
    fetch(`/products/${id}`)
        .then(response => response.json())
        .then(product => {
            let productDetailHTML = `<h2>Product Detail</h2>
                <p>Descripcion: ${product.description}</p>
                <p>Price: ${product.price}</p>
                <p>Cantidad : ${product.amount}</p>
                <button onclick="showProducts()">Back to List</button>`;
            document.getElementById('content').innerHTML = productDetailHTML;
        });
}

function showCreateForm() {
    // data=(product.amount, product.price, product.description, product.category)
    let formHTML = `<h2>Create New Product</h2>
        <form onsubmit="createProduct(event)">
            <label for="amount">Cantidad:</label>
            <input type="number" id="amount" name="amount" required><br>
            <label for="price">Price:</label>
            <input type="number" id="price" name="price" required><br>
            <label for="description">Descripcion:</label>
            <input type="text" id="description" name="description" required><br>
            <label for="category">categoria:</label>
            <input type="text" id="category" name="category" required><br>
            <button type="submit">Create</button>
        </form>`;
    document.getElementById('content').innerHTML = formHTML;
}

function createProduct(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    fetch('/products/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        showProducts();
    });
}

function showUpdateForm(id) {
    // data=(product.amount, product.price, product.description, product.category)
    fetch(`/products/${id}`)
        .then(response => response.json())
        .then(product => {

     
            let formHTML = `<h2>Actualizar Product</h2>
                <form id="updateProductForm">
                   
                    <label for="amount">Cantidad:</label>
                    <input type="number" id="amount"  name="amount" value="${product.amount}" required><br>
                    
                    <label for="price">Price:</label>
                    <input type="number" id="price" name="price" value="${product.price}" required><br>
                    
                    <label for="description">Descripcion:</label>
                    <input type="text" id="description" name="description" placeholder="${product.description}" required><br>
                    
                    <label for="category">categoria:</label>
                    <input type="text" id="category" name="category" value="${product.category}" required><br>
                    
                    <button type="submit">Actualizar</button>
                </form>`;
            document.getElementById('content').innerHTML = formHTML;
            document.getElementById('updateProductForm').onsubmit = function(event) {
                event.preventDefault();
                updateProduct(event, id);
            };
        });
}

function updateProduct(event, id) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const data = Object.fromEntries(formData.entries());
    fetch(`/products/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        showProducts();
    });
  
}

function deleteProduct(id) {
    fetch(`/products/delete_product/${id}`, {
        method: 'DELETE'
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        showProducts();
    });
}
