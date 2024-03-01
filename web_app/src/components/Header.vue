<script setup>
import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
<header v-if="!isLoginPage">
    <div>
      <img alt="EPI logo" class="logo" src="@/assets/rayo.png"/>
    </div>
    <div>
      <a class="logout" v-on:click="logout" href="#">Logout</a>  
    </div>
    <div>
      <div class="wrapper">      
        <nav>
            <RouterLink to="/">Home</RouterLink>
            <RouterLink to="/clients"  >Clients</RouterLink>
            <RouterLink to="/about">About</RouterLink>                  
        </nav>
      </div>    
    </div>   
  </header>
  <div>
    <RouterView />
  </div>  
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
        isLoginPage: true
    };
  },
  watch: {
    '$route'(to, from) {
      // Update currentRoute whenever route changes
      this.isLoginPage = to.path == "/login"
    }
  },
  methods:{
    logout(){
        this.$emit('logout',"");
    },     
  },
}

</script>

<style scoped>
header {
    line-height: 1.5;
    position: fixed;
    top: 0;
    left: 0;    
    width: 100%;
    background-color: #fff; /* Set background color if needed */
    z-index: 1000; /* Set a high z-index to make sure it stays above other elements */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Optional: Add a box shadow for a subtle effect */
  }
.logout {
    position: fixed;
    text-align: center;
    top: 0;
    left: 95%;  
    right: 1;    
    width: 5%;
    z-index: 1001; /* Set a high z-index to make sure it stays above other elements */
  }

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 0;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: grid;
    place-items: center;
    top: 0;
    /* position: fixed; */
    width: 100%;
  }

  .logo {
    margin: 0 0 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: center;
    flex-wrap: wrap;
    top: 0;
    /* position: fixed; */
    width: 100%;
  }

  nav {
    /* text-align: left;
    margin-left: -1rem; */
    font-size: 1rem;

    padding: 0;
    /* margin-top: 1rem; */
  }
}
</style>
