<template>
  <div>
    <h2>{{ $t('analytics.inventoryChart') }}</h2>
    <canvas ref="inventoryChart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  name: 'InventoryChart',
  data() {
    return {
      inventoryData: []
    };
  },
  mounted() {
    this.fetchInventoryData();
  },
  methods: {
    fetchInventoryData() {
      // Fetch inventory data from the backend API
      // Example: this.inventoryData = await fetch('/api/inventory').then(res => res.json());
      this.renderChart();
    },
    renderChart() {
      const ctx = this.$refs.inventoryChart.getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.inventoryData.map(item => item.name),
          datasets: [{
            label: this.$t('analytics.inventory'),
            data: this.inventoryData.map(item => item.quantity),
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    }
  }
};
</script>

<style scoped>
h2 {
  font-size: 1.5em;
  margin-bottom: 1em;
}
canvas {
  width: 100%;
  height: auto;
}
</style>
