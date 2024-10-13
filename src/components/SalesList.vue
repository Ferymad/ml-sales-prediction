<template>
  <div>
    <h1>Sales List</h1>
    <ul>
      <li v-for="sale in sales" :key="sale.id">
        {{ sale.date }} - Product ID: {{ sale.product_id }} - Quantity: {{ sale.quantity }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SalesList',
  data() {
    return {
      sales: [],
      // Other data properties
    };
  },
  methods: {
    async fetchSales() {
      try {
        const response = await this.$axios.get('/api/sales');
        this.sales = response.data;
      } catch (error) {
        console.error('Error fetching sales:', error);
        // Handle error appropriately, possibly setting an error message in the UI
      }
    },
    // Other methods
  },
  created() {
    this.fetchSales();
  },
};
</script>

<style scoped>
/* Add any necessary styles here */
</style>
