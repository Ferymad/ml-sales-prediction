import { createI18n } from 'vue-i18n';
import en from './en.json';
import tr from './tr.json';

const messages = {
  en,
  tr
};

const i18n = createI18n({
  locale: 'en', // set locale
  fallbackLocale: 'en', // set fallback locale
  messages // set locale messages
});

export default i18n;
