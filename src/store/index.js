import { createStore } from 'vuex';
import axios from 'axios';

const store = createStore({
  state: {
    inventory: [],
    sales: [],
    predictions: []
  },
  mutations: {
    SET_INVENTORY(state, inventory) {
      state.inventory = inventory;
    },
    SET_SALES(state, sales) {
      state.sales = sales;
    },
    SET_PREDICTIONS(state, predictions) {
      state.predictions = predictions;
    }
  },
  actions: {
    async fetchInventory({ commit }) {
      try {
        const response = await axios.get('/inventory');
        commit('SET_INVENTORY', response.data);
      } catch (error) {
        console.error('Error fetching inventory:', error);
      }
    },
    async fetchSales({ commit }) {
      try {
        const response = await axios.get('/sales');
        commit('SET_SALES', response.data);
      } catch (error) {
        console.error('Error fetching sales:', error);
      }
    },
    async fetchPredictions({ commit }) {
      try {
        const response = await axios.get('/predictions');
        commit('SET_PREDICTIONS', response.data);
      } catch (error) {
        console.error('Error fetching predictions:', error);
      }
    }
  },
  modules: {}
});

export default store;
