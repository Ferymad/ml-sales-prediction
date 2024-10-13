<template>
  <div>
    <h2>{{ $t('prediction.result') }}</h2>
    <p>{{ $t('prediction.predictedSales') }}: {{ predictedSales }}</p>
  </div>
</template>

<script>
export default {
  name: 'PredictionResult',
  props: {
    predictedSales: {
      type: Number,
      required: true
    }
  }
};
</script>

<style scoped>
h2 {
  font-size: 1.5em;
  margin-bottom: 1em;
}
p {
  font-size: 1.2em;
}
</style>
