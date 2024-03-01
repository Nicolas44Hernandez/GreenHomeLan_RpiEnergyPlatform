<script setup>
import SelectZoneItem from './SelectZoneItem.vue'
import SelectEnergeticianItem from './SelectEnergeticianItem.vue'
</script>
<template>  
<div class="buttons-container">
  <div class="column">   
      <div class="row">
        <button @click="onClick100" class="btn-100">
          Send Energy Recommendation 100% 
        </button>
      </div>
  </div>
  <div class="column">   
      <div class="row">
        <button @click="onClick25" class="btn-25">
          Send Energy Recommendation 25% 
        </button>
      </div>
  </div>
  <div class="column">   
      <div class="row">
        <button @click="onClick0" class="btn-0">
          Send Energy Recommendation 0% 
        </button>
      </div>
  </div>
</div> 
<div class="selection-container">
  <SelectZoneItem @zone-changed="handleZoneSelectionChanged" :zones=zones_list :selected-zone=zone></SelectZoneItem>
  <SelectEnergeticianItem @energetician-changed="handleEnergeticianSelectionChanged" :energeticians=energeticians_list :selected-energetician=energetician></SelectEnergeticianItem>
</div> 
</template>
<script>
import axios from 'axios';
import qs from 'qs';

export default {
  data() {
    return {
      zone: "",
      zones_list: [],
      energetician:"",
      energeticians_list: [],
    };
  },
  mounted() {
    // in startup
    console.log("in mounted Recommendations Vue");
    this.getConfig();
  },
  methods: {
    getConfig() {
      // Geting zones from backend
      //const zonesUrl ='http://localhost:5000/api/zones/'
      const zonesUrl = "/api/zones/";
      const jwt = JSON.parse(localStorage.getItem("user-info")).token;      
      axios.get(zonesUrl, { headers: { Authorization: `Bearer: ${jwt}` } })
        .then(response => {          
          let zones_array_str = response.data.zones.split("\'");
          let zones_list = []
          zones_array_str.forEach((element) => {
            if(element.length > 2){
              zones_list.push(element);
            }
          });

          this.zones_list = zones_list;  
          this.zone = this.zones_list[0];          
        })
        .catch(error => {
          console.log(error);
          this.inValidToken(error);
        });
      
      // Geting energetician from backend
      //const energeticiansUrl ='http://localhost:5000/api/energeticians/'
      const energeticiansUrl='/api/energeticians/';
      axios.get(energeticiansUrl, { headers: { Authorization: `Bearer: ${jwt}` } })
        .then(response => {          
          let energeticians_array_str = response.data.energeticians.split("\'");
          let energeticians_list = []
          energeticians_array_str.forEach((element) => {
            let ele = element.replace(" ", "");
            if(ele.length > 1){
              energeticians_list.push(ele);
            }
          });
          this.energeticians_list = energeticians_list;  
          this.energetician = this.energeticians_list[0];  
        })
        .catch(error => {
          console.log(error);
          this.inValidToken(error);
        });
    },
    sendRecommendations(power) {
      // Geting clients to aply recommendation
      //const url ='http://localhost:5000/api/clients'
      const url ='/api/clients';
      axios.get(url)
        .then(response => {
          response.data.forEach((client) => {
            if((this.zone == client.zone)&&(this.energetician == client.energetician)){
              this.sendRecommendation(client.ip, client.port, client.zone, client.energetician, client.contract_class, power);
            }
          }); 
        })
        .catch(error => {
          console.log(error);
          this.inValidToken(error);
        });
    },
    handleZoneSelectionChanged(newVal) {          
      this.zone = newVal;
      console.log("Zone selection has changed");  
      console.log(this.zone);
    },
    handleEnergeticianSelectionChanged(newVal) {          
      this.energetician = newVal;
      console.log("Energetician selection has changed");  
      console.log(this.energetician);
    },
    onClick100(){
      console.log("onClick100");
      this.sendRecommendations("100");
    },
    onClick25(){
      console.log("onClick25");
      this.sendRecommendations("25");
    },
    onClick0(){
      console.log("onClick0");
      this.sendRecommendations("0");
    },
    sendRecommendation(client_ip, port, zone, energetician, contract_class, power){

      const client_url = `http://${client_ip}:${port}`;
      console.log("Sending recommendation to: "+ client_url + "  power: " + power);

      //Get current datetime
      const now = new Date()
      const now_str = now.toISOString()      

      // Get end datetime
      //TODO: add picker
      const end = new Date(now.setMinutes(now.getMinutes() + 3));
      const end_str = end.toISOString()      
      //const test_ip = "http://192.168.1.19:5000"  //eth
      //const test_ip = "http://192.168.102.21:5000"  //wifi 
      
      const data = {
        id_zone: zone,
        recomendation_datetime: now_str,
        msg_title: "Recomendation",
        power: power,
        //start_datetime: now_str,
        sender: "PIE",
        id_energy_supplier: energetician,
        //end_datetime: end_str,
        msg_id: "001",
        recommendation_class: contract_class,
      };
      const queryString = qs.stringify(data);
      const url = `${client_url}/energy_recomendations?${queryString}`;
      console.log(url);
      axios.post(url)
        .then(response => {          
          console.log("recommendation sent");
        })
        .catch(error => {
          console.log(error);
          this.inValidToken(error);
        });
    },
    inValidToken(msg){
        localStorage.clear();
        this.$router.push({name: "login"});
    }, 
  }
}
</script>

<style scoped>
.buttons-container{
  margin-top:5%;
  display: flex;
  align-items: center;
}
.btn-100 {
  background-color: rgb(17, 136, 53);
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin:5%; 
  padding: 5%;
}
.btn-25 {
  background-color: rgb(235, 192, 53);
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin:2%;
  padding: 5%;
}
.btn-0 {
  background-color: rgb(180, 17, 17);
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin:2%;
  padding: 5%;
}
.selection-container{
  margin-top:2%;
  margin-left:10%;
  display: grid;
  align-items: center;
}

.column {
    float: left;
    margin-top: 4px;
    margin-bottom: 4px;
} 
.row{
    margin: 0px;
    padding: 0px;
    /*border: 1px solid red;*/
} 
</style>