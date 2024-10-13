<template>
  <div id="app">
    <nav>
      <router-link to="/inventory">{{ $t('navigation.inventory') }}</router-link> |
      <router-link to="/sales">{{ $t('navigation.sales') }}</router-link> |
      <router-link to="/prediction">{{ $t('navigation.prediction') }}</router-link> |
      <router-link to="/analytics">{{ $t('navigation.analytics') }}</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
