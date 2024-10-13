import { createRouter, createWebHistory } from 'vue-router';
import InventoryView from '../views/InventoryView.vue';
import SalesView from '../views/SalesView.vue';
import PredictionView from '../views/PredictionView.vue';
import AnalyticsView from '../views/AnalyticsView.vue';

const routes = [
  {
    path: '/',
    redirect: '/inventory' // Default route
  },
  {
    path: '/inventory',
    name: 'Inventory',
    component: InventoryView
  },
  {
    path: '/sales',
    name: 'Sales',
    component: SalesView
  },
  {
    path: '/prediction',
    name: 'Prediction',
    component: PredictionView
  },
  {
    path: '/analytics',
    name: 'Analytics',
    component: AnalyticsView
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
