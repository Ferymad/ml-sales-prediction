<template>
  <div>
    <h2>{{ $t('sales.addSale') }}</h2>
    <form @submit.prevent="addSale">
      <label for="productName">{{ $t('sales.productName') }}</label>
      <input id="productName" v-model="productName" type="text" required />
      <label for="saleQuantity">{{ $t('sales.saleQuantity') }}</label>
      <input id="saleQuantity" v-model="saleQuantity" type="number" required />
      <label for="saleDate">{{ $t('sales.saleDate') }}</label>
      <input id="saleDate" v-model="saleDate" type="date" required />
      <button type="submit">{{ $t('sales.add') }}</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SalesForm',
  data() {
    return {
      productName: '',
      saleQuantity: 0,
      saleDate: ''
    };
  },
  methods: {
    async addSale() {
      try {
        await this.$axios.post('/api/sales', {
          productName: this.productName,
          quantity: this.saleQuantity,
          date: this.saleDate
        });
        this.productName = '';
        this.saleQuantity = 0;
        this.saleDate = '';
      } catch (error) {
        console.error('Error adding sale:', error);
      }
    }
  }
};
</script>

<style scoped>
h2 {
  font-size: 1.5em;
  margin-bottom: 1em;
}
form {
  display: flex;
  flex-direction: column;
}
label {
  margin-bottom: 0.5em;
}
input {
  margin-bottom: 1em;
}
button {
  align-self: flex-start;
}
</style>
