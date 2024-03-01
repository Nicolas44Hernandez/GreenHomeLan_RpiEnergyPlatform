<template>  
<div class="register-container">
  <div class="column-logo">
    <img alt="EPI logo" class="logo" src="@/assets/rayo.png"/>
  </div>
  <div class="column-login">
    <h1>Login</h1>
  </div>
  <div class="column-register">
    <input type="text" v-model="email" placeholder="Enter id"/>
  </div>
  <div class="column-register">
    <input type="text" v-model="password" placeholder="Enter password"/>
  </div>
  <div class="column-register">
    <button v-on:click="onClickLogin">Login</button>
  </div>   
</div>

</template>
<script>
import axios from 'axios';
import qs from 'qs';

export default {
  data() {
    return {
      email: "",
      password: "",
      token: ""
    };
  },
  mounted() {
    // in startup
    console.log("in mounted Login Vue");
    // Call methods if necessary
  },
  methods: {
    onClickLogin(){
      console.log("onClickLogin");
      console.log("email:"+this.email + "password:"+this.password);

      // Try to login
      //const loginUrl ='http://localhost:5000/api/login/'
      const loginUrl = "/api/login/";
      const data = {
        email: this.email,
        password: this.password,
      };
      const queryString = qs.stringify(data);
      const url = `${loginUrl}?${queryString}`;
      
      console.log('loginUrl: ' + url);      

      axios.post(url)
        .then(response => {   
          //console.log(response.data);
          if(response.status==200 ){
            const userAuth = {
              email: this.email,
              password: this.password,
              token: response.data.token,
            };
            localStorage.setItem("user-info", JSON.stringify(userAuth));
            this.$router.push({name: "home"})
          }        
        })
        .catch(error => {
          console.log(error);
        });
      
    },

  }
}
</script>
<style scoped>
.register-container{
  margin-top:15%;
  margin-left:10%;
  display: grid;
  align-items: center;
}
.column-register{
  margin-top:5%;
  display: grid;
  align-items: center;
}
.column-register input{
  width: 100%;
  height: 100%;
  margin:5%; 
  padding: 5%;
  border: 1px solid rgb(224, 124, 41);
}
.column-register button{
  background-color: rgb(224, 124, 41);
  color: black;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin:5%; 
  padding: 5%;
  margin-left: 15%;
}
.column-login {
    margin-left: 25%;
    float: left;
    margin: 10%;
    margin-left: 25%;
} 
.column-logo {
    margin-top: 10%;
    margin-left: 25%;
    margin-bottom: 10%;
    display: grid;
    align-items: center;
} 
</style>