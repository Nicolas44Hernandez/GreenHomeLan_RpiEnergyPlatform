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
      //TODO: Get from backend
      this.clientList=[
        { 
          id: 1, 
          zone: 'Zone 1',
          energetician: 'E1',
          id_energetician: '1',
          class: '6KVA',
          fai: 'Orange',
          id_client_fai: '1',
          name_client_fai: 'MyOrchestrator',
          ip: '80.65.254.231',
          port: '80',
        },
        { 
          id: 2, 
          zone: 'Zone 1',
          energetician: 'E1',
          id_energetician: '1',
          class: '6KVA',
          fai: 'Orange',
          id_client_fai: '2',
          name_client_fai: 'MyOrchestrator2',
          ip: '80.65.254.232',
          port: '80',
        },
        { 
          id: 3, 
          zone: 'Zone 2',
          energetician: 'E1',
          id_energetician: '1',
          class: '6KVA',
          fai: 'Orange',
          id_client_fai: '3',
          name_client_fai: 'MyOrchestrator3',
          ip: '80.65.254.233',
          port: '80',
        },
        { 
          id: 4, 
          zone: 'Zone 3',
          energetician: 'E2',
          id_energetician: '2',
          class: '6KVA',
          fai: 'Orange',
          id_client_fai: '4',
          name_client_fai: 'MyOrchestrator4',
          ip: '80.65.254.234',
          port: '80',
        },
        { 
          id: 5, 
          zone: 'Zone 1',
          energetician: 'E1',
          id_energetician: '1',
          class: '6KVA',
          fai: 'Orange',
          id_client_fai: '5',
          name_client_fai: 'MyOrchestrator5',
          ip: '80.65.254.235',
          port: '80',
        },
        { 
          id: 6, 
          zone: 'Zone 3',
          energetician: 'E2',
          id_energetician: '3',
          class: '6KVA',
          fai: 'Orange',
          id_client_fai: '6',
          name_client_fai: 'MyOrchestrator6',
          ip: '80.65.254.236',
          port: '80',
        },
      ]
            
      //console.log(config.CONFIGURATION_URL);
      // axios.get(config.CONFIGURATION_URL)
      //   .then(response => {
      //     console.log("Configuration retreieved:");
      //     this.pitches = response.data.pitches;
      //     this.video = response.data.video;
      //     console.log(response.data);
      //   })
      //   .catch(error => {
      //     console.log(error);
      //     // TODO: Handle errors
      //   });
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