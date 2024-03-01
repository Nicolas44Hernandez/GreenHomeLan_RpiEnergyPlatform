<script setup>
import Header from '@/components/Header.vue';
</script>

<template>
  <Header @logout="logoutHandler"></Header>
</template>

<script>
export default {
  name: 'App',
  
  data() {
    return {
        logged: false
    };
  },
  mounted() {
    // in startup
    let userInfo = localStorage.getItem("user-info");
    console.log("userInfo: "+ userInfo);
    if(!userInfo){
      this.logged = false; 
      this.$router.push({name: "login"})     
    }
    else{
      this.logged = true;
      console.log("User already logged " + userInfo);
      this.$router.push({name: "home"})
    }
  },
  components: {
    Header
  },
  methods:{
    logoutHandler()
      {
        localStorage.clear();
        this.$router.push({name: "login"});
      },
  },
}

</script>