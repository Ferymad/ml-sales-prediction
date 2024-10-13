<template>
  <div>
    <h2>{{ $t('analytics.salesChart') }}</h2>
    <canvas ref="salesChart"></canvas>
  </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  name: 'SalesChart',
  data() {
    return {
      salesData: []
    };
  },
  mounted() {
    this.fetchSalesData();
  },
  methods: {
    fetchSalesData() {
      // Fetch sales data from the backend API
      // Example: this.salesData = await fetch('/api/sales').then(res => res.json());
      this.renderChart();
    },
    renderChart() {
      const ctx = this.$refs.salesChart.getContext('2d');
      new Chart(ctx, {
        type: 'line',
        data: {
          labels: this.salesData.map(sale => sale.date),
          datasets: [{
            label: this.$t('analytics.sales'),
            data: this.salesData.map(sale => sale.quantity),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
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
