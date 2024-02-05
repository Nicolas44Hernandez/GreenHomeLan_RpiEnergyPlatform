<template>
    <div class="item">     
      <div class="column-left">
        Energetician to apply  
      </div>
      <div class="column-right">
        <div>  
          <select v-model="energeticianSelection" class="select">
            <option v-for="energetician in energeticians" :key="energetician">{{ energetician }}</option>
          </select>  
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      selectedEnergetician: {
        type: String,
        required: true,
      },
      energeticians: {
        type: Array,
        required: true,
        validator: function(value) {
          // Check if each item in the array is a string
          return value.every(item => typeof item === 'string')
        }
      }
    },
    mounted() {
      this.zoneSelection = this.selectedEnergetician;
    },
    data() {
      return {
        energeticianSelection: "E1",
      }
    },
    watch: {
      energeticianSelection(newVal) {
        this.$emit('energetician-changed', newVal);
      },
      selectedEnergetician(newVal) {
        this.energeticianSelection = newVal;
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
  