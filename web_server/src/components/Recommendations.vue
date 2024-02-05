<script setup>
import SelectZoneItem from './SelectZoneItem.vue'
import SelectEnergeticianItem from './SelectEnergeticianItem.vue'
import SelectPowerItem from './SelectPowerItem.vue'
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
  <SelectPowerItem @power-changed="handlePowerSelectionChanged" :powers=powers_list :selected-power=power></SelectPowerItem>
</div> 
</template>
<script>
import config from '@/config.js';

export default {
  data() {
    return {
      zone: "",
      zones_list: [],
      energetician:"",
      energeticians_list: [],
      power:"",
      powers_list: [],
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
      //TODO: Get from backend
      this.zone="Zone 1"
      this.zones_list = ["Zone 1", "Zone 2", "Zone 3", "Zone 4", "Zona x"]; 
      
      // Geting energetician from database
      //TODO: Get from backend
      this.energetician="E1"
      this.energeticians_list = ["E1", "E2", "E3"]; 

      // Geting powers from config
      this.powers_list = config.POWER_LIST;
      this.power=this.powers_list[0];

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
    handlePowerSelectionChanged(newVal) {          
      this.power = newVal;
      console.log("Power selection has changed");  
      console.log(this.power);
    },
    onClick100(){
      console.log("onClick100");
    },
    onClick25(){
      console.log("onClick25");
    },
    onClick0(){
      console.log("onClick0");
    }
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