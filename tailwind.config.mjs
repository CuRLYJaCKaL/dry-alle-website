import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const config = require('./config/site.config.json');

const brand = config.brand;

/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: brand.primaryColor,
        'primary-dark': brand.primaryDark,
        secondary: brand.secondaryColor,
        accent: brand.accentColor,
        'accent-light': brand.accentLight,
        surface: brand.surfaceColor,
        'surface-alt': brand.surfaceAlt,
        'text-primary': brand.textPrimary,
        'text-secondary': brand.textSecondary,
        border: brand.borderColor,
      },
      fontFamily: {
        heading: [brand.fontFamily, 'system-ui', 'sans-serif'],
        body: [brand.fontFamily, 'system-ui', 'sans-serif'],
      },
      fontSize: {
        'hero': ['clamp(2rem, 5vw, 3.5rem)', { lineHeight: '1.15' }],
        'section': ['clamp(1.5rem, 3vw, 2.25rem)', { lineHeight: '1.2' }],
      },
      spacing: {
        'section': 'clamp(3rem, 8vw, 6rem)',
        'component': 'clamp(1.5rem, 4vw, 3rem)',
      },
      boxShadow: {
        'card': '0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04)',
        'elevated': '0 10px 25px -5px rgba(0,0,0,0.1), 0 4px 6px -2px rgba(0,0,0,0.05)',
      }
    },
  },
  safelist: ['border-red-400'],
  plugins: [require('@tailwindcss/typography')],
};
