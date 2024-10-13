<template>
  <div>
    <h2>{{ $t('inventory.addItem') }}</h2>
    <form @submit.prevent="addItem">
      <label for="itemName">{{ $t('inventory.itemName') }}</label>
      <input id="itemName" v-model="itemName" type="text" required />
      <label for="itemQuantity">{{ $t('inventory.itemQuantity') }}</label>
      <input id="itemQuantity" v-model="itemQuantity" type="number" required />
      <button type="submit">{{ $t('inventory.add') }}</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'InventoryForm',
  data() {
    return {
      itemName: '',
      itemQuantity: 0
    };
  },
  methods: {
    async addItem() {
      try {
        await this.$axios.post('/api/inventory', {
          name: this.itemName,
          quantity: this.itemQuantity
        });
        this.itemName = '';
        this.itemQuantity = 0;
      } catch (error) {
        console.error('Error adding item:', error);
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
