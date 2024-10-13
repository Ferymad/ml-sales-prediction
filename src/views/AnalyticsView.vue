<template>
  <div>
    <SalesChart />
    <InventoryChart />
  </div>
</template>

<script>
import SalesChart from '../components/SalesChart.vue';
import InventoryChart from '../components/InventoryChart.vue';

export default {
  name: 'AnalyticsView',
  components: {
    SalesChart,
    InventoryChart
  }
};
</script>

<style scoped>
</style>
