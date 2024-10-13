<template>
  <div>
    <InventoryList />
    <InventoryForm />
  </div>
</template>

<script>
import InventoryList from '../components/InventoryList.vue';
import InventoryForm from '../components/InventoryForm.vue';

export default {
  name: 'InventoryView',
  components: {
    InventoryList,
    InventoryForm
  }
};
</script>

<style scoped>
</style>
