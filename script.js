let dadosClientes = document.querySelector("#dadosClientes")

fetch('clientes.json')
    .then(response => response.json())
    .then(dados => {
        dadosCliente.innerHTML = `<p>ID: ${dados.Nome}</p>
                                  <p>Nome: ${dados.Telefone}</p>
                                  <p>Email: ${dados.Email}</p>
                                  <p>Cpf: ${dados.Cpf}</p>`;
    })