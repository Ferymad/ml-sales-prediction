<template>
  <div>
    <h2>{{ $t('inventory.title') }}</h2>
    <v-data-table
      :headers="headers"
      :items="inventory"
      :loading="loading"
      class="elevation-1"
    >
      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click="editItem(item)">mdi-pencil</v-icon>
        <v-icon small @click="deleteItem(item)">mdi-delete</v-icon>
      </template>
    </v-data-table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      headers: [
        { text: this.$t('inventory.headers.name'), value: 'name' },
        { text: this.$t('inventory.headers.quantity'), value: 'quantity' },
        { text: this.$t('inventory.headers.actions'), value: 'actions', sortable: false },
      ],
      inventory: [],
      loading: true,
    };
  },
  created() {
    this.fetchInventory();
  },
  methods: {
    async fetchInventory() {
      try {
        const response = await axios.get('/api/products'); // Ensure this is correct
        this.inventory = response.data;
      } catch (error) {
        console.error('Error fetching inventory:', error);
      } finally {
        this.loading = false;
      }
    },
    editItem(item) {
      // Implement edit functionality
    },
    deleteItem(item) {
      // Implement delete functionality
    },
  },
};
</script>
