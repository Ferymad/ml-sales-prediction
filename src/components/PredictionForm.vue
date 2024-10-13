<template>
  <v-card class="pa-5">
    <v-form ref="form" v-model="valid" @submit.prevent="submitForm">
      <!-- Start Date -->
      <v-menu
        ref="startMenu"
        v-model="startMenu"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="form.date"
            label="Start Date"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
            :rules="[rules.required]"
          ></v-text-field>
        </template>
        <v-date-picker v-model="form.date" @input="startMenu = false"></v-date-picker>
      </v-menu>

      <!-- End Date -->
      <v-menu
        ref="endMenu"
        v-model="endMenu"
        :close-on-content-click="false"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="form.end_date"
            label="End Date"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
            :rules="[rules.required]"
          ></v-text-field>
        </template>
        <v-date-picker v-model="form.end_date" @input="endMenu = false"></v-date-picker>
      </v-menu>

      <!-- Product Code -->
      <v-text-field
        v-model="form.product_code"
        :rules="[rules.required]"
        label="Product Code"
        required
      ></v-text-field>

      <!-- Product Color -->
      <v-text-field
        v-model="form.product_color"
        :rules="[rules.required]"
        label="Product Color"
        required
      ></v-text-field>

      <!-- Product Model -->
      <v-text-field
        v-model="form.product_model"
        :rules="[rules.required]"
        label="Product Model"
        required
      ></v-text-field>

      <!-- Product Type -->
      <v-text-field
        v-model="form.product_type"
        :rules="[rules.required]"
        label="Product Type"
        required
      ></v-text-field>

      <!-- Submit Button -->
      <v-btn :disabled="!valid" color="primary" type="submit">Predict Sales</v-btn>
    </v-form>

    <!-- Prediction Result -->
    <v-alert
      v-if="prediction !== null"
      type="success"
      class="mt-4"
    >
      Predicted Sales Quantity: {{ prediction }}
    </v-alert>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PredictionForm',
  data() {
    return {
      valid: false,
      startMenu: false,
      endMenu: false,
      form: {
        date: '',          // Start Date
        end_date: '',      // End Date
        product_code: '',
        product_color: '',
        product_model: '',
        product_type: '',
      },
      prediction: null,
      rules: {
        required: (value) => !!value || 'Required.',
      },
    };
  },
  methods: {
    submitForm() {
      if (this.$refs.form.validate()) {
        // Prepare the data payload
        const payload = {
          date: this.form.date,
          end_date: this.form.end_date,
          product_code: this.form.product_code,
          product_color: this.form.product_color,
          product_model: this.form.product_model,
          product_type: this.form.product_type,
        };

        // Send POST request to the backend API
        axios
          .post('/api/predict', payload)
          .then((response) => {
            this.prediction = response.data.predicted_quantity;
          })
          .catch((error) => {
            console.error('Prediction error:', error);
            // Optionally, display an error message to the user
          });
      }
    },
  },
};
</script>

<style scoped>
.pa-5 {
  padding: 20px;
}
</style>
