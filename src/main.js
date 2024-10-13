import { createApp } from 'vue';
import App from './App.vue';
import i18n from './i18n';
import axios from 'axios';
import router from './router'; // Import Vue Router

const app = createApp(App);
app.use(i18n);
app.use(router); // Use Vue Router

// Configure Axios defaults
axios.defaults.baseURL = 'http://localhost:5000'; // Adjusted base URL

app.config.globalProperties.$axios = axios;

app.mount('#app');
