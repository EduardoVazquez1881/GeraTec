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
        85: '21.25rem', // Equivale a 340px (85 * 4)
        90: '22.5rem', // Equivale a 360px (90 * 4)   
        300: '75rem', // Equivale a 1200px (300 * 4)    
        250: '62.5rem', // Equivale a 1000px (250 * 4) 
        200: '50rem', // Equivale a 800px (200 * 4)
        180: '45rem', // Equivale a 720px (180 * 4)
        150: '37.5rem', // Equivale a 600px (150 * 4)
      },
    },
  },
  plugins: [
    ],
};
