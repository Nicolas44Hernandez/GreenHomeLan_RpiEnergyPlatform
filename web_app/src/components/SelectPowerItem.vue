<template>
    <div class="item">     
      <div class="column-left">
        Power to apply  
      </div>
      <div class="column-right">
        <div>  
          <select v-model="powerSelection" class="select">
            <option v-for="power in powers" :key="power">{{ power }}</option>
          </select>  
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      selectedPower: {
        type: String,
        required: true,
      },
      powers: {
        type: Array,
        required: true,
        validator: function(value) {
          // Check if each item in the array is a string
          return value.every(item => typeof item === 'string')
        }
      }
    },
    mounted() {
      this.powerSelection = this.selectedPower;
    },
    data() {
      return {
        powerSelection: "100%",
      }
    },
    watch: {
      powerSelection(newVal) {
        this.$emit('power-changed', newVal);
      },
      selectedPower(newVal) {
        this.powerSelection = newVal;
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
  