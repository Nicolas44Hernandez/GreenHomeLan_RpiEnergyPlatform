<template>
    <div class="item">     
      <div class="column-left">
        Zone to apply  
      </div>
      <div class="column-right">
        <div>  
          <select v-model="zoneSelection" class="select">
            <option v-for="zone in zones" :key="zone">{{ zone }}</option>
          </select>  
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      selectedZone: {
        type: String,
        required: true,
      },
      zones: {
        type: Array,
        required: true,
        validator: function(value) {
          // Check if each item in the array is a string
          return value.every(item => typeof item === 'string')
        }
      }
    },
    mounted() {
      this.zoneSelection = this.selectedZone;
    },
    data() {
      return {
        zoneSelection: "Zone 1",
      }
    },
    watch: {
      zoneSelection(newVal) {
        this.$emit('zone-changed', newVal);
      },
      selectedZone(newVal) {
        this.zoneSelection = newVal;
      },
    }  
  }
  </script>
  
  <style scoped>
  .column-left{
    flex-basis: 30%;
    font-size: 110%;
  }
  .column-right {
    flex-basis: 50%;
    margin-left: 1%; 
  }
  .item {
    margin-top: 2rem;
    display: flex;
  }
  .select {
    font-size: 100%;
    padding: 2%;
    width: 100%;
  }
  i {
    display: flex;
    place-items: center;
    place-content: center;
    width: 32px;
    height: 32px; 
    color: var(--color-text);
  }
  </style>
  