// Função de cadastro do Seller
document
  .getElementById("formCadastro")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const nome = document.getElementById("nome").value;
    const cnpj = document.getElementById("cnpj").value;
    const email = document.getElementById("email").value;
    const celular = document.getElementById("celular").value;
    const senha = document.getElementById("senha").value;

    fetch("http://localhost:8080/api/sellers", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nome: nome,
        cnpj: cnpj,
        email: email,
        celular: celular,
        senha: senha,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        alert("Cadastro realizado com sucesso!");
      })
      .catch((error) => {
        alert("Erro ao cadastrar o mini mercado!");
      });
  });

// Função de login do Seller
document
  .getElementById("formLogin")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const email = document.getElementById("loginEmail").value;
    const senha = document.getElementById("loginSenha").value;

    fetch("http://localhost:8080/api/auth/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email: email,
        senha: senha,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.token) {
          localStorage.setItem("authToken", data.token);
          alert("Login bem-sucedido!");
          document.getElementById("loginSeller").style.display = "none";
          document.getElementById("dashboard").style.display = "block";
        } else {
          alert("E-mail ou senha inválidos!");
        }
      })
      .catch((error) => {
        alert("Erro ao realizar o login!");
      });
  });

// Função para carregar os produtos no Dashboard
function loadProducts() {
  const token = localStorage.getItem("authToken");
  if (!token) {
    alert("Você precisa estar logado!");
    return;
  }

  fetch("http://localhost:8080/api/products", {
    method: "GET",
    headers: {
      Authorization: `Bearer ${token}`,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const productList = document.getElementById("productList");
      productList.innerHTML = "";

      data.forEach((product) => {
        const li = document.createElement("li");
        li.textContent = `${product.nome} - R$${product.preco} - Estoque: ${product.quantidade}`;
        productList.appendChild(li);
      });
    })
    .catch((error) => {
      alert("Erro ao carregar os produtos!");
    });
}
