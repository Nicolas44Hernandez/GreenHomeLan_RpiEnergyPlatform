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
      //const url ='http://localhost:5000/api/clients/'
      const url ='/api/clients/'
      const jwt = JSON.parse(localStorage.getItem("user-info")).token;      
      axios.get(url, { headers: { Authorization: `Bearer: ${jwt}` } })
        .then(response => {
          console.log("Clients list retreived:");
          console.log(response.data);
          this.clientList = response.data;          
        })
        .catch(error => {
          console.log(error);  
          this.inValidToken(error);
        });
    },
    inValidToken(msg){
        console.log("Error msg: "+ msg);
        localStorage.clear();
        this.$router.push({name: "login"});
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