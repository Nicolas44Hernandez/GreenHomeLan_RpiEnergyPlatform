<template>
    <div class="item">     
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Zone</th>
            <th>Energetician</th>
            <th>ID Energetician</th>
            <th>Contract Class</th>
            <th>FAI</th>
            <th>ID Client FAI</th>
            <th>Name Client FAI</th>
            <th>IP</th>
            <th>Port</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="client in clients" :key="client.id">
            <td>{{ client.id }}</td>
            <td>{{ client.zone }}</td>
            <td>{{ client.energetician }}</td>
            <td>{{ client.id_energetician }}</td>
            <td>{{ client.class }}</td>
            <td>{{ client.fai }}</td>
            <td>{{ client.id_client_fai }}</td>
            <td>{{ client.name_client_fai }}</td>
            <td>{{ client.ip }}</td>
            <td>{{ client.port }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      clients: {
        type: Array,
        required: true,
        //     validator: function(value) {
        //       // Check if each item in the array is a string
        //       return value.every(item => typeof item === 'string')
        //     }
      },
    },
  }
  </script>

  <style scoped>
  table {
  border-collapse: collapse;
  width: 100%;
}

th, td {
  border: 1px solid #0e0e0e; /* Add a border on all sides of each cell */
  padding: 8px; /* Add padding for better readability */
  text-align: left;
}
th {
  background-color: #f2f2f2; /* Add a background color to header cells */
  font-weight: bold; /* Make the column headers bold */
}
</style> 
  