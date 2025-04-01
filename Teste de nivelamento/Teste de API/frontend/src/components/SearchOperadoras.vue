<template>
    <div>
        <!-- Campo de entrada para busca -->
        <input
            v-model="searchQuery"
            @input="search"
            placeholder="Digite para buscar (Razão Social, Nome Fantasia, CNPJ ou Cidade)"
            type="text"
            class="search-input"
        />

        <!-- Tabela para exibir os resultados da busca -->
        <table v-if="results.length" class="results-table">
            <thead>
                <tr>
                    <th>Registro ANS</th>
                    <th>CNPJ</th>
                    <th>Razão Social</th>
                    <th>Nome Fantasia</th>
                    <th>Cidade</th>
                    <th>UF</th>
                </tr>
            </thead>

            <tbody>
                <!-- Itera sobre os resultados e exibe cada operadora em uma linha -->
                <tr v-for="(operadora, index) in results" :key="operadora.Registro_ANS || index">
                    <td>{{ operadora.Registro_ANS || 'N/A' }}</td>
                    <td>{{ operadora.CNPJ || 'N/A' }}</td>
                    <td>{{ operadora.Razao_Social || 'N/A' }}</td>
                    <td>{{ operadora.Nome_Fantasia || '-' }}</td>
                    <td>{{ operadora.Cidade || 'N/A' }}</td>
                    <td>{{ operadora.UF || 'N/A' }}</td>
                </tr>
            </tbody>
        </table>
        <!-- Mensagem exibida se não houver resultados e a busca não estiver carregando -->
        <p v-else-if="searchQuery && !loading">Nenhum resultado encontrado.</p>
    </div>
</template>

<script>
    import axios from 'axios'; // Importa a biblioteca axios para fazer requisições HTTP
    import debounce from 'lodash/debounce'; // Importa debounce para limitar chamadas à API

    export default {
        data() {
            return {
                searchQuery: '', // Armazena o texto digitado no campo de busca
                results: [], // Armazena os resultados retornados pela API
                loading: false, // Indica se a busca está em andamento
            };
        },

        methods: {
            // Método para buscar dados na API
            search: debounce(async function() {
                if (!this.searchQuery) {
                    this.results = [];
                    return;
                }
                this.loading = true; // Indica que a busca está em andamento
                try {
                    // Faz uma requisição GET para a API de busca com o texto digitado
                    const response = await axios.get('/api/search', {
                    params: { q: this.searchQuery } // Envia o texto da busca como parâmetro
                    });
                    this.results = [...response.data]; // Atualiza os resultados com os dados retornados
                } catch (error) {
                    console.error('Erro na busca:', error.message);
                    if (error.response) {
                    console.error('Resposta do servidor:', error.response.data);
                    }
                } finally {
                    this.loading = false;  // Finaliza o estado de carregamento
                }
            }, 300) // Debounce de 300ms para evitar chamadas excessivas à API
        }
    };
</script>

<style scoped>
    /* Estilo para o campo de entrada */
    .search-input {
        width: 50%;
        padding: 10px;
        margin-bottom: 20px;
        font-size: 16px;
    }

    /* Estilos para a tabela de resultados */
    .results-table {
        width: 80%;
        margin: 0 auto;
        border-collapse: collapse;
    }

    .results-table th, .results-table td {
        border: 1px solid #ddd;
        padding: 8px;
    }

    .results-table td {
        background-color: #f2f2f2;
    }
</style>