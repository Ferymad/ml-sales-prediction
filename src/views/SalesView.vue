<template>
  <div>
    <SalesList />
    <SalesForm />
  </div>
</template>

<script>
import SalesList from '../components/SalesList.vue';
import SalesForm from '../components/SalesForm.vue';

export default {
  name: 'SalesView',
  components: {
    SalesList,
    SalesForm
  }
};
</script>

<style scoped>
</style>
