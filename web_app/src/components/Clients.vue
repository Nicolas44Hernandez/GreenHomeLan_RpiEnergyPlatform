<script setup>
import ClientsTable from './ClientsTable.vue'
</script>
<template>  
<h2>Registered Clients</h2>
  <div class="clients-table-container">
    <ClientsTable :clients="clientList" />
  </div>
</template>
<script>
import config from '@/config.js';
import axios from 'axios';

export default {
  data() {
    return {
      clientList: [],
    };
  },
  mounted() {
    // in startup
    console.log("in mounted Clients Vue");
    this.getClienstList();
  },
  methods: {
    getClienstList() {
      // Geting clients list from backend
      const url = `${config.BACKEND_URL}/clients/`;
      //const url ='/clients'
      axios.get(url)
        .then(response => {
          console.log("Clients list retreived:");
          console.log(response.data);
          this.clientList = response.data;          
        })
        .catch(error => {
          console.log(error);
        });
    },
  }
}
</script>

<style scoped>
.clients-table-container{
  margin-top:1%;
  display: flex;
  align-items: center;
}
h2{
  text-align: center;
}
</style>