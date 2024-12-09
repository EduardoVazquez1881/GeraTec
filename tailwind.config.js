/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './web/geraGames/templates/**/*.html', // Ruta relativa a tus plantillas
  ],
  theme: {
    extend: {
      colors: { // Cambiado de "color" a "colors"
        fondo: '#10243d',
        fondonaranja: '#f27726',
        colorhover: '#f09709',
        azulhover: '#203a57'
      },
      spacing: {
        18: '4.5rem', // Equivale a 72px (18 * 4)
      },
    },
  },
  plugins: [],
};
