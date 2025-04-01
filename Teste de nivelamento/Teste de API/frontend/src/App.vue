<template>
    <div id="app">
        <h1>Busca de Operadoras de Saúde</h1>
        <!-- Componente de busca de operadoras -->
        <SearchOperadoras />
    </div>
</template>

<script>
    import SearchOperadoras from './components/SearchOperadoras.vue'; // Importa o componente SearchOperadoras

    export default {
        name: 'App', // Nome do componente principal
        components: {
            SearchOperadoras
        }
    };
</script>

<style>
    /* Estilo para o container principal */
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        text-align: center;
        margin-top: 60px;
    }
</style>